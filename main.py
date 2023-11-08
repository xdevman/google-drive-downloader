import os
import gdown

def download_file_from_google_drive(google_drive_url, output_file):
    gdown.download(google_drive_url, output_file, quiet=False)

# Read links from the text file
with open('download_links.txt', 'r') as file:
    links = file.readlines()

# Remove empty lines from the links
links = [link.strip() for link in links if link.strip()]

# Create the downloaded_files directory if it doesn't exist
download_dir = 'downloaded_files'
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Download files from Google Drive links and save them in the downloaded_files directory
for index, link in enumerate(links, start=1):
    output_file = os.path.join(download_dir, f'file{index}.mp4')
    download_file_from_google_drive(link, output_file)
    print(f'File downloaded: {output_file}')
