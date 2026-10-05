# ROS 2 接入与兼容

[返回首页](../README.zh-CN.md) · [先接通单手](quickstart.md) · [SDK](sdk.md)

机器人端适配由 [roboparty_dexhand_ros](https://github.com/Roboparty/roboparty_dexhand_ros) 维护。它通过 `dexhand_py` 控制设备，双手各用一个独立进程。

## 版本状态

| 来源 | 当前说明 | 使用判断 |
| --- | --- | --- |
| SDK 文档 `046108e` | Ubuntu 24.04、Python 3.12、镜像内置驱动，面向 Jazzy 下游 | 可以作为独立 SDK 文档基线；不等于整个 ROS 组合已验证 |
| ROS 包 `bfc325f` | 已验证环境为 Ubuntu 22.04、Python 3.10、Humble；驱动最低版本写为 0.4.2 | 需使用与该 Python ABI 匹配的驱动，不能直接套用 Python 3.12 路径 |
| 飞书原版 ROS 示例 | Humble / EtherCAT，`lhandpro_service` 和 RViz 示例 | 是另一条原版集成路线，不是当前 CAN-FD ROS 包 |

上游目前存在安装说明差异：ROS README 引用了 `~/roboparty_dexhand/setup.bash`，而当前 SDK 构建文档明确不提供该文件。源码安装路径应以对应 SDK 版本的构建说明为准。

SDK README 提到的下游 `configure_feedback` 在本次检查的 ROS 包中尚未实现。当前可用的配置入口是 [快速开始](quickstart.md) 中的 `roboparty-dexhand-config`；配置时先停止 ROS 节点和其他控制进程。

## 已有接口

| 接口 | 类型 | 行为 |
| --- | --- | --- |
| `/dexhand_left/cmd` | `std_msgs/msg/Int32MultiArray` | 六个位置指令，范围 `0..10000`，按配置速度执行 |
| `/dexhand_left/init` | `std_srvs/srv/Trigger` | 重建实例并使能，不回零；只用于零位可信的恢复场景 |
| `/dexhand_left/reset` | `std_srvs/srv/Trigger` | 重建、使能并回零，会产生运动 |

右手将名字中的 `left` 替换为 `right`。默认左手接口为 `can0`，右手为 `can3`，需要与实际接线一致。完整参数由 [ROS README](https://github.com/Roboparty/roboparty_dexhand_ros/blob/bfc325f2d5d7bf33d3a64ebdc79b01ed3641f227/README.md) 维护。

## 当前限制

当前节点在位置命令中执行 `set_move_no_home(1)`，会允许未完成回零时运动，与 SDK 推荐的回零要求不一致。参见 [节点实现](https://github.com/Roboparty/roboparty_dexhand_ros/blob/bfc325f2d5d7bf33d3a64ebdc79b01ed3641f227/roboparty_dexhand_ros/dexhand_node.py#L277)。在修正并验证冷启动/恢复行为前，优先使用 SDK 的受控单手验收流程；本页不把当前 ROS 默认运动路径列为已验收的快速开始。

当前 CAN-FD ROS 包没有发布位置、状态、电流、报警或 `/joint_states`，不能直接沿用原版 EtherCAT 示例中的 RViz 反馈能力说明。后续补齐带时间信息的反馈和 [关节映射](models.md) 后，再提供 RViz 与 rosbag 流程。

## 集成验收需要记录

记录镜像版本、Ubuntu、Python、ROS 发行版、SDK 包/tag、ROS commit、硬件/固件、左右手接口与 node ID。分别验证通信初始化、冷启动回零、零位可信时恢复、异常退出、双进程资源隔离和反馈行为。

本页为集成状态说明，尚不声明 Jazzy/Humble 与任意驱动 Release 可以自由组合。
