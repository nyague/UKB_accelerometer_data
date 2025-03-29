import sys
print(sys.executable)
print(sys.version)

#!python --version

import jdk
from jdk.enums import OperatingSystem, Architecture

# Download and install the JDK
jdk.install('11', jre=True, operating_system=OperatingSystem.LINUX)

import os
# Set JAVA_HOME and PATH for this Python session
jdk_version = 'jdk-11.0.26+4-jre'
os.environ['JAVA_HOME'] = f"/home/dnanexus/.jre/jdk-11.0.26+4-jre"
os.environ['PATH'] += f":{os.environ['JAVA_HOME']}/bin"

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

import sys
import os

# Build the path to the correct tool
acc_bin = os.path.join(os.path.dirname(sys.executable), "accProcess")
plot_bin = os.path.join(os.path.dirname(sys.executable), "accPlot")

# Run them safely
!{acc_bin} data/sample.cwa.gz
!{plot_bin} data/sample-timeSeries.csv.gz

# Define binary path for accProcess
acc_bin = os.path.join(os.path.dirname(sys.executable), "accProcess")

# Download a sample CWA file
#!dx download /Bulk/Activity/Raw/10/1000064_90001_0_0.cwa

# Process the CWA file
!{acc_bin} 10/1000064_90001_0_0.cwa --outputFolder accOut

# Upload the results
!dx upload accOut -r --destination Accelerometer_data/