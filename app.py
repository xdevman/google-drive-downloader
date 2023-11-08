from flask import Flask, send_from_directory

app = Flask(__name__)

download_dir = 'downloaded_files'

@app.route('/')
def index():
    return 'Welcome to the file download server!'

@app.route('/downloads/<filename>')
def download_file(filename):
    return send_from_directory(download_dir, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
