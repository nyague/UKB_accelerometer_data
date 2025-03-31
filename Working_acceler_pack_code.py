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

# Define binary path for accProcess
acc_bin = os.path.join(os.path.dirname(sys.executable), "accProcess")

# Download a sample CWA file
!mkdir -p data
!dx download /Bulk/Activity/Raw/10/1000064_90001_0_0.cwa -o data/

# Process the CWA file
!{acc_bin} data/1000064_90001_0_0.cwa --outputFolder accOut

# Upload the results
#!dx upload accOut -r --destination Accelerometer_data/