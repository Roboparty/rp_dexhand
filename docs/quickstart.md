# 单手 CAN-FD 快速开始

[首页](../README.zh-CN.md) · [English](en/quickstart.md) · [硬件](hardware.md) · [兼容](compatibility.md)

本指南使用 [SDK `eb923ac`](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39) 的 `rphand` 接口。命令在目标 Linux 计算机的 Bash 中执行。先完成无硬件构建，再接入单手，最后扩展到双手或 ROS。

## 1. 准备与构建

需要 Linux、CMake ≥ 3.16、C++17 编译器及 Git。Python 另需 Python ≥ 3.9、对应开发头文件与 pybind11。Ubuntu 可安装：

```bash
sudo apt update
sudo apt install build-essential cmake git python3-dev pybind11-dev can-utils
```

```bash
git clone https://github.com/Roboparty/roboparty_dexhand.git
cd roboparty_dexhand
git checkout eb923acf61a02febabc9db90ad4d5eed84ffbc39
bash build.sh cpp
RPHAND_PYTHON=/usr/bin/python3 bash build.sh python
RPHAND_PYTHON=/usr/bin/python3 source setup_python.sh
/usr/bin/python3 -c 'from rphand import Hand; print(Hand)'
```

若 CMake 未找到 pybind11，按目标环境安装其 CMake 包；使用 pip 安装时可通过 `pybind11_DIR` 指向 `python3 -m pybind11 --cmakedir` 的输出。构建和运行使用同一解释器，切勿混用旧版扩展文件。

## 2. 无硬件检查

在 SDK 根目录执行：

```bash
cmake -S . -B build/check -DRPHAND_BUILD_SMOKE=ON -DRPHAND_BUILD_DEMO=ON
cmake --build build/check --parallel 2
ctest --test-dir build/check --output-on-failure
```

这些是 SDK 提供的模拟 / 离线测试；运行成功后再检查设备接线与通信，不据此判断实机运动已通过验收。

## 3. 接线与 CAN-FD

断电连接 VDC、GND、CANH、CANL，按[引脚图](hardware.md)辨认插头和插座视角。`can0`、节点 ID `1` 是示例，需与实际设备一致。总线和终端配置应符合整机接线方案。

```bash
ip -details -statistics link show can0
```

目标接口应为 UP、CAN-FD，参考部署采用仲裁段 1 Mbit/s、数据段 5 Mbit/s。仅在接口尚未配置、且已停止共享该接口的控制程序后配置：

```bash
sudo ip link set can0 down
sudo ip link set can0 type can bitrate 1000000 dbitrate 5000000 fd on
sudo ip link set can0 up
```

SDK 不创建系统接口或修改总线速率。当前 `connect()` 会配置并检查六轴的 20 ms 反馈周期；不再执行旧版 `roboparty-dexhand-config` 步骤。

## 4. 首次连接与状态读取

停止其他控制同一只手的程序。在新终端先进入 SDK 目录，加载 `setup_python.sh`：

```bash
RPHAND_PYTHON=/usr/bin/python3 source setup_python.sh
```

```python
from rphand import Hand

hand = Hand()
try:
    if not hand.connect("can0", 1):
        raise RuntimeError("Hand connection failed")
    state = hand.get_state()
    print("feedback_valid:", state.feedback_valid)
    print("positions:", state.positions)
    print("fault_codes:", state.fault_codes)
finally:
    hand.disconnect()
```

本例不主动使能或回零，但 `connect()` 会写入通信配置，并可能失能和恢复遗留软件急停；它不是只读查询。状态有效性必须与数组一起检查，详见 [SDK](sdk.md)。

## 5. 运动与双手接入

完成接口、机械范围和停止措施确认后，使用 SDK 的 [C++ / Python wave 示例](https://github.com/Roboparty/roboparty_dexhand/tree/eb923acf61a02febabc9db90ad4d5eed84ffbc39/examples)。它们会连接、配置、使能、回零并持续发送目标；拇指阶段包含全行程目标，不宜直接用于受限安装空间或带载首次调试。

正常运动流程为 `connect → disable → 配置 → enable → home → 位置控制 → stop / disable → disconnect`。逐步检查返回值、有效反馈和实际动作。`disconnect()` 只释放本地资源，不自动停止或失能。

双手推荐使用配套 [ROS 2 launch](ros2.md)。当前 SDK 不再依赖旧版进程级厂商回调；不要让多个进程同时控制同一个接口和节点 ID。

记录硬件/固件版本、左右手、接口、节点 ID、SDK commit、系统与 Python 版本，再记录连接、回零、运动、反馈和退出结果。本次文档更新没有进行实机运动验收。
