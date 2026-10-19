# 常见问题

[首页](../README.zh-CN.md) · [English](en/troubleshooting.md) · [快速开始](quickstart.md)

| 现象 | 检查方法 |
| --- | --- |
| `ModuleNotFoundError: rphand` | 在 SDK 根目录加载 `setup_python.sh`，确认 Python 与构建解释器相同 |
| 只有 `dexhand_py` / `HandDriver` | 当前加载的是旧版驱动，先阅读版本兼容，勿混用 API |
| CMake 找不到 pybind11 | 安装目标环境的 pybind11 CMake 包，或配置 `pybind11_DIR` |
| 原生扩展导入失败 | 检查 Python ABI、目标架构及依赖；在目标系统重新构建 |
| `can0` 不存在 / 不为 FD | 检查适配器和系统驱动；SDK 不创建接口或配置总线速率 |
| `connect()` 失败 | 检查供电、接线、1/5 Mbit/s、节点 ID、反馈及其他设备控制进程 |
| ROS 启动后没有动作 | 当前节点等待 reset；启动不主动连接或回零 |
| reset 返回成功但还不能运动 | true 仅表示受理；等待完成日志并核对新鲜反馈和故障状态 |
| state 有旧数值但手已掉线 | 检查 `feedback_valid` 及消息新鲜度，缓存不代表实时反馈 |
| 找不到 `/joint_states` | 当前使用自定义 state，模型转换需要另行建立映射 |
| 全零目标未停止 / 未重新回零 | 全零是位置目标，不是 stop、disable 或 home |
| 停止命令发布后手仍执行 | 节点继续发送缓存目标；按运行指南执行退出清理并确认实际状态 |
| 原始飞书附件打不开 | 优先使用 GitHub 版本化资源；飞书仍需单独权限 |

## 收集诊断信息

```bash
uname -m
/usr/bin/python3 --version
git -C /path/to/roboparty_dexhand rev-parse HEAD
ip -details -statistics link show can0
/usr/bin/python3 -c 'import rphand; print(rphand.__file__)'
```

将路径与接口名换成实际配置。提交硬件/固件、左右手、接口与 ID、系统/ROS/Python、SDK commit、初始化步骤和日志。不要在 Issue 中附带访问 token 或其他凭据。产品文档问题在本仓库反馈；运行时代码问题到 SDK 仓库反馈，具体见贡献指南。
