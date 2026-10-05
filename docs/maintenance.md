# 资料来源与维护

[返回首页](../README.zh-CN.md)

## 当前基线

整理日期：2026-10-05。仓库名称为 `rp_dexhand`，产品名称为 RP Hand，维护的 SDK 为 `roboparty_dexhand`。本版建立资料入口；大型软件/模型镜像、关节映射和完整 ROS 组合验收仍有后续工作。

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

原始飞书页面和公司首页仓库可能要求访问权限；本仓库内的硬件图示与正文不依赖远端图片 token 渲染。

## 素材对应

| 本地文件 | 来源 |
| --- | --- |
| `assets/dimensions.png` | 用户手册图片 `IJRgbzn0PotT42x6EyHcbG7Qn9e`，保持原始内容 |
| `assets/pinout.png` | 用户手册图片 `NPObb1VGQo1CpZxsHzScTKBwnVe`，保持原始内容 |
| `assets/rp-hand.gif` | 公司首页 `assets/readme/rp1-hand.gif`，保持原始内容 |

仓库内三份素材的校验值见 [SHA256SUMS.txt](../assets/SHA256SUMS.txt)。在仓库根目录执行 `sha256sum -c assets/SHA256SUMS.txt` 可核验文件完整性。

## 更新流程

1. 在飞书完成产品内容核对，记录文档 revision 和附件版本。
2. 将确认后的正文整理到对应 Markdown，图片下载到 `assets/`，大附件按版本进入 Release。
3. 检查本地链接、图片、代码示例语法；涉及设备行为时记录实际软硬件组合和验收结果。
4. 使用 PR 审阅变更，再更新下载表与中英文首页。SDK API 的修改回到 SDK 仓库维护。

不把飞书文档 token 当作公开下载链接；不在本仓库存储访问凭据。下载状态以实际发布结果为准。

## 下一阶段

- 确认公开发布的资料范围和仓库可见性，并补齐适用的文档/素材许可声明。
- 核验六主动轴、左右手、DH116/DH116S 与模型的对应关系。
- 确定发布的镜像/SDK/ROS 组合，修正上游安装入口与回零行为差异。
- 将确认发布的软件和模型转为版本化 Release，计算并提供校验值。
- 补全详细英文手册，依据实际测试记录更新兼容状态。

本版没有进行真实硬件运动测试，不以文档检查代替设备验收。
