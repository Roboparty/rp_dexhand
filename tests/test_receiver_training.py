import pytest
from tactile_lab.receivers.synthetic import generate_dataset
from tactile_lab.receivers.training import fit_config,select_threshold

def test_training_rejects_test():
    with pytest.raises(ValueError): fit_config([t for t in generate_dataset(1,1) if t.split=="test"])
def test_threshold_selection_rejects_train():
    ts=[t for t in generate_dataset(1,1) if t.split=="train"]
    with pytest.raises(ValueError): select_threshold(ts,[t.samples for t in ts],[1])
def test_initial_noise_positive():
    ts=[t for t in generate_dataset(1,1) if t.split=="train"]
    assert fit_config(ts).initial_noise>=.03
