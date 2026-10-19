# 版本兼容与迁移

[首页](../README.zh-CN.md) · [English](en/compatibility.md) · [快速开始](quickstart.md)

新项目推荐从 [SDK `eb923ac`](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39) 源码构建，并使用同仓库内的 ROS 适配。先按独立 SDK 完成单手接入，再按需加入 ROS。

| 路线 | 接口 / 环境 | 使用方式 |
| --- | --- | --- |
| 当前源码 SDK | `rphand::Hand` / `rphand.Hand`；Linux、C++17、CMake ≥ 3.20、Python ≥ 3.9 | 推荐用于新项目，按目标计算机与解释器构建 |
| 当前配套 ROS | `rphand_ros`；ROS 2 Jazzy | 与当前 SDK 同仓库构建，已实现 state 发布 |
| 旧版 SDK `046108e` / v0.5.0 包 | `HandDriver` / `dexhand_py`；Debian 包与镜像入口 | 仅用于已有系统维护，不与当前 API 混用 |
| 原版软件及 EtherCAT 示例 | 独立 SDK / 应用包 | 保留在[资源下载](downloads.md)，不视为当前 CAN-FD 路线的功能 |

## 主要变化

| 旧版 | 当前 |
| --- | --- |
| `from dexhand_py import HandDriver, HandModel` | `from rphand import Hand` |
| 工厂创建 + `init_hand()` | `Hand()` + `connect(interface, node_id)`，随后明确配置/使能/回零 |
| `roboparty-dexhand-config` 配反馈 | `connect()` 配置并检查周期反馈 |
| 厂商二进制及进程级回调 | 源码协议与独立 Session；同一接口/ID仍不能被多个控制程序占用 |
| 旧 ROS 包无状态发布 | 配套 `rphand_ros` 发布自定义 `state` |
| 旧文档中的电流 mA 表述 | 当前电流限制为额定电流千分比，`0..3000` |

这不是可直接覆盖旧 `.so` 的升级。应用需迁移方法调用、单位、状态检查和退出流程；原版、旧封装和当前源码分别使用独立安装路径及终端环境。

## 验证状态

SDK 在 Ubuntu 24.04 x86-64 的 C++ / Python 构建、安装、离线测试及外部 CMake 工程链接由 [CI](https://github.com/Roboparty/rp_dexhand/actions/runs/39203726788)检查。

ARM64、ROS 2 和实机部署需在目标设备上完成对应检查，并记录硬件/固件、系统、Python ABI 与动作工况。

已有系统的 SDK 参考版本为 [`046108e`](https://github.com/Roboparty/roboparty_dexhand/tree/046108e7ba800763a096ca1c99b04a8414797105)。旧 v0.5.0 软件包不提供当前 `rphand` API。ROS 接入统一使用当前 SDK 中的 `ros2/rphand_ros`。
