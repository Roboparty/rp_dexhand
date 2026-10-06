# 下载与可用状态

[返回首页](../README.zh-CN.md) · [SDK 选择](sdk.md) · [模型说明](models.md)

资料快照日期：2026-10-05。12 份飞书资料已归档至 [resources-2026.10.05](https://github.com/Roboparty/rp_dexhand/releases/tag/resources-2026.10.05)。原件合计 1,409,480,165 字节；CAD 无损压缩后，12 个下载文件合计 975,103,906 字节（约 975.10 MB）。这是资料预发布版，不是新版 SDK，也不代表实机验收通过。

本仓库及 Release 当前为私有，需要具有仓库访问权限的 GitHub 账号；未登录或无权限时可能返回 404。原始飞书链接仍需要对应的飞书权限。软件和模型保持原包，部分下载文件名改为 ASCII；CAD 使用 XZ 无损压缩，已核对解压后与飞书原件的 SHA-256 一致。

## RoboParty 维护的驱动

| 资源 | 版本/架构 | 下载入口 |
| --- | --- | --- |
| Linux Debian 包 | v0.5.0 / amd64 | [roboparty-dexhand_0.5.0-1_amd64.deb](https://github.com/Roboparty/roboparty_dexhand/releases/download/v0.5.0/roboparty-dexhand_0.5.0-1_amd64.deb) |
| Linux Debian 包 | v0.5.0 / arm64 | [roboparty-dexhand_0.5.0-1_arm64.deb](https://github.com/Roboparty/roboparty_dexhand/releases/download/v0.5.0/roboparty-dexhand_0.5.0-1_arm64.deb) |
| SDK 源码与其他 Release | 以选定 tag 为准 | [源码](https://github.com/Roboparty/roboparty_dexhand) · [Release 列表](https://github.com/Roboparty/roboparty_dexhand/releases) |
| ROS 适配包源码 | 兼容性见 [ROS 指南](ros2.md) | [roboparty_dexhand_ros](https://github.com/Roboparty/roboparty_dexhand_ros) |

这些 deb 是已确认存在的上游发布资产。本次没有安装运行或计算它们的校验值，不声明跨系统/Python ABI 兼容。安装前确认目标环境，并获取匹配的 `roboparty-base`；已有配套镜像的用户通常不需要重复安装。

## 厂商软件与配套应用

| 资源 | 版本 / 大小（十进制 MB） | Release 下载 |
| --- | --- | --- |
| Windows 上位机 | 1.4.0 / 2026-08-25 / 205.57 MB | [ZIP](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand-v1.4.0-2026-08-25.zip) |
| 上位机原始更新日志 | 来源文档 revision 6 / 0.07 MB | [TXT](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_Host_changelog.txt) |
| 手势软件 Windows | 1.1.1 / 299.84 MB | [EXE](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP-Hand-Gesture-Setup-1.1.1.exe) |
| 手势软件 Linux amd64 | 1.1.1 / 309.22 MB | [DEB](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP-Hand-Gesture-1.1.1-amd64.deb) |
| 厂商 Linux SDK | 2026-07-27 / 13.43 MB | [tar.gz](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_SDK-API-Linux-20260727.tar.gz) |
| 厂商 Windows SDK | 2026-07-27 / 7.63 MB | [7z](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_SDK-API-Windows-20260727.7z) |
| 厂商 ROS 示例 | Humble / EtherCAT；来源文档 revision 4 / 33.35 MB | [ZIP](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/hand_control_ws_rp_hand.zip) |

原始来源：[上位机](https://roboparty.feishu.cn/docx/VnbPdcs9toG7a1xe9l2cwVujnOe)、[手势软件](https://roboparty.feishu.cn/docx/UDyrdMlzyoJ1YaxHlb8cwkFenXg)、[厂商 SDK](https://roboparty.feishu.cn/docx/RIKJdBaQYoDGRfx4yDwcmBcpnwf)、[ROS 示例](https://roboparty.feishu.cn/docx/ZP7ldU3L9owd4BxRPXEcpclrnog)。Linux 原版 SDK 归档中包含 `aarch64`、`i386`、`x86_64` 目录；目录存在不代表在目标系统上已测试。

厂商原版 SDK/ROS 示例与 RoboParty CAN-FD 封装是不同软件路线。不要将原版 `.so` 随意覆盖到已安装的驱动目录，也不要将原版示例能力直接视为当前 ROS 包的能力。

## 模型与协议

| 资源 | 版本 / 大小（十进制 MB） | Release 下载 |
| --- | --- | --- |
| DH116 URDF / MJCF，左右手 | 2026-04-09 / 7.22 MB | [7z](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116_URDF_MJCF_Files_2026_4_9.7z) |
| DH116S URDF / MJCF，左右手 | 2026-04-09 / 9.56 MB | [7z](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116S_URDF_MJCF_Files_2026_4_9.7z) |
| DH116S 左手白色 CAD | L000-A1 / A / 45.29 MB（解压后 260.96 MB） | [X_T.xz](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116S-L000-A1_RP_Left_White_A.x_t.xz) |
| DH116S 右手白色 CAD | R000-A1 / A / 43.56 MB（解压后 262.26 MB） | [X_T.xz](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/DH116S-R000-A1_RP_Right_White_A.x_t.xz) |
| EtherCAT / CAN-FD / RS485 协议表格 | 来源手册 revision 13 / 0.37 MB | [XLSX](https://github.com/Roboparty/rp_dexhand/releases/download/resources-2026.10.05/RP_Hand_Protocols_EtherCAT_CAN-FD_RS485.xlsx) |

原始来源：[模型下载页](https://roboparty.feishu.cn/docx/E4pUdKUfWoplqHxbR9CcnNUfn4d)、[产品手册附件](https://roboparty.feishu.cn/docx/SaoIdLjNeoOCVZxXzdIcqwLqnNb)。[在线 CAN-FD 协议](https://roboparty.feishu.cn/docx/NofXd7ZqKovElLxfgr8cWMegnxg)为 revision 14；不能仅凭文档 revision 比较它与附件表格的协议版本。

尺寸与引脚图已经存入 [硬件手册](hardware.md)，不依赖飞书登录即可在本仓库查看。

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

将输出的完整哈希与校验表中同名记录比较。校验值用于确认字节一致性，不替代来源身份、签名或安全性检查。

CAD 下载后先核对压缩包哈希，再解压。例如 Linux 下保留压缩包并恢复左手原始文件：

```bash
xz -dk DH116S-L000-A1_RP_Left_White_A.x_t.xz
sha256sum DH116S-L000-A1_RP_Left_White_A.x_t
```

解压后哈希与清单中的 `original_sha256` 比较，原始大小见 `original_size_bytes`。右手同理；Windows 可用支持 XZ 的解压工具。

本次完成了 ZIP/7z/gzip 完整性检查、XZ 解压还原哈希检查和 Debian 包元数据/内容列表检查。EXE 与 X_T 内容仅核对文件类型及头部，没有执行安装程序、加载 CAD 几何、运行仿真或驱动实机。公开再分发范围仍需按 [第三方说明](../NOTICE.md) 确认。
