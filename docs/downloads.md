# 下载与可用状态

[返回首页](../README.zh-CN.md) · [SDK 选择](sdk.md) · [模型说明](models.md)

核对日期：2026-10-05。表中的“原始飞书”代表需要该文档的访问权限，不代表已在 GitHub 镜像或公开发布。

## RoboParty 维护的驱动

| 资源 | 版本/架构 | 下载入口 |
| --- | --- | --- |
| Linux Debian 包 | v0.5.0 / amd64 | [roboparty-dexhand_0.5.0-1_amd64.deb](https://github.com/Roboparty/roboparty_dexhand/releases/download/v0.5.0/roboparty-dexhand_0.5.0-1_amd64.deb) |
| Linux Debian 包 | v0.5.0 / arm64 | [roboparty-dexhand_0.5.0-1_arm64.deb](https://github.com/Roboparty/roboparty_dexhand/releases/download/v0.5.0/roboparty-dexhand_0.5.0-1_arm64.deb) |
| SDK 源码与其他 Release | 以选定 tag 为准 | [源码](https://github.com/Roboparty/roboparty_dexhand) · [Release 列表](https://github.com/Roboparty/roboparty_dexhand/releases) |
| ROS 适配包源码 | 兼容性见 [ROS 指南](ros2.md) | [roboparty_dexhand_ros](https://github.com/Roboparty/roboparty_dexhand_ros) |

这些 deb 是已确认存在的上游发布资产。本次没有安装运行或计算它们的校验值，不声明跨系统/Python ABI 兼容。安装前确认目标环境，并获取匹配的 `roboparty-base`；已有配套镜像的用户通常不需要重复安装。

## 厂商软件与配套应用

| 资源 | 原始文件/版本 | 入口与状态 |
| --- | --- | --- |
| Windows 上位机 | `RP_Hand-v1.4.0-2026-08-25.zip` | [原始飞书](https://roboparty.feishu.cn/docx/VnbPdcs9toG7a1xe9l2cwVujnOe)，约 206 MB，未镜像 |
| 手势软件 Windows | `RP-Hand Gesture Setup 1.1.1.exe` | [原始飞书](https://roboparty.feishu.cn/docx/UDyrdMlzyoJ1YaxHlb8cwkFenXg)，约 300 MB，未镜像 |
| 手势软件 Linux amd64 | `RP-Hand-Gesture-1.1.1-amd64.deb` | 同一 [原始飞书下载页](https://roboparty.feishu.cn/docx/UDyrdMlzyoJ1YaxHlb8cwkFenXg)，约 309 MB，未镜像 |
| 厂商 Linux SDK | `RP_Hand_SDK-API-Linux-20260727.tar.gz` | [原始飞书](https://roboparty.feishu.cn/docx/RIKJdBaQYoDGRfx4yDwcmBcpnwf)，未镜像 |
| 厂商 Windows SDK | `RP_Hand_SDK-API-Windows-20260727.7z` | 同一 [原始飞书下载页](https://roboparty.feishu.cn/docx/RIKJdBaQYoDGRfx4yDwcmBcpnwf)，未镜像 |
| 厂商 ROS 示例 | `hand_control_ws_rp_hand.zip` | [原始飞书](https://roboparty.feishu.cn/docx/ZP7ldU3L9owd4BxRPXEcpclrnog)，Humble / EtherCAT 示例，未镜像 |

厂商原版 SDK/ROS 示例与 RoboParty CAN-FD 封装是不同软件路线。不要将原版 `.so` 随意覆盖到已安装的驱动目录，也不要将原版示例能力直接视为当前 ROS 包的能力。

## 模型与协议

| 资源 | 入口与状态 |
| --- | --- |
| DH116 / DH116S URDF、MJCF | [原始飞书](https://roboparty.feishu.cn/docx/E4pUdKUfWoplqHxbR9CcnNUfn4d)，两个 2026-04-09 版本归档，未镜像 |
| 左右手 X_T CAD | [产品手册附件](https://roboparty.feishu.cn/docx/SaoIdLjNeoOCVZxXzdIcqwLqnNb)，未镜像 |
| CAN-FD 协议正文 | [原始飞书](https://roboparty.feishu.cn/docx/NofXd7ZqKovElLxfgr8cWMegnxg)，revision 14 |
| EtherCAT / CAN-FD / RS485 协议表格 | [产品手册附件](https://roboparty.feishu.cn/docx/SaoIdLjNeoOCVZxXzdIcqwLqnNb)中的 xlsx，未镜像 |

尺寸与引脚图已经存入 [硬件手册](hardware.md)，不依赖飞书登录即可在本仓库查看。

## 后续 Release

转存大附件时使用明确的资料版本，每个文件记录硬件型号、平台/架构、原始版本、文件大小和实际计算的 SHA-256。上位机、厂商 SDK 和模型分别保留用途说明及适用许可。未取得文件前不填写校验值，也不把未发布附件列为“可下载”。
