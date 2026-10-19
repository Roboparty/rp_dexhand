# 资料来源与维护

[首页](../README.zh-CN.md) · [下载](downloads.md) · [版本兼容](compatibility.md)

## 版本与资源

| 内容 | 版本 / 入口 |
| --- | --- |
| SDK 与配套 ROS | [eb923ac](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39) |
| 软件、模型及协议文件 | [resources-2026.10.05](https://github.com/Roboparty/rp_dexhand/releases/tag/resources-2026.10.05) |
| 原始文件名、大小及 SHA-256 | [manifest.json](../resources/resources-2026.10.05/manifest.json) |
| 下载文件校验值 | [SHA256SUMS.txt](../resources/resources-2026.10.05/SHA256SUMS.txt) |
| 资源格式检查 | [validation.json](../resources/resources-2026.10.05/validation.json) |
| DH116S 模型结构与资源引用 | [模型记录](../resources/model-inspection-2026.10.19.json) |

软件接入使用上表中的 SDK 版本。下面的来源表记录产品资料与配套应用的原始版本，其中旧 SDK 和 ROS 条目供已有系统维护时查阅。

## 产品资料来源

| 来源 | 版本 | 使用位置 |
| --- | --- | --- |
| [RP Hand 用户手册](https://roboparty.feishu.cn/docx/SaoIdLjNeoOCVZxXzdIcqwLqnNb) | revision 13 | 产品参数、硬件说明、尺寸图、引脚图 |
| [SDK 下载页](https://roboparty.feishu.cn/docx/RIKJdBaQYoDGRfx4yDwcmBcpnwf) | revision 9 | 原版包名和版本 |
| [ROS 示例下载页](https://roboparty.feishu.cn/docx/ZP7ldU3L9owd4BxRPXEcpclrnog) | revision 4 | 原版 ROS 资源 |
| [ROS 示例说明](https://roboparty.feishu.cn/docx/F1fydcBSKo2H4jxjtyDccqUwnnc) | revision 1 | 原版 Humble/EtherCAT 路线识别 |
| [模型下载页](https://roboparty.feishu.cn/docx/E4pUdKUfWoplqHxbR9CcnNUfn4d) | revision 7 | DH116/DH116S 归档信息 |
| [上位机下载页](https://roboparty.feishu.cn/docx/VnbPdcs9toG7a1xe9l2cwVujnOe) | revision 6 | 软件包名和版本 |
| [手势软件下载页](https://roboparty.feishu.cn/docx/UDyrdMlzyoJ1YaxHlb8cwkFenXg) | revision 67 | Windows/Linux 包名和版本 |
| [CAN-FD 协议](https://roboparty.feishu.cn/docx/NofXd7ZqKovElLxfgr8cWMegnxg) | revision 14，相关章节 | 行程单位及通信说明 |
| [SDK](https://github.com/Roboparty/roboparty_dexhand/tree/046108e7ba800763a096ca1c99b04a8414797105) | `046108e` | 软件支持范围、API、安装和验收入口 |
| [ROS 包](https://github.com/Roboparty/roboparty_dexhand_ros/tree/bfc325f2d5d7bf33d3a64ebdc79b01ed3641f227) | `bfc325f` | 集成状态与限制 |
| [公司首页](https://github.com/Roboparty/rptest_repo/tree/f1ca45288a61985d2372cbe38d767869d818eb8d) | `f1ca452` | `assets/readme/rp1-hand.gif` 产品动图 |

## 图片来源

| 文件 | 来源 |
| --- | --- |
| `assets/dimensions.png` | RP Hand 用户手册尺寸图 |
| `assets/pinout.png` | RP Hand 用户手册引脚图 |
| `assets/rp-hand.gif` | RoboParty 项目页面安装动图 |

图片校验值见 [assets/SHA256SUMS.txt](../assets/SHA256SUMS.txt)。

## 更新文档

1. 更新产品参数或接口时，注明对应硬件、固件和软件版本。
2. 同步修改中英文指南；新旧 API 的区别写入版本兼容页。
3. 大型软件包与 CAD 按版本发布至 Release，并更新文件清单与校验值。
4. 新增资源检查记录，保留已发布版本的原始清单。
5. 按 [CONTRIBUTING.md](../CONTRIBUTING.md) 运行文档检查并提交 PR。
