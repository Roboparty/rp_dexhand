# Hardware

[Home](../../README.md) · [中文](../hardware.md) · [Quick start](quickstart.md)

RP Hand has 11 mechanical DoF, including 6 active axes and 5 passive/coupled DoF, with worm-gear transmission. The product-manual values below are not per-axis software limits or a calibration result.

![Dimensions and wrist mounting, mm](../../assets/dimensions.png)

| Property | Manual value |
| --- | --- |
| Dimensions | 147.54 × 73.53 × 26.35 mm |
| Mass | 379 ± 10 g |
| Thumb abduction | 0..87.5° |
| Thumb flexion | 0..65° |
| Other finger flexion | 0..72° |
| Static / maximum current | ≤ 0.1 A / ≤ 2.5 A |
| Manual minimum opening/closing time | ≤ 0.7 s; test conditions not specified in this guide |
| Operating environment | -10..45 °C, 10%..90% RH |
| Storage temperature | -10..70 °C |
| Ingress rating | IP30 |

## CAN-FD pinout and power

![Connector views; identify pin 1 in the drawing](../../assets/pinout.png)

| Pins | Signal |
| --- | --- |
| 1, 2 | VDC |
| 5, 6 | GND |
| 3 | CANH |
| 4 | CANL |

The manual lists input power as `12 V (-10%) .. 48 V (+10%)`. Confirm the supplied model, nameplate and power supply before wiring; the upper bound is not a recommended operating setpoint. Identify plug/socket orientation from the drawing, not wire colors. Connect with power off.

This guide covers CAN-FD firmware/configuration. Other transports require matching firmware and wiring. Reference bus rates are 1 Mbit/s arbitration, 5 Mbit/s data; node IDs are 1..127. Default integration examples use left can0/right can3 with ID 1 on separate buses.

See [SDK](sdk.md) for source-defined axis order and units, and [models](models.md) for calibration boundaries. Tactile acquisition is not part of this integration path.

Product source: RP Hand manual revision 13, archived 2026-10-05. Source records are in [maintenance](../maintenance.md); confirm the actual hardware revision before machining or assembly.
