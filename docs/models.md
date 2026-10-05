# URDF、MJCF 与 CAD

[返回首页](../README.zh-CN.md) · [硬件尺寸](hardware.md) · [下载清单](downloads.md)

## 现有资源

| 资源 | 来源版本 | 当前状态 |
| --- | --- | --- |
| DH116 URDF / MJCF | `DH116_URDF_MJCF_Files_2026_4_9.7z` | 已归档；7z 完整性检查通过 |
| DH116S URDF / MJCF | `DH116S_URDF_MJCF_Files_2026_4_9.7z` | 已归档；7z 完整性检查通过 |
| 左手 CAD | `DH116S-L000-A1-结构件 RP左手DH116S-LW1-RP1套装  白色_A.x_t` | 已归档，260,959,468 字节；只检查头部和哈希 |
| 右手 CAD | `DH116S-R000-A1-结构件 RP右手DH116S-RW1-RP1套装  白色_A.x_t` | 已归档，262,261,691 字节；只检查头部和哈希 |

[私有资源 Release](https://github.com/Roboparty/rp_dexhand/releases/tag/resources-2026.10.05) 需要本仓库的 GitHub 访问权限，具体下载与校验方式见 [下载清单](downloads.md)。[原始 URDF/MJCF 下载页](https://roboparty.feishu.cn/docx/E4pUdKUfWoplqHxbR9CcnNUfn4d) 与 [产品手册中的 CAD 附件](https://roboparty.feishu.cn/docx/SaoIdLjNeoOCVZxXzdIcqwLqnNb) 仍保留作来源记录。

两个模型归档均包含对应型号的 `L000-A1`、`R000-A1` 目录；每侧有 `urdf/*.urdf`、`mjcf/*.xml` 和 mesh。完整路径记录在 [检查报告](../resources/resources-2026.10.05/validation.json)。目前只验证归档完整性并列出目录，尚未验证 mesh 引用、仿真加载或实际关节映射。

DH116 和 DH116S 不是可无条件互换的文件名。当前 RoboParty SDK 公共模型 0 内部映射到 Dof6S，但这不能替代对实际交付硬件和模型版本的核对。

## 映射要求

将模型接到实机前，需要逐轴确认以下信息：

| 字段 | 要记录的内容 |
| --- | --- |
| SDK 主动轴 | ID 1～6 |
| 物理含义 | 对应手指、侧摆或屈伸动作 |
| 左右手 | 模型侧别、方向与安装坐标系 |
| 模型关节 | URDF/MJCF 中的实际 joint 名称 |
| 零位与正方向 | SDK 零位与模型零位的对应关系 |
| 单位和范围 | 设备位置值/角度到模型弧度的转换、各轴限位 |
| 被动/联动关节 | 五个额外自由度的耦合关系或 mimic 定义 |

目前尚未发布经过核验的对应表。不能按名字猜测 joint 顺序，或把六个输入值直接填入模型全部 11 个关节；也不能把通用行程系数当作所有轴相同的角度换算。

## 后续文件组织

大型 CAD 和模型原始归档已经采用版本化 Release，Git 中只保留文档、清单和校验值。模型文本和配套 mesh 在核对引用路径及适用版本后再决定是否直接放入 Git。

当前运行时建议仍以 [SDK 单手验收](quickstart.md) 为基础；模型可视化不替代实际设备的状态反馈。
