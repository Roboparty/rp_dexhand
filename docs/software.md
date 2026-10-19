# 上位机与手势识别软件

[首页](../README.zh-CN.md) · [English](en/software.md) · [下载](downloads.md)

配套应用可用于设备调试和演示；开发自己的机器人程序时，使用当前 C++ / Python SDK 或 ROS 2 接口。两类软件分别维护，不共享安装步骤。

| 应用 | 资源版本 | 平台与用途 |
| --- | --- | --- |
| RP Hand 上位机 | 1.4.0，2026-08-25 | Windows；设备调试与参数配置 |
| RP Hand Gesture | 1.1.1 | Windows EXE / Linux amd64 DEB；视觉手势识别演示 |
| 当前 rphand SDK | 源码基线 eb923ac | Linux；C++ / Python / 配套 Jazzy ROS 开发 |

前两项可从[下载清单](downloads.md)获取原版软件包与更新日志。根据原包说明核对设备固件、通信方式、系统依赖和相机要求；不要把 Windows 应用、其他通信方式示例或旧版 SDK 的安装步骤套到当前源码路线。

本次文档整理未安装、运行这些原版应用，也不声明它们已直接适配当前 rphand API。手势软件的存在不等于当前 ROS 节点已实现视觉映射；节点负责设备指令与反馈，识别 / 重定向由操作端应用承担。

需要控制自己的程序时，从[快速开始](quickstart.md)进入。需要录制已发布的手部 state/action 时，使用 [ROS 数据记录](ros2.md)。
