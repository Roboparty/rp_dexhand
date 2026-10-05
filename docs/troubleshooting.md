# 常见问题

[返回首页](../README.zh-CN.md) · [快速开始](quickstart.md)

| 现象 | 检查方法 |
| --- | --- |
| `/opt/roboparty/setup.bash` 不存在 | 检查镜像是否包含 `roboparty-base`；源码安装使用 SDK 构建文档中的路径设置 |
| `ModuleNotFoundError: dexhand_py` | 在当前终端加载对应环境，使用匹配的系统 Python，检查实际安装路径 |
| 导入 `.so` 失败 | 核对 CPU 架构、Python ABI 和完整依赖；不要混用源码与镜像中的扩展 |
| `can0` 不存在 | 用 `ip -brief link` 查看实际接口，检查适配器、接线和 Linux 驱动 |
| 无法通信或反馈超时 | 检查供电、CAN-FD 1 Mbps/5 Mbps、node ID、反馈配置及其他控制进程 |
| 参数断电后失效 | 检查配置时是否使用 `--save`，并在手本体断电后重新执行 `show` |
| 回零失败 | 查看新鲜位置/状态反馈和报警；不要绕过回零继续运动 |
| 在一个进程中打开第二只手失败 | 厂商回调资源为进程级，使用一手一进程 |
| 初始化通信成功但手不动 | `init_hand(False, False, 0.0)` 不会使能；运动阶段需要独立的明确使能和回零流程 |
| 已初始化后改变 init 参数失败 | 先 `deinit_hand()` 再重新创建/初始化；不能把重复 init 当作状态切换 |
| ROS 找不到 `configure_feedback` | 当前被核对的 ROS 包没有该入口，使用 SDK 的 `roboparty-dexhand-config` |
| ROS 没有 `/joint_states` | 当前 CAN-FD ROS 包尚未实现发布，不能套用厂商 EtherCAT 示例的说明 |
| 飞书附件打不开 | 原始资料需要访问权限；查看下载页是否已经有 GitHub 镜像，不要把权限问题当作驱动故障 |

## 收集诊断信息

以下命令不发送运动命令：

```bash
uname -m
/usr/bin/python3 --version
dpkg-query -W roboparty-dexhand roboparty-base
ip -details -statistics link show can0
/usr/bin/python3 -c 'import dexhand_py; print(dexhand_py.__file__)'
```

最后一条命令需先加载对应软件环境。将 `can0` 替换为目标接口，记录硬件型号/左右手、固件、驱动版本、系统镜像、node ID、执行步骤及完整错误信息。

getter 读数是缓存，不能仅凭“读数为零”判断设备不在线，也不能仅凭“有读数”判断反馈仍在更新。软件故障、通信异常与机械运动结果需要分别核对。
