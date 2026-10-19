# C++ / Python SDK

[首页](../README.zh-CN.md) · [English](en/sdk.md) · [快速开始](quickstart.md) · [ROS 2](ros2.md)

当前指南对应 [roboparty_dexhand `eb923ac`](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39)。C++ 使用 `rphand::Hand`，Python 使用 `rphand.Hand`，协议处理直接从源码构建。旧版 `HandDriver`、`dexhand_py` 与厂商二进制封装见[迁移说明](compatibility.md)。

## API 与构建产物

| 入口 | 用途 |
| --- | --- |
| `<rphand/hand.hpp>` / `rphand::Hand` | C++ 设备连接、控制和状态快照 |
| `from rphand import Hand` | Python 绑定，共用 C++ 实现 |
| `rphand_ros` | 同仓库内的 Jazzy ROS 2 适配 |
| `bash build.sh cpp / python / ros` | 分别构建到 `install/cpp`、`install/python`、`install/ros` |

外部 CMake 项目在安装 SDK 后使用：

```cmake
find_package(rphand CONFIG REQUIRED)
add_executable(hand_app main.cpp)
target_link_libraries(hand_app PRIVATE rphand::rphand)
```

配置时把 `CMAKE_PREFIX_PATH` 指向 SDK 的 `install/cpp`。完整构建、安装和例程见[上游 API 文档](https://github.com/Roboparty/roboparty_dexhand/blob/eb923acf61a02febabc9db90ad4d5eed84ffbc39/docs/api.md)。

## 六轴顺序与单位

| 数组下标 | 单轴 ID | 软件通道 |
| --- | --- | --- |
| 0 | 1 | 拇指侧摆 |
| 1 | 2 | 拇指屈伸 |
| 2 | 3 | 食指 |
| 3 | 4 | 中指 |
| 4 | 5 | 无名指 |
| 5 | 6 | 小指 |

此顺序来自当前公共头文件与 API，尚不等于已标定的左右手 URDF 关节对应表。

| 数据 | 单位 / 范围 |
| --- | --- |
| 位置目标 | 绝对行程当量，`0..10000`；不是角度或弧度 |
| 速度设置 | 行程当量/秒；ROS 接口约束 `1..20000` |
| 电流限制 | 额定电流千分比，`0..3000`；不是 mA |
| 反馈电流 | 协议解码值；不能直接当作力或力矩 |
| 单轴 ID | `1..6`，当前单轴公共接口不接受广播 ID 0 |

## 控制流程

`connect → disable → 配置速度/电流/到位模式 → enable → home → 位置控制 → stop / disable → disconnect`

`set_positions()` 一次下发六轴目标，成功不代表已经到位；SDK 不做轨迹插值或周期重发。上层应用应检查返回值与设备反馈。`connect()` 会写通信配置，并可能恢复遗留急停，不是只读操作。位置 API 不提供完整的健康门控，应用需要自行确保初始化和状态条件。

Python 清理应分别调用并检查 `stop()`、`disable()`，再 `disconnect()`；不能因 stop 失败而跳过 disable。C++ 另有 `prepare_disconnect()`，停止、失能各最多尝试一次。断开和析构本身不发送停止指令。

## 状态反馈

`get_state()` 返回最新缓存快照：`positions`、`velocities`、`currents`、`enabled`、`homed`、`torque_reached`、`fault_codes` 均为六元素数组，另有 `feedback_valid`。

只有连接正常且位置组、状态组均已接收、各自年龄小于 100 ms 时，`feedback_valid` 才为 true。两组并非同时采样，过期后数组可能保留旧值。`is_connected()` 不代表反馈仍在更新。

ROS 发布对应状态，也提供采集入口，见 [ROS 2](ros2.md)。电流反馈采用协议值，使用时按设备定义解释。

线程、重试次数、并发约束和完整方法签名由[上游架构](https://github.com/Roboparty/roboparty_dexhand/blob/eb923acf61a02febabc9db90ad4d5eed84ffbc39/docs/architecture.md)与 [API](https://github.com/Roboparty/roboparty_dexhand/blob/eb923acf61a02febabc9db90ad4d5eed84ffbc39/docs/api.md)维护。本仓库仅维护产品集成说明。
