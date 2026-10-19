# Tactile Intelligence: Two Project Plans

Status: synthetic software prototypes, evaluation tools and learning materials implemented; physical integration and hardware validation pending.
Prepared: 2026-10-18.

[Documentation](README.md) · [Hardware](docs/hardware.md) · [SDK](docs/sdk.md) · [ROS limitations](docs/ros2.md)

## Objective and evidence boundary

Build a robot hand that detects contact and slip reliably and adjusts its grasp using measured tactile feedback. Explore two distinct ideas:

1. **Body-meridian-inspired pathways:** test whether a predefined pathway graph helps combine tactile signals.
2. **A. Meridian-inspired adaptive receiver:** test whether adaptive filtering and signal integration improve tactile event detection.

Traditional body-meridian maps and A. Meridian's *Consciousness Spectrum Operations* are conceptual inspirations. They are not evidence that a robot has biological meridians, receives consciousness, or transmits torsion fields. Positive results would support the tested engineering architecture. Negative results should lead to dropping or revising the hypothesis.

This project concerns the robot's tactile perception. Human sensory feedback, electrical stimulation and medical claims are outside this first build.

## Repository and hardware scope

This repository contains documentation, resource inventories and the Python tactile research package. It does not implement the robot driver. Physical integration would use the separate upstream [SDK](https://github.com/Roboparty/roboparty_dexhand), with ROS integration optional and later.

The pinned documentation baseline describes:
- Six active axes and eleven mechanical DOF.
- Linux CAN-FD support in the maintained wrapper.
- Optional tactile hardware with no tactile readout in the public driver API.
- Cached getter feedback; freshness must be measured separately.
- Incomplete physical-to-model joint mapping and ROS feedback publication.
- A homing bypass in the inspected ROS motion path; use the controlled SDK acceptance route first.

These are documented limitations, not a fresh audit of every upstream release. Before implementation, record the chosen hardware revision and pin the actual driver commit/package. Confirm tactile access or choose a separate sensor acquisition device. Do not assume motor current is a calibrated contact-force measurement.

## Shared foundation

### Learn in dependency order

1. Units, uncertainty, calibration, probability and held-out evaluation.
2. Linear algebra, Fourier analysis, convolution, sampling, aliasing and filter responses.
3. Basic circuits, sensor readout, impedance, drift and hysteresis.
4. Mechanoreception, receptive fields, contact mechanics, friction and slip.
5. Robot kinematics, feedback control, delay, stability and actuator limits.
6. Graph signal processing and adaptive state estimation.

Connect these to the existing curriculum's mathematical foundations, classical ML, deep learning, evaluation and applied systems sections. Robotics, instrumentation and contact mechanics need dedicated study; transformer knowledge is not a prerequisite for the first experiments.

### Smallest physical platform

Start with one calibrated sensor on a benchtop fixture, then a small compliant tactile patch. Use pressure sensing for low-frequency contact and a suitable dynamic sensor for slip-related vibration if the pressure sensor lacks bandwidth. Do not assume every inexpensive force sensor can resolve slip.

Select parts only after specifying measurement range, bandwidth, sampling rate, mounting space, interface and cost. An optical tactile sensor such as [DIGIT](https://arxiv.org/abs/2005.14679) is a later option, subject to physical fit and acquisition support; compatibility with RP Hand is not established here.

Required functions:
- A repeatable contact fixture and known-load calibration method.
- Timestamped raw acquisition without automatic filtering that hides the input.
- Independent event reference, such as synchronized video or a measured displacement signal.
- A logger that records missing samples, clipping and acquisition configuration.
- A simple detector and offline replay before any actuator control.

### Data contract

For each run, save:
- Session ID, object ID, sensor ID, placement coordinates and mounting version.
- Monotonic timestamp, raw value, calibrated value and units.
- Sample rate, filter configuration, calibration ID and sensor limits.
- Event label and independent reference timestamp, including labeling uncertainty.
- Motor command/feedback timestamps when available, plus temperature or nuisance measurements when used.

Preserve raw observations. Derived features belong in separate files. Record synchronization offsets and uncertainty. Split training/validation/test by complete session and object, not adjacent frames from the same recording.

## Plan A — Body-meridian-inspired tactile pathways

### Hypothesis

At equal sensor positions, data and computational budget, a predefined pathway graph improves contact localization, slip detection or tolerance to missing sensors relative to independent processing and spatial-neighbor graphs.

The pathway graph is a proposed inductive bias. Mapping a human anatomical drawing onto a robotic surface is an approximation that must be documented.

### Milestones

| Stage | Learn | Build | Completion criterion |
| --- | --- | --- | --- |
| A1: Map | Hand anatomy, receptive fields, graphs | Sensor-coordinate map and pathway-to-node mapping | Every node and edge has an explicit rule; arbitrary choices are marked |
| A2: Measure | Calibration, hysteresis, mechanical coupling | Small tactile patch and repeatable contacts | Calibration report includes error, repeatability, drift, clipping and cross-talk |
| A3: Baseline | Classical classifiers, temporal features | Independent-sensor and spatial-neighbor models | Offline replay and frozen session/object test split work |
| A4: Pathway model | Adjacency matrices, Laplacians, graph filters | Same processing pipeline with pathway adjacency | Comparison changes graph structure only; feature windows and tuning budgets match |
| A5: Grasp | Feedback and stability | Detector-driven grip adjustment | Controlled object tests with verified limits, stopping and feedback freshness |

### Experiment

Freeze the pathway mapping before examining test performance. Compare:
1. Independent processing with shared aggregation.
2. Spatial-neighbor graph.
3. Meridian-inspired graph.

Keep identical sensors and their locations. Match edge counts where feasible and report degree distribution, parameter count and processing cost. A later physical-placement experiment must be separate from the graph experiment.

Primary endpoint: choose either contact-localization error in mm or slip-detection delay in ms at a fixed false-alarm rate before collecting the final dataset. Secondary endpoints: event recall, sensor-dropout degradation, latency and grasp success at matched force limits.

Use complete trials as the statistical unit; report paired differences and uncertainty across sessions/objects. Do not count correlated sensor frames as independent trials. Use pilot variability to determine the final number of trials before opening the test set.

### Continue or stop

Choose a minimum practically useful improvement after pilot measurement and before final evaluation. Continue only if the pathway model improves the primary endpoint beyond that margin without unacceptable latency or reliability costs. Otherwise keep the simpler graph and publish the negative result.

A gain does not establish Qi channels or anatomical meridian mechanisms. Test whether simpler features, connectivity or regularization explain it before claiming a distinctive pathway effect.

### Deliverables

Sensor map, mapping rationale, calibration report, dataset specification, baseline implementations, frozen experiment configuration, evaluation report and a short grasp demonstration if hardware is available.

## Plan B — A. Meridian-inspired adaptive tactile receiver

### Hypothesis

An adaptive receiver detects contact/slip more reliably than a fixed receiver when noise, vibration, sensor drift or contact conditions change.

Extract precise engineering questions from the manuscript's receiver language. Equations transferred from RF systems require their original assumptions; they do not automatically describe consciousness or tactile sensing.

| Inspiration | Operational meaning | Measurement |
| --- | --- | --- |
| Tuning | Select frequency bands useful for a tactile task | Detection performance across surfaces and speeds |
| Selectivity | Separate contact events from nuisance signals | Recall at a fixed false-alarm rate |
| Coherence | Quantify relationships between synchronized channels | Added predictive value beyond individual channels |
| Tracking | Update an estimate under changing conditions | Recovery time and error after a change |
| Receiver state | Maintain contact/slip estimates with uncertainty | Calibration, detection delay and stability |

### Milestones

| Stage | Learn | Build | Completion criterion |
| --- | --- | --- | --- |
| B1: Synthetic receiver | Fourier spectra, convolution, SNR and aliasing | Known event plus controlled nuisance signals | Recovery and failure regimes are measured; synthetic results labeled |
| B2: Fixed receiver | Filtering, thresholds and detection theory | Fixed filter and threshold baseline on recorded data | Reproducible held-out evaluation |
| B3: Adaptation | Noise estimation, adaptive thresholds, state estimation | Add one adaptive component at a time | Each component has a measured contribution and processing cost |
| B4: Sensor fusion | Cross-correlation, spectral coherence, clock alignment | Timestamp-aligned multichannel features | Gains survive motor-noise and timing-error controls |
| B5: Closed loop | Delay and control stability | Use receiver estimates in grip control | Better event detection improves actual grasp outcomes |

### Experiment

Start with raw thresholding, fixed filtering and adaptive filtering on exactly the same recordings. Challenge them with documented nuisance conditions: actuator vibration, gradual drift, changing contact speed and temporary missing samples.

Use independently labeled slip/contact events. Choose the primary endpoint and acceptable false-alarm rate from a pilot, then freeze both. Report delay, missed events, false alarms, recovery time, CPU cost and memory.

Coherent noise can look like coherent contact: include motor-only and no-contact trials. Train nuisance estimates without access to test labels. Assess both offline performance and causal online performance; a filter that uses future samples is not a deployable real-time detector.

Greater selectivity can increase delay. More cross-sensor coherence is not inherently better. Compare adaptation against an equally tuned fixed baseline and include failure cases such as adaptation suppressing a genuine weak event.

### Continue or stop

Continue only if adaptive processing beats the fixed baseline on unseen conditions by the prespecified useful margin and stays within the measured control-latency budget. If it only helps synthetic data or one known object, narrow the claim or keep the fixed receiver.

No successful receiver experiment would establish a consciousness field or torsion mechanism. Those would require a separate source model, detector model and controlled physical evidence.

### Deliverables

Signal generator, raw recordings, fixed/adaptive baselines, interference and timing tests, ablation report and a causal streaming demonstration.

## Combined experiment

Run this only after each individual experiment is reproducible:

| | Fixed receiver | Adaptive receiver |
| --- | --- | --- |
| Spatial-neighbor graph | Baseline | Receiver contribution |
| Meridian-inspired graph | Pathway contribution | Combined system |

Use the same dataset splits, sensor hardware, tuning budgets and endpoint definitions. Report each contribution and whether the combined effect differs from what the separate gains suggest. Do not change graph, sensor placement and receiver together without separate comparisons.

## Proposed 16-week curriculum

Assumption: about six hours per week, adjusted after the instrumentation pilot.

| Weeks | Focus | Deliverable |
| --- | --- | --- |
| 1–2 | Math, units, uncertainty and signals | Synthetic detector with known ground truth |
| 3–4 | Circuits, calibration and acquisition | One sensor, then a small patch; documented dataset |
| 5–7 | Contact mechanics and graph processing | Plan A baseline and pathway comparison |
| 8–10 | Filtering, adaptation and synchronization | Plan B fixed/adaptive comparison |
| 11–12 | Experimental design and combined evaluation | Four-condition result with uncertainty |
| 13–16 | SDK bring-up and feedback control | Hand integration if prerequisites pass; otherwise benchtop demonstration |

Weekly split: two hours foundations, one hour critical source reading, three hours experiments and analysis. If this replaces existing curriculum time, extend the schedule rather than dropping prerequisites.

For each speculative reading, record: exact source/page, proposed claim, established prerequisite, measurable prediction, competing explanation and a condition that would reject the claim. The torsion companion's energy, information-channel and experimental-design exercises can support this habit; do not treat simulations as physical detections.

## Hardware integration gates

1. Record hardware revision, firmware, power requirements, CAN-FD adapter and selected driver environment.
2. Verify communication without motion using the documented quick start.
3. Verify enabling/homing and a stopping method with bounded targets and a clear motion envelope.
4. Establish per-axis units and model mapping. Measure feedback freshness.
5. Validate the independent tactile acquisition path, mounting and clock alignment.
6. Replay detectors offline, then run observation-only alongside the hand.
7. Enable bounded grip adjustment only after stale/missing sensor behavior is defined and tested.

There is no claim that motor position commands provide force control. If direct force control is unavailable, validate a conservative position-based grip adjustment against independent force measurements. Do not infer load safety from motor current alone.

## Implemented research layout

- [Quickstart](RESEARCH_QUICKSTART.md): installation, tests, benchmarks and CSV replay.
- [Knowledge](knowledge/README.md): definitions, equations, assumptions and worked examples.
- [Status](IMPLEMENTATION_STATUS.md): completed software and remaining physical milestones.
- [Experiments](experiments/README.md): protocols for both plans and their combined comparison.
- [Configuration](configs/README.md): actual code defaults and parameter roles.
- [Data contract](data/README.md): synthetic examples and future measured recordings.
- `src/tactile_lab/`: executable prototypes, calibration, diagnostics and evaluation.
- `tests/`: analytical, causal, split-isolation and integration checks.

Keep large datasets outside Git with hashes and retrieval instructions. Commit configurations, small examples, analysis and reports. Record package versions and upstream commits. Publish positive and negative results with enough detail to reproduce them. The implementation is a learning/research foundation; the hardware gates above remain open.

## Reading and source roles

- RP Hand guides in this repository: hardware and integration constraints.
- RoboParty SDK and ROS repositories linked above: implementation interfaces; verify selected versions.
- [DIGIT paper](https://arxiv.org/abs/2005.14679): established optical tactile-sensor research, not a guarantee of mechanical compatibility.
- *The Body Meridians: Meridian Flows and Acu-Point Charts*, Natural-health-zone.com: pathway inspiration, not a verified robotic mechanism.
- A. Meridian, *Consciousness Spectrum Operations*: receiver-framework inspiration; preserve its distinctions between literal engineering and speculative extensions.
- *Torsion: geometry, models, and lecture claims* and its reproducible lab: exercises in mathematical definitions, model checking and experimental design.

Local reading PDFs are not redistributed in this repository. No novelty claim is made; complete a focused prior-art review before presenting either architecture as new.
