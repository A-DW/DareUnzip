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
script_dir = os.path.dirname(os.path.dirname(__file__))
print(f"Script is running from: {script_dir}")

# 2. Define the full path for the output zip file.
#    Uses os.path.join to safely combine the script's directory
#    with the desired zip filename. This ensures the zip is always
#    created in the same folder as generate.py.
output_zip_path = os.path.join(script_dir, "malicious.zip")
print(f"Output zip file will be created at: {output_zip_path}")

# 3. Define the full path to the payload script we want to add.
#    This path is constructed relative to the project root to ensure
#    it works regardless of where the script is run from.
payload_source_path = os.path.join("malware_simulator", "payload.py")
print(f"Looking for payload at: {payload_source_path}")

# 4. Check if the payload file exists BEFORE trying to create the zip.
#    If it doesn't exist, print an ERROR message.
#    If it does exist, proceed to create the zip file.
if not os.path.exists(payload_source_path):
    print(f"ERROR: The payload source file is located at: {payload_source_path}")
    print("ERROR: The payload source file does not exist. Zip file creation aborted. Please check the path.")
    sys.exit(1)
else:
    print(f"Payload source file found at: {payload_source_path}")
    try:
        # 5. Attempt to open the payload file to ensure it's accessible.
        with open(payload_source_path, 'r') as f:
            print("Payload source file is accessible.")
    except Exception as e:
        print(f"ERROR: Unable to access the payload source file. {e}")
        sys.exit(1)
    # 6. If the file is accessible, proceed to create the zip file.
    with zipfile.ZipFile(output_zip_path, 'w') as z:
        # 7. Write the payload file to the zip.
        #    The first argument is the source file on your computer.
        #    The 'arcname' argument specifies what the file will be named inside the zip.
        #    This prevents the zip from containing the '../malware_simulator/' folders
        z.write(payload_source_path, arcname='payload.py')
    # 8. Check if the zip file was created successfully.
    if os.path.exists(output_zip_path):
        print(f"Zip file created successfully at: {output_zip_path}")
    else:
        # This case is highly unlikely, but it's good to check.
        print(f"ERROR: Failed to create zip file at: {output_zip_path}")
