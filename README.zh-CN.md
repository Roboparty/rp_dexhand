<a id="top"></a>

<p align="center">
  <a href="https://github.com/Roboparty/RP1">RP1 人形机器人</a> &nbsp; / &nbsp; <strong>RP Hand 灵巧手</strong> &nbsp; / &nbsp; <a href="https://github.com/Roboparty/roboparty_dexhand">SDK</a>
</p>

<h1 align="center">RP Hand</h1>

<p align="center">
  面向人形机器人的紧凑型五指灵巧手。<br>
  六轴主动控制，CAN-FD 接入，配套软件与模型齐备。
</p>

<p align="center">
  <a href="README.md">English</a> &nbsp; | &nbsp; <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <img src="assets/rp-hand.gif" alt="RP Hand 在 RP1 人形机器人上的快换安装演示" width="760">
</p>

<p align="center"><sub>RP Hand 在 RP1 上的快换安装。</sub></p>

<p align="center">
  <a href="docs/quickstart.md"><strong>快速开始</strong></a> &nbsp; · &nbsp;
  <a href="docs/downloads.md"><strong>软件与模型下载</strong></a> &nbsp; · &nbsp;
  <a href="https://github.com/Roboparty/roboparty_dexhand"><strong>SDK 源码</strong></a>
</p>

## 产品概览

RP Hand 面向中小尺寸人形机器人的五指操作，采用紧凑的蜗轮蜗杆机构，具有 **11 个机械自由度，其中 6 个主动控制轴**。搭配 RP1 的 CAN-FD 通信链路，可实现整机内走线。

- **整机适配**：提供尺寸图、引脚图与左右手 CAD，便于完成安装和接线。
- **设备调试**：配套 Windows 上位机，用于调试与参数配置。
- **视觉手势控制**：提供 Windows 和 Linux 手势识别 Demo 软件包。
- **程序开发**：Linux CAN-FD SDK 提供 C++、Python 及配套 ROS 2 接口，另提供 URDF 和 MJCF 模型。

## 产品参数

| 参数 | 数值 |
| --- | --- |
| 手指数 | 5 |
| 机械自由度 | 11：6 个主动控制轴，5 个被动 / 联动自由度 |
| 外形尺寸 | 147.54 × 73.53 × 26.35 mm |
| 质量 | 379 ± 10 g |
| 传动方式 | 蜗轮蜗杆 |
| RP1 通信方式 | CAN-FD |

[查看尺寸、供电与引脚说明 →](docs/hardware.md)

## 按需开始

| 调试与体验 | 编写控制程序 | 安装与模型适配 |
| --- | --- | --- |
| 配置设备参数，运行手势识别 Demo。 | 通过 CAN-FD 接入 C++、Python 或 ROS 2 程序。 | 核对安装空间，使用左右手 CAD 与机器人模型。 |
| [配套软件](docs/software.md) · [下载](docs/downloads.md) | [快速开始](docs/quickstart.md) · [SDK 仓库](https://github.com/Roboparty/roboparty_dexhand) | [硬件手册](docs/hardware.md) · [CAD / URDF / MJCF](docs/models.md) |

首次接入机器人时，先核对[硬件接线](docs/hardware.md)，按[快速开始](docs/quickstart.md)完成单手控制，再按需接入 [ROS 2](docs/ros2.md)。ROS 2 包位于 SDK 仓库的 `ros2/rphand_ros`，与 SDK 一同构建。

## 文档导航

| 指南 | 内容 |
| --- | --- |
| [快速开始](docs/quickstart.md) | Linux 环境、SDK 构建、CAN-FD 配置与首次连接 |
| [C++ / Python SDK](docs/sdk.md) | 控制流程、六轴顺序、单位与状态反馈 |
| [ROS 2 接入](docs/ros2.md) | Jazzy 构建、双手启动、指令与数据记录 |
| [硬件手册](docs/hardware.md) | 外形尺寸、供电、引脚与接线 |
| [配套软件](docs/software.md) | 上位机与手势识别 Demo |
| [模型与 CAD](docs/models.md) | 左右手 CAD、URDF、MJCF 与关节映射 |
| [下载](docs/downloads.md) | 应用软件、模型与协议文件 |
| [常见问题](docs/troubleshooting.md) | 构建、通信与运动问题排查 |

## 支持与贡献

产品文档和资源问题请在 [rp_dexhand Issues](https://github.com/Roboparty/rp_dexhand/issues) 提交；C++、Python 及 ROS 2 代码问题请在 [SDK Issues](https://github.com/Roboparty/roboparty_dexhand/issues) 提交。

[参与贡献](CONTRIBUTING.md) · [许可信息](LICENSES.md) · [资料来源](NOTICE.md) · [返回顶部](#top)
