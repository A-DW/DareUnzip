# DareUnzip

This project is a simulation of a common malware delivery and operation pattern. This project demonstrates how a payload can be packaged, delivered via a web server, and establish a connection back to a Command and Control (C2) server.

## Architecture

The project is divided into four main components:

1.  **Zip Generator (`zip_generator/`):** A Python script that packages the `payload.py` into a `malicious.zip` file.
2.  **Web Server (`webserver/`):** A Flask-based web server that hosts the `malicious.zip` file and logs download requests.
3.  **Malware Simulator (`malware_simulator/`):** The `payload.py` script that, when executed on a target machine, will "phone home" to the C2 server.
4.  **C2 Server (`c2_server/`):** A server that listens for incoming connections from the payload, logs the interaction, and can send back commands.

A visual diagram of this flow can be found in `docs/diagrams.mmd`.

## Setup

1.  Clone the repository to your local machine.
2.  It is recommended to create and activate a virtual environment.
3.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

All commands should be run from the root directory of the project.

1.  **Generate the ZIP file:**
    This script creates `malicious.zip` inside the `zip_generator/` directory.
    ```bash
    python zip_generator/generate_zip.py
    ```

2.  **Start the Web Server:**
    This will start the Flask server, making the file available for download.
    ```bash
    python webserver/serve_zip.py
    ```

3.  **Download the file:**
    Open a browser or use a tool like `curl` to download the file from `http://127.0.0.1:8000/download`.