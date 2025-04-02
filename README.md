# UKB_accelerometer_data

accel_new_env: contains the base setup for the final accel_env environment (includes python version 3.10, scikit_lean 1.0.1, and other dependencies needed for the oxford accelerometer package to work)

In bash before running the python kernel:
  -Set up the environment: conda env create -f accel_new_env.yaml
  -Activate the environment: conda activate accel_env
  -Create a python kernel that is within your environment: python -m ipykernel install --user --name accel_env --display-name "Python (Accelerometer)"
  -Install ipykernel: conda install ipykernel
  -To remove an ipykernel before reinstalling: jupyter kernelspec uninstall accel_env
  - To remove the environment use: conda deactivate and conda env remove -n accel_env

Light_Data.ipynb: contains code required to use GGIR packahe in R, look at metadata containing header info, and see light data (including lightmean and lightpeak)

