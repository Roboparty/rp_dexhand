# 上位机与手势识别软件

[首页](../README.zh-CN.md) · [English](en/software.md) · [下载](downloads.md)

RP Hand 提供上位机和手势识别 Demo，可用于设备调试与视觉手势演示。开发自定义控制程序时，可使用 C++ / Python SDK 或 ROS 2 接口。

| 应用 | 资源版本 | 平台与用途 |
| --- | --- | --- |
| RP Hand 上位机 | 1.4.0，2026-08-25 | Windows；设备调试与参数配置 |
| RP Hand Gesture | 1.1.1 | Windows EXE / Linux amd64 DEB；视觉手势识别演示 |
| 当前 rphand SDK | 源码基线 eb923ac | Linux；C++ / Python / 配套 Jazzy ROS 开发 |

从[下载页](downloads.md)获取软件包与更新日志，并按包内说明配置设备固件、通信接口、系统依赖和相机。

视觉识别与动作映射由操作端程序完成，机器人端 SDK / ROS 节点负责接收目标并执行手部控制。将自定义手势程序接入机器人时，按[六轴顺序和单位](sdk.md)输出控制目标。

需要控制自己的程序时，从[快速开始](quickstart.md)进入。需要录制已发布的手部 state/action 时，使用 [ROS 数据记录](ros2.md)。
