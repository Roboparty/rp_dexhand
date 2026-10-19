"""Offline spectral diagnostics; never used as a causal detector score."""
import numpy as np

def coherence(x, y, sample_rate_hz, segment_length=128):
    x,y=np.asarray(x,float),np.asarray(y,float)
    if x.ndim!=1 or x.shape!=y.shape or not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ValueError("need equal finite one-dimensional signals")
    if not np.isfinite(sample_rate_hz) or sample_rate_hz<=0:
        raise ValueError("sample rate must be positive")
    if isinstance(segment_length,bool) or not isinstance(segment_length,int) or segment_length<8:
        raise ValueError("segment length must be integer >= 8")
    stride=segment_length//2
    starts=list(range(0,len(x)-segment_length+1,stride))
    if len(starts)<3:
        raise ValueError("at least three overlapping segments required")
    window=np.hanning(segment_length)
    def transform(signal):
        return np.stack([np.fft.rfft((signal[s:s+segment_length]-signal[s:s+segment_length].mean())*window) for s in starts])
    a,b=transform(x),transform(y)
    px=np.mean(abs(a)**2,axis=0); py=np.mean(abs(b)**2,axis=0)
    cross=np.mean(a*np.conj(b),axis=0)
    denominator=px*py
    result=np.divide(abs(cross)**2,denominator,out=np.full_like(px,np.nan),where=denominator>np.finfo(float).tiny)
    return {"frequency_hz":np.fft.rfftfreq(segment_length,1/sample_rate_hz),
            "coherence":np.clip(result,0,1),"segments":len(starts)}

def estimate_lag(x,y,max_lag=20):
    """Positive lag means y arrives later than x; full-record offline diagnostic."""
    x,y=np.asarray(x,float),np.asarray(y,float)
    if x.ndim!=1 or x.shape!=y.shape or not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ValueError("need equal finite vectors")
    if isinstance(max_lag,bool) or not isinstance(max_lag,int) or not 0<=max_lag<len(x)-1:
        raise ValueError("invalid max lag")
    scores=[]
    for lag in range(-max_lag,max_lag+1):
        a=x[-lag:] if lag<0 else x[:len(x)-lag] if lag else x
        b=y[:len(y)+lag] if lag<0 else y[lag:] if lag else y
        a=a-a.mean(); b=b-b.mean()
        den=np.linalg.norm(a)*np.linalg.norm(b)
        scores.append(float(a@b/den) if den>0 else -np.inf)
    if not np.isfinite(scores).any():
        raise ValueError("constant signals have no identifiable lag")
    return int(np.argmax(scores)-max_lag)
