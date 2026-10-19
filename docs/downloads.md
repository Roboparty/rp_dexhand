# 软件与模型下载

[返回首页](../README.zh-CN.md) · [English](en/downloads.md) · [SDK 选择](sdk.md) · [模型说明](models.md)

配套软件、机器人模型和协议文件统一发布在 [resources-2026.10.05](https://github.com/Roboparty/rp_dexhand/releases/tag/resources-2026.10.05)。按下表选择版本，下载后可使用 SHA-256 校验文件完整性。

## 当前推荐 SDK

| 入口 | 内容 |
| --- | --- |
| [源码基线 `eb923ac`](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39) | 当前 `rphand` C++ / Python SDK 与配套 Jazzy ROS 包 |
| [快速开始](quickstart.md) | 目标 Linux 环境源码构建与单手连接 |
| [版本兼容](compatibility.md) | 新旧 API 与环境区别 |

新项目按[快速开始](quickstart.md)构建 `rphand`。使用旧版 `dexhand_py` 的系统可在 [v0.5.0 Release](https://github.com/Roboparty/roboparty_dexhand/releases/tag/v0.5.0) 获取对应软件包，升级步骤见[版本兼容](compatibility.md)。

## 配套应用与原版 SDK

| 资源 | 版本 / 大小（十进制 MB） | Release 下载 |
| --- | --- | --- |
| Windows 上位机 | 1.4.0 / 2026-08-25 / 205.57 MB | [ZIP](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand-v1.4.0-2026-08-25.zip) |
| 上位机原始更新日志 | 来源文档 revision 6 / 0.07 MB | [TXT](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_Host_changelog.txt) |
| 手势软件 Windows | 1.1.1 / 299.84 MB | [EXE](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP-Hand-Gesture-Setup-1.1.1.exe) |
| 手势软件 Linux amd64 | 1.1.1 / 309.22 MB | [DEB](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP-Hand-Gesture-1.1.1-amd64.deb) |
| 原版 Linux SDK | 2026-07-27 / 13.43 MB | [tar.gz](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_SDK-API-Linux-20260727.tar.gz) |
| 原版 Windows SDK | 2026-07-27 / 7.63 MB | [7z](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_SDK-API-Windows-20260727.7z) |
| 原版 ROS 示例 | Humble / EtherCAT；来源文档 revision 4 / 33.35 MB | [ZIP](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/hand_control_ws_rp_hand.zip) |

上位机、手势软件和原版 SDK 按各自软件包内的说明安装。机器人程序开发使用上方的 `rphand` 源码入口；原版 EtherCAT 示例单独提供。

## 模型与协议

| 资源 | 版本 / 大小（十进制 MB） | Release 下载 |
| --- | --- | --- |
| DH116 URDF / MJCF，左右手 | 2026-04-09 / 7.22 MB | [7z](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116_URDF_MJCF_Files_2026_4_9.7z) |
| DH116S URDF / MJCF，左右手 | 2026-04-09 / 9.56 MB | [7z](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116S_URDF_MJCF_Files_2026_4_9.7z) |
| DH116S 左手白色 CAD | L000-A1 / A / 45.29 MB（解压后 260.96 MB） | [X_T.xz](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116S-L000-A1_RP_Left_White_A.x_t.xz) |
| DH116S 右手白色 CAD | R000-A1 / A / 43.56 MB（解压后 262.26 MB） | [X_T.xz](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116S-R000-A1_RP_Right_White_A.x_t.xz) |
| EtherCAT / CAN-FD / RS485 协议表格 | 来源手册 revision 13 / 0.37 MB | [XLSX](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_Protocols_EtherCAT_CAN-FD_RS485.xlsx) |

安装尺寸与接线见[硬件手册](hardware.md)，模型选择与关节说明见[模型文档](models.md)。

## 清单与完整性校验

- [完整清单](../resources/resources-2026.10.05/manifest.json)：原始名称、版本、适用型号/平台、来源文档与 revision、精确字节数、SHA-256。
- [SHA256SUMS.txt](../resources/resources-2026.10.05/SHA256SUMS.txt)：12 个下载文件的完整校验值（CAD 对应压缩包）；Release 中有同名副本。
- [检查记录](../resources/resources-2026.10.05/validation.json)：逐文件结果和验证边界。

下载全部 12 个附件和 `SHA256SUMS.txt` 到同一目录后，在该目录运行：

```bash
sha256sum -c SHA256SUMS.txt
```

只下载一个附件时，例如模型包，在文件所在目录运行：

```bash
sha256sum DH116S_URDF_MJCF_Files_2026_4_9.7z
```

将输出的完整哈希与校验表中同名记录比较。

CAD 下载后先核对压缩包哈希，再解压。例如 Linux 下保留压缩包并恢复左手原始文件：

```bash
xz -dk DH116S-L000-A1_RP_Left_White_A.x_t.xz
sha256sum DH116S-L000-A1_RP_Left_White_A.x_t
```

解压后哈希与清单中的 `original_sha256` 比较，原始大小见 `original_size_bytes`。右手同理；Windows 可用支持 XZ 的解压工具。

资源版本、原始文件名及来源见[维护记录](maintenance.md)与[完整清单](../resources/resources-2026.10.05/manifest.json)。
