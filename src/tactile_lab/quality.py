"""Descriptive acquisition-quality checks; no silent repairs."""
import numpy as np

def quality_report(timestamps_s, samples):
    t,x=np.asarray(timestamps_s,float),np.asarray(samples,float)
    if t.ndim!=1 or len(t)<2 or x.shape[0]!=len(t) or not np.isfinite(t).all():
        raise ValueError("require matching samples and finite timestamps")
    dt=np.diff(t)
    if (dt<=0).any() or np.isinf(x).any():
        raise ValueError("time must increase and samples cannot contain infinity")
    observed=np.isfinite(x)
    nominal=float(np.median(dt))
    return {"samples":len(t),"channels":1 if x.ndim==1 else int(np.prod(x.shape[1:])),
            "nominal_rate_hz":1/nominal,"max_relative_jitter":float(np.max(abs(dt-nominal))/nominal),
            "observed_fraction":float(observed.mean()),"duration_s":float(t[-1]-t[0]),
            "all_channels_missing_frames":int((~observed).sum()) if x.ndim==1 else int((~observed).reshape(len(t),-1).all(axis=1).sum())}
