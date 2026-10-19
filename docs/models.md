# URDF、MJCF 与 CAD

[首页](../README.zh-CN.md) · [English](en/models.md) · [下载](downloads.md)

## 资源选择

| 资源 | 版本 | 用途 |
| --- | --- | --- |
| DH116 URDF / MJCF | 2026-04-09，左右手归档 | 该型号的机器人模型 |
| DH116S URDF / MJCF | 2026-04-09，左右手归档 | 该型号的机器人模型；本次完成静态检查 |
| DH116S 左 / 右手 CAD | L000-A1 / R000-A1，白色，修订 A | 安装空间与结构适配；X_T 无损 XZ 压缩 |

从[版本化资源](https://github.com/Roboparty/rp_dexhand/releases/tag/resources-2026.10.05)下载，先核对 SHA-256 再解压。CAD 解压后的原件哈希另见资源清单，不能与 XZ 包哈希混用。DH116 与 DH116S 应按交付型号选择。

## DH116S 静态检查

2026-10-19 下载原始 DH116S 模型包，确认包哈希与原始清单一致后解析 XML。左右手分别包含：

| 项目 | 每只手 |
| --- | --- |
| URDF link | 17 |
| 可动关节 | 11 |
| 独立关节 | 6 |
| mimic 联动关节 | 5 |
| 固定关节 | 5 |
| URDF mesh 引用 | 34，均可解析到归档内文件 |
| MJCF mesh 引用 | 17，均可解析到归档内文件 |

独立关节名称为 `finger11`、`finger12`、`finger21`、`finger31`、`finger41`、`finger51`。关节树和 mimic 源引用检查通过，完整记录见[模型检查报告](../resources/model-inspection-2026.10.19.json)。DH116 此次未重复检查。

URDF 使用 `package://DH116S-L000-A1/...` 或右手对应包路径；应让资源解析器能找到相应包和 meshes。MJCF 的相对 meshdir 需保持原始目录关系，不能只移动单个 XML。

## 接到真实设备前

| 层级 | 已明确 | 仍需核对 |
| --- | --- | --- |
| SDK | 六轴顺序与通道名称见 SDK 指南 | 交付固件是否使用相同定义 |
| URDF | 六独立关节、五 mimic 及几何引用 | 左右手物理轴对应、零位、正方向与行程比例 |
| 运行时 | 当前 ROS 发布设备 state | 弧度转换、joint_states 和可视化适配 |

静态文件检查不代表完成仿真加载、动力学验证或实机标定。URDF 中部分 effort/velocity 为 0，不能作为设备输出能力参数。模型限位也不自动等于手册行程或 SDK 的 0..10000 目标范围。

CAD 原件尚未在 CAD 软件中加载验收；本仓库保留原始文件，不替换其质量、惯量、关节限位或联动参数。
