# URDF、MJCF 与 CAD

[首页](../README.zh-CN.md) · [English](en/models.md) · [下载](downloads.md)

## 资源选择

| 资源 | 版本 | 用途 |
| --- | --- | --- |
| DH116 URDF / MJCF | 2026-04-09，左右手归档 | 该型号的机器人模型 |
| DH116S URDF / MJCF | 2026-04-09，左右手归档 | 包含独立关节与 mimic 联动定义 |
| DH116S 左 / 右手 CAD | L000-A1 / R000-A1，白色，修订 A | 安装空间与结构适配；X_T 无损 XZ 压缩 |

从[版本化资源](https://github.com/Roboparty/rp_dexhand/releases/tag/resources-2026.10.05)下载，先核对 SHA-256 再解压。CAD 解压后的原件哈希另见资源清单，不能与 XZ 包哈希混用。DH116 与 DH116S 应按交付型号选择。

## DH116S 模型结构

DH116S 左右手模型分别包含以下结构：

| 项目 | 每只手 |
| --- | --- |
| URDF link | 17 |
| 可动关节 | 11 |
| 独立关节 | 6 |
| mimic 联动关节 | 5 |
| 固定关节 | 5 |
| URDF mesh 引用 | 34，均可解析到归档内文件 |
| MJCF mesh 引用 | 17，均可解析到归档内文件 |

独立关节名称为 `finger11`、`finger12`、`finger21`、`finger31`、`finger41`、`finger51`。关节树、mimic 和资源引用详情见[模型结构记录](../resources/model-inspection-2026.10.19.json)。

URDF 使用 `package://DH116S-L000-A1/...` 或右手对应包路径；应让资源解析器能找到相应包和 meshes。MJCF 的相对 meshdir 需保持原始目录关系，不能只移动单个 XML。

## 接到真实设备前

| 层级 | 已明确 | 仍需核对 |
| --- | --- | --- |
| SDK | 六轴顺序与通道名称见 SDK 指南 | 交付固件是否使用相同定义 |
| URDF | 六独立关节、五 mimic 及几何引用 | 左右手物理轴对应、零位、正方向与行程比例 |
| 运行时 | 当前 ROS 发布设备 state | 弧度转换、joint_states 和可视化适配 |

接入实机时，先标定各轴零位、方向和行程到弧度的转换。URDF 中部分 effort/velocity 为 0，输出限制应按实际设备参数设置；模型角度限位与 SDK 的 0..10000 行程目标需要分别处理。

CAD 使用原始 X_T 格式。导入设计软件后，结合对应版本的工程图检查腕部安装尺寸与装配间隙。
