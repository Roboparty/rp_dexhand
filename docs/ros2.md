# ROS 2 Jazzy 接入

[首页](../README.zh-CN.md) · [English](en/ros2.md) · [SDK](sdk.md) · [旧版迁移](compatibility.md)

推荐使用 [SDK `eb923ac`](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39) 内置的 `ros2/rphand_ros`。节点直接调用 C++ SDK，提供双手 launch、位置命令、reset 服务和状态反馈。ROS 接入与 SDK 使用同一份源码，无需额外克隆驱动仓库。

## 构建与启动

先完成[单手接线与接口检查](quickstart.md)，再按 [ROS 2 Jazzy 官方文档](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)准备 ROS。以下在同一 SDK 根目录执行：

```bash
source /opt/ros/jazzy/setup.bash
sudo apt install python3-colcon-common-extensions python3-rosdep
# 首次使用 rosdep 时先按 ROS 安装文档完成初始化
rosdep update
rosdep install --from-paths ros2 --ignore-src -r -y --rosdistro jazzy
bash build.sh ros
source install/ros/local_setup.bash
ros2 launch rphand_ros dual_hand.launch.py command_rate_hz:=50
```

显式选择 50 Hz 目标发送频率，避免默认 launch 的 200 Hz 覆盖 YAML 中的 50 Hz。双手默认左 `can0`、右 `can3`，节点 ID 各为 `1`。仅左手时加入 `right:=false`；接口及 ID 可通过 `left_interface`、`right_interface`、`left_node_id`、`right_node_id` 调整。

启动本身不连接、使能或回零，等待 reset。新终端均需重新加载 ROS 和 `install/ros/local_setup.bash`。

## 初始化与命令

确认工作空间与停止措施后执行；reset 会使能并驱动整手回零：

```bash
ros2 service call /dexhand_left/reset std_srvs/srv/Trigger '{}'
ros2 topic echo /dexhand_left/state
```

`success=true` 仅代表请求受理。等待日志 `Reset complete; waiting for a new target`，再检查随后收到的反馈：状态有效、六轴已使能并完成回零、故障码为零。reset 会重新初始化设备并执行回零。

初始化完成后可使用：

```bash
ros2 run rphand_ros command.py --side left 0 0 1000 1000 1000 1000
```

六个整数按[六轴顺序](sdk.md)表示绝对行程目标 `0..10000`。发送成功不代表到位，位置全零也不等于 stop 或 home。

## 话题与数据采集

| 接口（左手） | 类型 | 含义 |
| --- | --- | --- |
| `/dexhand_left/cmd` | `std_msgs/msg/Int32MultiArray` | 六轴位置目标，action 输入 |
| `/dexhand_left/state` | `rphand_ros/msg/DexHandState` | 六轴反馈与 `feedback_valid` |
| `/dexhand_left/reset` | `std_srvs/srv/Trigger` | 受理连接、参数配置、使能和回零 |

右手将 `left` 替换为 `right`。状态包含位置、速度、电流、使能、回零、力矩到位与故障码。当前发布自定义 `state`，没有 `/joint_states`；不能直接把行程当量传给弧度制关节模型。

安装 ROS 的 rosbag2 CLI 及对应存储插件后，可记录已发布的双手 state/action：

```bash
ros2 bag record -o rp_hand_session   /dexhand_left/cmd /dexhand_left/state   /dexhand_right/cmd /dexhand_right/state
```

`cmd` 没有消息内时间戳，bag 保存接收时刻；`state.header.stamp` 记录 ROS 发布时间。状态两组反馈异步，初始化及阻塞调用期间可能暂停发布。采集端应检查反馈有效性、消息时效和记录频率；与整机视频联合采集时，还需统一时间基准。

## 运行边界

节点按设置频率重复发送最新目标，未收到新命令时仍保持最后目标，没有命令超时自动停止。停止发布 cmd 不等于停止设备；正常退出节点会尝试停止、失能和断开，通信故障或强制终止不能保证清理完成。当前没有 stop 服务，也没有反馈失效后的自动停止流程。

参数、清理流程和无硬件生命周期测试见[上游 ROS 文档](https://github.com/Roboparty/roboparty_dexhand/blob/eb923acf61a02febabc9db90ad4d5eed84ffbc39/docs/ros2.md)。
