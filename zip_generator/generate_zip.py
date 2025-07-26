# This script generates a zip file containing a payload script.
# It ensures the zip file is created in the same directory as this script,
# and checks if the payload file exists before attempting to create the zip.

import zipfile # Creating zip files
import sys # System-specific parameters and functions
import os # File and path manipulation


# 1. Get the absolute path of the directory where this script is located.
#    __file__ is the path to this script (generate.py).
#    os.path.abspath() gets its full path
#    os.path.dirname() gets the directory part of that path (e.g., '.../zip_generator').
scriptDir = os.path.dirname(__file__)
print(f"Script is running from: {scriptDir}")

# 2. Define the full path for the output zip file.
#    Uses os.path.join to safely combine the script's directory
#    with the desired zip filename. This ensures the zip is always
#    created in the same folder as generate.py.
outputZipPath = os.path.join(scriptDir, 'malicious.zip')
print(f"Output zip file will be created at: {outputZipPath}")

# 3. Define the full path to the payload script we want to add.
#    Starts from the script's directory, go up on level ('..'),
#    and then into the 'malware_simulator' folder to find 'payload.py'.
payloadSourcePath = os.path.join('malware_simulator', 'payload.py')
print(f"Looking for payload at: {payloadSourcePath}")

# 4. Check if the payload file exists BEFORE trying to create the zip.
#    If it doesn't exist, print an ERROR message.
#    If it does exist, proceed to create the zip file.
if not os.path.exists(payloadSourcePath):
    print(f"ERROR: The payload source file is located at: {payloadSourcePath}")
    print("ERROR: The payload source file does not exist. Zip file creation aborted. Please check the path.")
    sys.exit(1)
else:
    print(f"Payload source file found at: {payloadSourcePath}")
    try:
        # 5. Attempt to open the payload file to ensure it's accessible.
        with open(payloadSourcePath, 'r') as f:
            print("Payload source file is accessible.")
    except Exception as e:
        print(f"ERROR: Unable to access the payload source file. {e}")
        sys.exit(1)
    # 6. If the file is accessible, proceed to create the zip file.
    with zipfile.ZipFile(outputZipPath, 'w') as z:
        # 7. Write the payload file to the zip.
        #    The first argument is the source file on your computer.
        #    The 'arcname' argument specifies what the file will be named inside the zip.
        #    This prevents the zip from containing the '../malware_simulator/' folders
        z.write(payloadSourcePath, arcname='payload.py')
    # 8. Check if the zip file was created successfully.
    if os.path.exists(outputZipPath):
        print(f"Zip file created successfully at: {outputZipPath}")
    else:
        # This case is highly unlikely, but it's good to check.
        print(f"ERROR: Failed to create zip file at: {outputZipPath}")
