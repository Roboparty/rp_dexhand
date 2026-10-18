"""Run after editable installation: python examples/calibration_demo.py."""
from tactile_lab.calibration import fit_linear
model=fit_linear([0,1,2,3],[1,3,5,7],unit="N")
print("gain, offset, fit RMSE:",model.gain,model.offset,model.rmse)
print("at raw 1.5:",float(model.apply(1.5)),model.unit)
print("Exact synthetic reference example; not a physical sensor calibration.")
