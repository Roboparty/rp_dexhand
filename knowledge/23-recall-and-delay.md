# Event recall and conditional detection delay

An event occupies the half-open index interval [start,end). An alarm matches when start ≤ alarm < end. Only the first matching alarm contributes a delay for that event.

Recall = detected_events / total_events. Delay in milliseconds is 1000(alarm − start)/f_s. Missed events have no measured detection delay.

Example: five events, four detected, delays [10,20,30,40] ms. Recall is 0.8 and median detected delay is 25 ms. Reporting only 25 ms omits the missed fifth event. Assigning that miss zero latency would be incorrect.

**Why used:** a detector can look fast by detecting only easy events. Recall, false alarms and latency must be interpreted together.

For an evaluation set with no positive events, recall is null rather than zero. If no events are detected, delay is null. Multiple alarm onsets within one event do not increase the event count.

**Limits:** event interval length determines how late a response may still count. Reference timing uncertainty is not modeled by the synthetic generator and must be measured for real data.

**Code:** [evaluate_trial and aggregate](../src/tactile_lab/receivers/metrics.py).
