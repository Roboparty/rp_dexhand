# RP Hand

[English](README.md) | [简体中文](README.zh-CN.md)

![RP Hand 在 RP1 上的快换安装演示](assets/rp-hand.gif)

RP Hand 是面向中小尺寸人形机器人的紧凑型灵巧手，具有 **11 个机械自由度、6 个主动控制轴**。本仓库整理产品资料和集成指南；持续更新的 Linux CAN-FD 驱动由 [roboparty_dexhand](https://github.com/Roboparty/roboparty_dexhand) 维护。

| 产品参数 | 数值 |
| --- | --- |
| 尺寸 | 147.54 × 73.53 × 26.35 mm |
| 重量 | 379 g ± 10 g |
| 传动方式 | 蜗轮蜗杆 |
| 自由度 | 6 个主动控制轴，另有 5 个被动/联动自由度 |
| 触觉 | 可选配；当前 RoboParty 驱动公共 API 未提供触觉读取接口 |

以上参数整理自产品手册。选型与集成时应确认交付产品的硬件版本及选配情况。

## 从这里开始

| 你要完成的任务 | 文档 |
| --- | --- |
| 查看尺寸、供电、引脚和接线 | [硬件手册](docs/hardware.md) |
| 通过 CAN-FD 接通并控制一只手 | [快速开始](docs/quickstart.md) |
| 使用最新版 C++ / Python 驱动 | [SDK 接入](docs/sdk.md) |
| 接入 ROS 2 | [ROS 2 与版本兼容](docs/ros2.md) |
| 查找模型、理解关节对应关系 | [URDF、MJCF 与 CAD](docs/models.md) |
| 获取指定版本的软件包 | [下载与可用状态](docs/downloads.md) |
| 排查安装、通信和回零问题 | [常见问题](docs/troubleshooting.md) |

## 软件分工

| 项目 | 职责 |
| --- | --- |
| [roboparty_dexhand](https://github.com/Roboparty/roboparty_dexhand) | Linux CAN-FD 驱动、`HandDriver` C++ 接口、`dexhand_py` Python 模块、反馈配置工具和 amd64/arm64 软件包 |
| [roboparty_dexhand_ros](https://github.com/Roboparty/roboparty_dexhand_ros) | 一手一进程的 ROS 节点、位置命令话题和初始化/回零服务；版本与当前限制见 ROS 指南 |
| 厂商 SDK 与调试软件 | 独立的原版软件及示例；操作系统、协议和下载状态见下载表 |

本仓库推荐的 RoboParty SDK 路线为 **Linux + CAN-FD + 六主动轴**。产品资料中的 Windows、EtherCAT、RS485 和触觉能力不代表此封装已经实现。双手使用两个 OS 进程，驱动 getter 读取缓存反馈。

当前 SDK 文档面向 Ubuntu 24.04 / Python 3.12 镜像，下游 ROS README 的已验证环境仍为 Ubuntu 22.04 / Python 3.10 / Humble。组合安装前请阅读 [兼容说明](docs/ros2.md)，本仓库暂不将完整 Jazzy 组合标为已验证。

## 资料与维护

尺寸图、引脚图已存入仓库，可以直接查看。大型厂商软件和 CAD/模型附件尚未镜像到本仓库，下载表会明确原始入口和访问条件；已发布的 RoboParty 驱动直接链接其 Release。

产品文档问题提交到 [本仓库 Issues](https://github.com/Roboparty/rp_dexhand/issues)，驱动问题提交到 [SDK Issues](https://github.com/Roboparty/roboparty_dexhand/issues)，ROS 问题提交到 [ROS Issues](https://github.com/Roboparty/roboparty_dexhand_ros/issues)。

[资料来源与更新流程](docs/maintenance.md) | [第三方与素材说明](NOTICE.md)
