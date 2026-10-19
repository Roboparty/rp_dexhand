# Hardware Guide

[Home](../README.md) · [Quick start](quickstart.md) · [Model downloads](models.md)

## Product and dimensions

RP Hand uses a worm-gear transmission with 11 mechanical degrees of freedom and 6 actively controlled axes. The SDK's `RP_HAND_6DOF` refers to the six active axes; the current driver verifies total DOF 11 and active DOF 6 on successful initialization.

![RP Hand dimensions and wrist mounting dimensions, in mm](../assets/dimensions.png)

| Parameter | Manual specification |
| --- | --- |
| Dimensions | 147.54 × 73.53 × 26.35 mm |
| Weight | 379 g ± 10 g |
| Thumb lateral swing | 0°–87.5° |
| Thumb flexion/extension | 0°–65° |
| Four-finger flexion | 0°–72° |
| Idle current | ≤ 0.1 A |
| Maximum current | ≤ 2.5 A |
| Minimum opening/closing time | ≤ 0.7 s |
| Operating environment | -10–45 °C, 10%–90% RH |
| Storage temperature | -10–70 °C |
| Ingress protection | IP30 |

Some drawing labels are rounded; the table retains the manual's precise values. Use models and engineering drawings for the actual hardware revision when machining or mounting. These specifications are not per-axis software limits or load-calibration results.

## Pinout and power

![RP Hand plug and socket; note the pin 1 markers in the drawing](../assets/pinout.png)

| Pins | Signal | Purpose |
| --- | --- | --- |
| 1, 2 | VDC | Power input |
| 5, 6 | GND | Power ground |
| 3 | CANH / 485+ | Select according to the device's communication configuration |
| 4 | CANL / 485- | Select according to the device's communication configuration |

The product manual specifies `12 V (-10%) – 48 V (+10%)`. Before wiring, follow the delivered model's nameplate and matched power-supply requirements; this guide does not recommend operating at the upper limit. Identify pins from the plug/socket views shown, not wire colors. Connect and check wiring with power off, then follow the device's power-on procedure.

CAN-FD and RS485 share signal pins and are alternatives according to device configuration; this does not mean two different buses can be connected simultaneously.

## CAN-FD connection

A Linux-supported CAN-FD adapter is required. An ordinary CAN adapter is not a substitute. Match wiring, termination, grounding and power to the delivered device.

| Setting | Current SDK deployment guidance |
| --- | --- |
| Nominal bitrate | 1 Mbps |
| Data bitrate | 5 Mbps |
| Node ID | 1–127, matching the actual device configuration |
| Single-hand example interface | `can0`; adjust to the actual connection |
| Downstream two-hand examples | Left `can0`, right `can3`; these are not auto-detected values |
| Two-hand node IDs | Separate buses may each use 1; IDs must not conflict on a shared bus |
| Feedback configuration | Raw value 200 on all six axes, corresponding to 20 ms |

Interface configuration commands are maintained in the [SDK hardware setup guide](https://github.com/Roboparty/roboparty_dexhand/blob/046108e7ba800763a096ca1c99b04a8414797105/docs/hardware-setup.md). The library does not bring up interfaces or change system bitrates for the application.

## Active axes, left/right hands and models

Current examples use active axis IDs `1..6`; `0` means all axes in methods supporting broadcast. The precise mapping between six axes, physical fingers, left/right hands and URDF joints has not been fully verified. Do not infer it from array order.

Before model integration or teleoperation, confirm the [joint-mapping requirements](models.md) for the delivered version. Tactile sensing is optional hardware; the current public `HandDriver` interface does not expose tactile data.

## Care

Clean exterior surfaces regularly and keep cleaning fluid out of the palm. Contact product service personnel for calibration, disassembly or repair. Warranty and after-sales service follow the applicable sales terms.

Source: [RP Hand user manual](https://roboparty.feishu.cn/docx/SaoIdLjNeoOCVZxXzdIcqwLqnNb), revision 13, checked 2026-10-05. Access to the original Feishu page requires the corresponding permissions.
