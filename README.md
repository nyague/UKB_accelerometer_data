# UKB_accelerometer_data

accel_new_env: contains the base setup for the final accel_env environment (includes python version 3.9, scikit_lean 1.0.1, and other dependencies needed for the oxford accelerometer package to work)

accel_env: the processed environment that successfully runs the accelerometer package. Should create the environment faster than the base setup version

In bash before running the python kernel:
  -Set up the environment: conda env create -f accel_env.yaml
  -Activate the environment: conda activate accel_env
  -Create a python kernel that is within your environment: python -m ipykernel install --user --name accel_env --display-name "Python (Accelerometer)"
