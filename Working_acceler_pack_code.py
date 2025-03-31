import sys
print(sys.executable)
print(sys.version)

#!python --version

import jdk
from jdk.enums import OperatingSystem, Architecture

# Download and install the JDK
jdk.install('11', jre=False) #operating_system=OperatingSystem.LINUX

import os
# Set JAVA_HOME and PATH for this Python session
jdk_version = 'jdk-11.0.26+4'
os.environ['JAVA_HOME'] = f"/home/dnanexus/.jdk/jdk-11.0.26+4"
os.environ['PATH'] += f":{os.environ['JAVA_HOME']}/bin"

!java -version
!javac -version

# Confirm
print("JAVA_HOME:", os.environ['JAVA_HOME'])
print("OS:", jdk.OS)
print("ARCH:", jdk.ARCH)

# Optional: print download URL
download_url = jdk.get_download_url('11', jre=True)
print("Download URL:", download_url)

!ls {os.environ['JAVA_HOME']}/bin
!{os.environ['JAVA_HOME']}/bin/java --version

import sys
!{sys.executable} -m pip install accelerometer

!javac -cp "/opt/conda/envs/accel_env/lib/python3.10/site-packages/accelerometer/java/JTransforms-3.1-with-dependencies.jar" \
/opt/conda/envs/accel_env/lib/python3.10/site-packages/accelerometer/java/*.java

!ls /opt/conda/envs/accel_env/lib/python3.10/site-packages/accelerometer/java/*.class
###############################################PROCESS 1 CWA FILE############################################################
# Define binary path for accProcess
acc_bin = os.path.join(os.path.dirname(sys.executable), "accProcess")

# Download a sample CWA file
!mkdir -p data
!dx download /Bulk/Activity/Raw/10/1000064_90001_0_0.cwa -o data/

# Process the CWA file
!{acc_bin} data/1000064_90001_0_0.cwa --outputFolder accOut

# Upload the results
#!dx upload accOut -r --destination Accelerometer_data/

##############################################PROCESS ALL CWA FILES###########################################################
import subprocess
# List CWA files in the specified folder
result = subprocess.run(["dx", "ls", "/Bulk/Activity/Raw/10/"], capture_output=True, text=True)

# Extract file names ending in .cwa
cwa_files_10 = [f.strip() for f in result.stdout.splitlines() if f.endswith(".cwa")]

# Show the first few for verification
print("Found CWA files:", cwa_files_10[:5])


# Make folders
os.makedirs("cwa_input", exist_ok=True)
os.makedirs("accOut", exist_ok=True)

# Loop through and process each file
for file in cwa_files_10:
    file_path = f"/Bulk/Activity/Raw/10/{file}"
    local_path = f"cwa_input/{file}"

    print(f"Downloading {file}...")
    subprocess.run(["dx", "download", file_path, "-o", local_path], check=True)

    print(f"Processing {file}...")
    subprocess.run([acc_bin, local_path, "--outputFolder", "accOut"], check=True)
