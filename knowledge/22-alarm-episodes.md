# Alarm episodes and refractory intervals

An above-threshold sample is not itself a new event. The implementation identifies rising edges of the Boolean score > threshold sequence. A continuous run of 100 positive samples produces one alarm onset.

A refractory interval further suppresses rising edges too close to the last accepted alarm. With refractory_samples = 20 at 200 Hz, the minimum accepted separation is 21 samples because the implemented comparison is strictly greater than 20.

Example: positive runs beginning at indices 10 and 15 are merged by suppression; a new run at 40 can produce another alarm. A missing score is not above threshold, so a later return above threshold can create a new onset if the refractory condition permits it.

**Why used:** frame counts inflate alarms for sustained responses and do not reflect event-level detection.

**Failure modes:** a long alarm beginning before the labeled event is a false alarm and does not become a successful detection merely by overlapping the event. A refractory interval can also suppress a real second event.

**Code:** [alarm_onsets](../src/tactile_lab/receivers/metrics.py). Parameter semantics are part of the measurement definition and must remain fixed across compared models.
