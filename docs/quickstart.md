# 单手 CAN-FD 快速开始

[返回首页](../README.zh-CN.md) · [接线](hardware.md) · [排障](troubleshooting.md)

本流程采用当前维护的 `roboparty_dexhand`，适用于 RP Hand 六主动轴。示例中的 `can0` 和 node ID `1` 必须与实物对应。先阅读硬件接线说明，停止其他控制同一只手的程序。

## 1. 选择安装方式

| 环境 | 入口 |
| --- | --- |
| RoboParty 镜像已内置驱动 | 直接执行下一节的环境检查 |
| 已确认适配系统、Python 和 CPU 架构的软件包 | 从 [下载页](downloads.md) 获取；同时需要 `roboparty-base` 提供公共环境入口 |
| 需要开发或适配其他环境 | 按 [SDK 构建说明](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/docs/build.md) 从源码构建 |

当前 SDK 文档基线是 Ubuntu 24.04、系统 Python 3.12。Python 扩展需要与解释器版本和 CPU 架构匹配。源码构建不提供仓库根目录的 `setup.bash`，应使用构建文档中的路径配置方式。驱动可以脱离 ROS 使用。

## 2. 检查镜像中的软件环境

以下命令在板端 Bash 运行，不会连接、使能或回零灵巧手：

```bash
source /opt/roboparty/setup.bash
/usr/bin/python3 -c 'import dexhand_py; print(dexhand_py.__file__)'
/usr/bin/python3 -c 'from dexhand_py import HandModel; print(HandModel.RP_HAND_6DOF.value)'
roboparty-dexhand-config --help
dpkg-query -W roboparty-dexhand roboparty-base
```

预期模块来自 `/opt/roboparty/`，模型值为 `0`，配置工具可用。缺少环境脚本时先检查安装，不能把 SDK 的 `.so` 单独复制到另一套 Python 环境中。

## 3. 检查接口

```bash
ip -details -statistics link show can0
```

目标接口应处于 `UP`，启用 CAN-FD，显示 `bitrate 1000000`、`dbitrate 5000000`。未配置时按 [SDK CAN-FD 配置步骤](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/docs/hardware-setup.md) 操作。重新配置接口会中断该接口上的通信。

## 4. 配置并验证反馈周期

新设备、更换设备、恢复出厂或配置未知时执行。这个步骤会修改手本体参数，配置期间不能同时运行手控制程序。

```bash
roboparty-dexhand-config feedback-period apply --interface can0 --node-id 1 --milliseconds 20 --save
```

给手本体断电再上电，然后查询：

```bash
roboparty-dexhand-config feedback-period show --interface can0 --node-id 1
```

六轴 raw value 都应为 `200`。如果 `apply` 返回 `already-compliant`，仍需完成断电后的读回确认。正常的 `init_hand()` 不负责持久化反馈周期。

20 ms 表示两类反馈各约 50 Hz，合计约 100 帧/秒/手；不是 100 Hz 的单类状态采样率，也不是整机 500 Hz 控制环的承诺。

## 5. 只初始化通信

以下示例会向设备发送初始化配置，但不会请求使能或回零。先完成上面的供电、接口与反馈配置：

```python
from dexhand_py import HandDriver, HandModel

hand = HandDriver.create_hand(
    "RP_Hand", "canfd", "can0", HandModel.RP_HAND_6DOF, 1
)
try:
    if not hand.init_hand(False, False, 0.0):
        raise RuntimeError("Communication initialization failed")
    hand.check_health()
    print("total DOF, active DOF:", hand.get_dof())
finally:
    hand.deinit_hand()
```

期望 DOF 为 `(11, 6)`。这只完成驱动初始化检查，不代表真实运动、回零或反馈新鲜度验收通过。运行结束后，先确认程序退出，再进入运动步骤。

## 6. 使能、回零与单手运动

这一阶段会产生真实运动。确认运动范围内无障碍物，准备硬件停止手段，并根据机构及负载确认目标值与速度。

使用 SDK 维护的 [完整 Python / C++ 示例](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/docs/api.md)。当前示例包含使能、回零、到目标位置、返回零位及资源释放。初始化失败时停止排查，不要设置 `set_move_no_home(1)` 绕过回零。

`home_wait_time=5.0` 是最大等待秒数；成功会提前返回。新创建实例在回零后需要收到新鲜的位置与状态反馈，才会确认回零结果。仅进程重启且本体没有掉电、零位可信的恢复场景，应按 SDK 文档处理，不能将此假设用于冷启动。

## 7. 验收与双手扩展

按 [SDK 部署与验收 SOP](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/VALIDATION.md) 检查实际动作、位置反馈、报警、帧率和参数持久化。getter 返回缓存，固定等待时间不能证明动作已经完成。

记录设备型号/左右手、固件、系统/Python、SDK 版本、CAN 接口与 node ID，再记录运行结果。这里的步骤是整理后的流程，未声明已经在你的设备上实测通过。

双手保持一手一 OS 进程。进入 ROS 前阅读 [ROS 版本与当前限制](ros2.md)。
