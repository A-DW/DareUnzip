# Use Flask for a simple HTTP(S) server to serve a zip file
from flask import Flask, request, send_file, send_from_directory, jsonify, abort
import os
import logging

# Each ZIP download logs:
# - The path of the zip file requested
# - The server should be able to serve the zip file over HTTP(S) protocol.
# - The size of the zip file
# - The IP address of the client (from HTTP request)
# - The user agent of the client
# - The timestamp of the request
# - Fingerprinting information (e.g., user machine details)
# - The time taken to process the request
# - The HTTP(S) status code returned and method used
# - The referrer URL (if available)
# - The response headers sent back to the client
# - The server should implement proper security measures to protect against common web vulnerabilities.
# - The server should handle errors gracefully and log them appropriately.
# - The server should log all requests and responses for auditing and debugging purposes.
# - All logs should be stored in a secure location on the 'docs' directory.
# - Final status of the request (success or failure)
# - Any error messages if the request fails


# --- Configuration ---
HOST = '0.0.0.0'
PORT = 8000

app = Flask(__name__)

banner = """
+-------------------------+
| Initializing Web Server |
+-------------------------+
"""
print(banner)

# Get the directory where this script (serve_zip.py) is located.
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Web server script directory is running from: {script_dir}\n")

# Go up one level to the project root ('DareUnzip/')
project_root = os.path.dirname(script_dir)
print(f"Project root is: {project_root}\n" + "-" * 40 + "\n")

print(f"### CHECKING IF ZIP FILE EXISTS ###\n")

# Construct the full, reliable path to the zip file.
zip_folder = 'zip_generator'
zip_file = 'malicious.zip'
print(f"Attempting to serve the zip file: {zip_file}\n")
zip_directory_path = os.path.join(project_root, zip_folder)
full_zip_path = os.path.join(zip_directory_path, zip_file)

@app.route('/download')
def download_zip():
    """Servers the malicious.zip file for download."""
    # Check for file existence on each request in case it's deleted while running
    if not os.path.exists(full_zip_path):
        # Abort with a 404 Not Found error if the file isn't there.
        abort(404, description="File not found on server")

    # Log request details (as outlined in the initial comments)
    print(f"--- New Download Request ---")
    print(f"IP address: {request.remote_addr}")
    print(f"User-Agent: {request.user_agent}")
    print(f"Servicing file: {zip_file}")
    print("-" * 40 + "\n")

    # Use send_form_directory for security. It prevents path traversal attacks.
    # 'as_attachment=True' prompts the user's browser to save the file
    return send_from_directory(directory=zip_directory_path, path=zip_file, as_attachment=True)

if __name__ == '__main__':
    # A quick check before starting to give the user immediate feedback.
    if not os.path.exists(full_zip_path):
        print(f"ERROR: Zip file not found at '{full_zip_path}'")
        print(f"Please run the 'generate_zip.py' script first, located at the 'zip_generator' folder, and then come back here!\n")
    else:
        print(f"SUCCESS: Found '{full_zip_path}' ready to be served.\n")
    
    print(f"Flask server starting on http://{HOST}:{PORT}")
    print(f"To download the file, visit http://127.0.0.1:{PORT}/download")
    app.run(host=HOST, port=PORT, debug=False)