# Fourier representation and spectral resolution

For N samples, the discrete Fourier transform is X[k] = Σ_(n=0)^(N−1) x[n] exp(−j2πkn/N). Frequency bin k corresponds to f_k = k f_s/N Hz.

At f_s = 200 Hz and N = 128, adjacent bins are 1.5625 Hz apart. A 25 Hz sinusoid lies exactly at bin 16. This is a frequency-grid spacing, not a universal guarantee of resolving two nearby tones.

**Why used:** vibration can be inspected by frequency rather than only by total amplitude. The offline coherence diagnostic uses real-input FFTs on windowed segments.

**Assumptions:** frequency interpretation assumes a known, uniform sample rate. Sampling at f_s cannot uniquely distinguish all continuous signals above f_s/2 from lower-frequency aliases without additional restrictions and appropriate acquisition filtering.

**Failure modes:** a finite segment truncates the signal. A Hann window reduces discontinuities at segment boundaries but broadens spectral peaks. Zero padding can interpolate a spectrum without adding measured information.

**Implementation status:** FFTs support the offline coherence function; the main causal detector does not perform FFT-based band selection.

**Code:** [spectral diagnostics](../src/tactile_lab/spectral.py).
