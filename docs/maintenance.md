# 资料来源与维护

[返回首页](../README.zh-CN.md)

## 当前基线

资料快照日期：2026-10-05。仓库名称为 `rp_dexhand`，产品名称为 RP Hand，维护的 SDK 为 `roboparty_dexhand`。资料入口和 12 个原始附件的版本化归档已完成；实机轴映射、适用许可和完整硬件验收仍需维护。当前公开状态与源码基线见下节。

## 2026-10-19 更新

- 仓库和资源 Release 页面当前公开可访问；保留创建时的 manifest、SHA256SUMS 和 validation，不改写历史事实。
- 推荐源码切换为 [SDK `eb923ac`](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39)：`rphand::Hand`、`rphand.Hand` 及同仓库内 `rphand_ros`。
- 根据公共头文件、Python 类型声明、ROS 消息、launch 与 API 文档核对轴顺序、单位、反馈有效性和运行行为。
- 下载 DH116S 模型归档并核对原始哈希，解析左右手 URDF/MJCF，检查关节树、mimic 和 mesh 文件引用；结果见[静态检查记录](../resources/model-inspection-2026.10.19.json)。
- 不声明本次在 Linux/Jazzy 上构建运行或完成真实设备动作验收。

以下来源表记录 2026-10-05 资料快照；其中 SDK/旧 ROS 行已由当前源码路线替代，仍保留作来源追溯。

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

## 资源归档

[resources-2026.10.05](https://github.com/Roboparty/rp_dexhand/releases/tag/resources-2026.10.05) 是创建时为私有的资料预发布版，对应 12 个飞书原件，原始合计 1,409,480,165 字节。2026-10-06 将尚未发布的左右手 CAD 无损封装为 XZ，下载文件合计缩减到 975,103,906 字节。该标签表示资料快照日期，不覆盖各附件的独立版本。已逐项核对原件大小；清单同时记录 CAD 压缩包与原件的大小和 SHA-256，并验证解压后字节一致。

Git 中的 [manifest.json](../resources/resources-2026.10.05/manifest.json)、[SHA256SUMS.txt](../resources/resources-2026.10.05/SHA256SUMS.txt) 和 [validation.json](../resources/resources-2026.10.05/validation.json) 与 Release 同名附件一致。大文件不进入 Git 历史，旧 SDK v0.5.0 二进制仍由 SDK 仓库历史 Release 维护。

后续资料更新创建新快照，不覆盖已发布附件；同步更新来源 revision、文件大小、哈希和检查记录。解压与格式检查不代表软件安全性、目标系统兼容性或真实硬件动作验收。

## 更新流程

1. 在飞书完成产品内容核对，记录文档 revision 和附件版本。
2. 将确认后的正文整理到对应 Markdown，图片下载到 `assets/`，大附件按版本进入 Release。
3. 检查本地链接、图片、代码示例语法；涉及设备行为时记录实际软硬件组合和验收结果。
4. 使用 PR 审阅变更，再更新下载表与中英文首页。SDK API 的修改回到 SDK 仓库维护。

不把飞书文档 token 当作公开下载链接；不在本仓库存储访问凭据。下载状态以实际发布结果为准。

## 下一阶段

- 由权利人确认文档、模型和归档软件的适用许可；公开状态与许可库存分开维护。
- 核验六主动轴、左右手、DH116/DH116S 与模型的对应关系。
- 在目标 Linux/Jazzy 与交付固件上运行当前 SDK，记录连接、回零、运动和状态时序验收。
- 维护后续资源快照，确认新版本适用范围后更新清单与校验值。
- 保持中英文指南一致，依据实际测试记录更新兼容矩阵。

本版没有进行真实硬件运动测试，不以文档检查代替设备验收。
