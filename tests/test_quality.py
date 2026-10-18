import numpy as np
import pytest
from tactile_lab.quality import quality_report

def test_missing_coverage_and_zero_values():
    r=quality_report([0,.1,.2],[[0,np.nan],[0,0],[np.nan,np.nan]])
    assert r["observed_fraction"]==.5 and r["all_channels_missing_frames"]==1
    assert r["nominal_rate_hz"]==10
def test_jitter_is_reported():
    assert quality_report([0,.1,.21],[1,2,3])["max_relative_jitter"]>0
def test_backwards_time():
    with pytest.raises(ValueError): quality_report([0,-1],[1,2])
