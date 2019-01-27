import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

#Path to where picture are uploaded
#UPLOAD_FOLDER is a directory you create where you can store uploaded files on a local machine
UPLOAD_FOLDER = '/Users/ibrahimmalik/Downloads/DeltaHacks/UPLOAD_FOLDER'
ALLOWED_EXTENSIONS = set([ 'pdf', 'png', 'jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
       #'upload_file' redirects webpage back to upload_file html after upload is successfully compelted
    return 0

if __name__ == "__main__":
    app.run(host = 'localhost', port = 8101, debug=True)
