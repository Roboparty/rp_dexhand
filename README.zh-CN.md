# RP Hand

![CAN-FD](https://img.shields.io/badge/Transport-CAN--FD-2563eb)
![C++17](https://img.shields.io/badge/C%2B%2B-17-64748b)
![Python](https://img.shields.io/badge/Python-3.9%2B-64748b)
![ROS 2](https://img.shields.io/badge/ROS_2-Jazzy-64748b)

[English](README.md) | [简体中文](README.zh-CN.md)

**面向机器人集成的紧凑型六轴灵巧手，提供 C++、Python 与 ROS 2 接口。**

![RP Hand 在 RP1 上的快换安装演示](assets/rp-hand.gif)

RP Hand 是一款面向中小尺寸人形机器人的五指灵巧手，通过 CAN-FD 接入机器人控制系统。这里提供硬件接线、软件接入和模型资源，控制代码见 [roboparty_dexhand](https://github.com/Roboparty/roboparty_dexhand)。

**维护方：** RoboParty · **支持：** [GitHub Issues](https://github.com/Roboparty/rp_dexhand/issues) · **整机平台：** [RP1](https://github.com/Roboparty/RP1)

## 特性

- 五指机构，11 个机械自由度，6 个主动控制轴。
- 通过 CAN-FD 接入 RP1，配合整机连接方案支持内走线。
- C++ `rphand::Hand` 与 Python `rphand.Hand` 共用设备控制实现。
- 配套 `rphand_ros`，提供目标指令、初始化服务与状态反馈。
- 提供 Windows 上位机，以及 Windows / Linux 手势识别 Demo 软件包。
- 提供左右手 CAD、URDF 与 MJCF 资源，按版本组织下载与校验值。

推荐开发路线为 **Linux + CAN-FD + 当前源码 SDK**。其他通信方式的原版资料单独归档，新旧接口区别见[版本兼容](docs/compatibility.md)。

## 配套工具

| 工具 | 开发用途 | 入口 |
| --- | --- | --- |
| Windows 上位机 | 设备调试与参数配置 | [应用与版本](docs/software.md) |
| 手势识别 Demo | 视觉手势识别演示，提供 Windows / Linux 包 | [手势软件](docs/software.md) |
| C++ / Python / ROS 2 | 自定义控制程序、整机接入与反馈记录 | [SDK](docs/sdk.md) · [ROS 2](docs/ros2.md) |
| CAD / URDF / MJCF | 安装适配与机器人模型开发 | [模型资源](docs/models.md) |

## 产品参数

| 参数 | 产品手册规格 |
| --- | --- |
| 外形尺寸 | 147.54 × 73.53 × 26.35 mm |
| 质量 | 379 ± 10 g |
| 自由度 | 6 个主动控制轴，另有 5 个被动 / 联动自由度 |
| 传动方式 | 蜗轮蜗杆 |
| 平台接入 | CAN-FD；安装及电气细节见硬件手册 |

选型与安装前请核对交付产品的硬件版本。[查看尺寸、供电与引脚 →](docs/hardware.md)

## 文档

| 指南 | 内容 |
| --- | --- |
| [快速开始](docs/quickstart.md) | 环境准备、源码构建、CAN 接口与首次连接 |
| [C++ / Python SDK](docs/sdk.md) | 接口、六轴顺序、单位与状态有效性 |
| [ROS 2 接入](docs/ros2.md) | Jazzy 构建、命令、反馈与数据记录 |
| [硬件手册](docs/hardware.md) | 外形尺寸、供电、CAN-FD 引脚与接线 |
| [模型与 CAD](docs/models.md) | 左右手模型、结构文件与映射状态 |
| [下载](docs/downloads.md) | 上位机、手势 Demo、SDK 源码与原版附件 |
| [版本兼容](docs/compatibility.md) | 推荐 SDK 基线及旧接口迁移 |
| [常见问题](docs/troubleshooting.md) | 构建、连接、运动与反馈检查 |

## 开始使用

源码基线为 [SDK `eb923ac`](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39)。需要 Linux、CMake ≥ 3.20 和 C++17 编译器；Python 绑定另需 Python ≥ 3.9、开发头文件和 pybind11。配套 ROS 构建入口面向 Jazzy。版本选择与已有系统升级见[版本兼容](docs/compatibility.md)。

```bash
git clone https://github.com/Roboparty/roboparty_dexhand.git
cd roboparty_dexhand
git checkout eb923acf61a02febabc9db90ad4d5eed84ffbc39
bash build.sh cpp
RPHAND_PYTHON=/usr/bin/python3 bash build.sh python
RPHAND_PYTHON=/usr/bin/python3 source setup_python.sh
/usr/bin/python3 -c 'from rphand import Hand; print(Hand)'
```

上述命令只构建和导入 SDK，不连接设备。接入实机前继续阅读[快速开始](docs/quickstart.md)。当前源码使用 `rphand`，旧版 `dexhand_py` 的 API 不适用于这条路线。

## 软件架构

```text
C++ application       Python application       ROS 2 Jazzy
rphand::Hand          rphand.Hand               rphand_ros
        \                  |                     /
         +---------- shared C++ SDK ------------+
                           |
                    Linux SocketCAN
                           |
                         CAN-FD
                           |
                         RP Hand
```

SDK 处理协议编解码、状态反馈与设备会话；ROS 层负责周期目标发送和状态发布。[查看接口说明 →](docs/sdk.md)

## 仓库结构

| 路径 | 内容 |
| --- | --- |
| `docs/` | 中文产品与集成文档 |
| `docs/en/` | 英文入门与参考文档 |
| `assets/` | 安装动图、尺寸图与引脚图 |
| `resources/` | 按版本归档的资源清单、来源与校验值 |
| `tools/`、`tests/` | 离线文档检查与检查器测试 |

## 贡献与许可

文档检查和问题提交方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。资料版本和验证范围见[维护记录](docs/maintenance.md)。

许可信息见 [LICENSES.md](LICENSES.md)，资料来源见 [NOTICE.md](NOTICE.md)。
