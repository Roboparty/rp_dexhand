"""Event-level metrics; missed events never receive a fabricated latency."""
import numpy as np


def alarm_onsets(scores, threshold, refractory_samples=20):
    scores = np.asarray(scores, dtype=float)
    if scores.ndim != 1 or not np.isfinite(threshold) or threshold < 0:
        raise ValueError('scores must be 1D and threshold finite and nonnegative')
    if isinstance(refractory_samples, bool) or not isinstance(refractory_samples, int) or refractory_samples < 0:
        raise ValueError('refractory_samples must be a nonnegative integer')
    above = np.isfinite(scores) & (scores > threshold)
    previous = False
    last = -refractory_samples - 1
    alarms = []
    for i, active in enumerate(above):
        if active and not previous and i - last > refractory_samples:
            alarms.append(i)
            last = i
        previous = bool(active)
    return alarms


def evaluate_trial(trial, scores, threshold, refractory_samples=20):
    scores = np.asarray(scores, dtype=float)
    if scores.shape != trial.samples.shape:
        raise ValueError('score length must match trial')
    alarms = alarm_onsets(scores, threshold, refractory_samples)
    matched = set()
    delays = []
    false_alarms = 0
    background = np.isfinite(scores)
    for start, end in trial.events:
        background[start:end] = False
    for alarm in alarms:
        matches = [j for j, (start, end) in enumerate(trial.events) if start <= alarm < end]
        if matches:
            j = matches[0]
            if j not in matched:
                matched.add(j)
                delays.append(1000 * (alarm - trial.events[j][0]) / trial.sample_rate_hz)
        else:
            false_alarms += 1
    minutes = float(background.sum() / trial.sample_rate_hz / 60)
    return dict(trial_id=trial.trial_id, session_id=trial.session_id,
                object_id=trial.object_id, scenario=trial.scenario,
                events=len(trial.events), detected_events=len(matched),
                missed_events=len(trial.events) - len(matched),
                detection_delays_ms=delays, false_alarms=false_alarms,
                background_minutes=minutes, alarm_indices=alarms,
                observed_samples=int(np.isfinite(scores).sum()),
                total_samples=len(scores))


def aggregate(rows):
    events = sum(r['events'] for r in rows)
    detected = sum(r['detected_events'] for r in rows)
    minutes = sum(r['background_minutes'] for r in rows)
    false = sum(r['false_alarms'] for r in rows)
    delays = [d for r in rows for d in r['detection_delays_ms']]
    return dict(trials=len(rows), events=events, detected_events=detected,
                recall=detected / events if events else None,
                false_alarms=false, background_minutes=minutes,
                false_alarms_per_minute=false / minutes if minutes else None,
                median_detected_latency_ms=float(np.median(delays)) if delays else None,
                mean_detected_latency_ms=float(np.mean(delays)) if delays else None)
