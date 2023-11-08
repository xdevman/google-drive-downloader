# google-drive-downloader

# Google Drive Downloader & Flask Web Server

Installation of Libraries
To run this project, first install the necessary libraries. Use the following command to install the required libraries:


pip install gdown Flask

## Downloading Files from Google Drive

Use the `main.py` file to download links from Google Drive.


## Setting Up Flask Web Server

Use the `app.py` file to launch the web server with Flask.

# Running the Applications
Google Drive Downloader:
Run `main.py` to download files from the specified Google Drive links.

Flask Web Server:
Run `app.py` with the following command to start the Flask web server:

screen -S webapp python3 app.py

Access the files via the following URL:

`http://<server_ip>:5000/downloads/<filename>`

Replace `<server_ip>` with the IP address or hostname of your server and `<filename>` with the desired file name.

