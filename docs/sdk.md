# SDK 接入

[返回首页](../README.zh-CN.md) · [快速开始](quickstart.md) · [下载](downloads.md)

## 选择哪套 SDK

| 路线 | 使用场景 | 入口 |
| --- | --- | --- |
| RoboParty 维护的封装 | Linux CAN-FD、RP Hand 六主动轴、C++ / Python 应用和机器人集成 | [roboparty_dexhand](https://github.com/Roboparty/roboparty_dexhand) |
| 厂商原版 SDK | 使用厂商 Windows/Linux 包及其 EtherCAT、CAN-FD、RS485 示例；具体组合以原版说明为准 | [原版资源列表](downloads.md) |

本项目默认推荐第一条路线。旧 `roboparty_hand` 的 `hand_py`、`connect_by_config()` 与当前 `dexhand_py` 不是同一套接口，不应混用教程。

## 封装结构

Python 应用通过 `dexhand_py` 调用公共 `HandDriver`；C++ 应用直接使用 `HandDriver`。私有 `LHandProDriver` 将厂商 SDK 适配器、SocketCAN 传输、回调和生命周期管理连接起来。厂商 `libLHandProLib.so` 仍属于底层依赖。

| 名称 | 含义 |
| --- | --- |
| `roboparty_dexhand` | SDK 源码项目 |
| `roboparty-dexhand` | Debian 软件包 |
| `dexhand_py` | Python 扩展模块 |
| `HandDriver` | 公共 C++ / Python 驱动接口 |
| `roboparty-dexhand-config` | 反馈参数配置工具 |
| `roboparty-base` | 提供 `/opt/roboparty/setup.bash` 的基础环境包 |

## API 与使用边界

- 新程序使用产品名 `RP_Hand`、接口 `canfd` 和 `HandModel.RP_HAND_6DOF`。
- 构造工厂不执行通信；`init_hand()` 才建立设备会话，可明确选择是否使能、回零。
- 成功创建后使用 `try/finally` 或对应 C++ 异常处理调用 `deinit_hand()`。
- 同一进程仅允许一个活动手实例，双手部署为两个进程。
- 读取轴 ID 为 `1..6`；允许广播的控制方法中 `0` 代表全部轴，不能将其当作第一个手指。
- `get_now_*()` 读取缓存，`check_health()` 不能替代带时间信息的反馈新鲜度判断。
- 当前公共 API 没有触觉读取，也不能由保留的旧枚举推断 RP Hand 支持 16 个主动轴。

SDK 接口将位置标注为编码器计数、速度为计数/秒、角度为度、电流为 mA。原始 CAN-FD 协议另有“总行程系数，默认 10000”的表述。将其接入弧度制模型前，应核验具体设备的转换和逐轴范围，不能直接使用通用线性换算假设。

## 权威文档

本版接入说明基于 SDK commit `046108e7ba800763a096ca1c99b04a8414797105`。完整内容维护在 SDK 仓库中：

- [Python / C++ API 与示例](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/docs/api.md)
- [CAN-FD 与反馈配置](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/docs/hardware-setup.md)
- [源码构建与 Debian 打包](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/docs/build.md)
- [硬件验收](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/VALIDATION.md)
- [已发布软件包](https://github.com/Roboparty/roboparty_dexhand/releases)
- [厂商二进制版本和许可说明](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/thirdparty/README.md)

源码文档基线与 Release 是不同的版本标识。安装时同时记录包版本、目标系统和 Python ABI，不用 main 分支日期替代软件包的兼容信息。
