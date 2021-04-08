import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    if os.path.exists('static/generated.mp4'):
      os.remove('static/generated.mp4')
    
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    file = request.files['file']
    if file.filename == '':
	    flash('No image selected for uploading')
	    return redirect(request.url)
    if file and allowed_file(file.filename):
	    filename = secure_filename('source.png')
	    file.save(os.path.join('static/uploads/', filename))
	    #print('upload_image filename: ' + filename)
	    #flash('Image successfully uploaded and displayed below')
	    #return render_template('index.html', filename=filename)
    else:
	    flash('Allowed image types are -> png, jpg, jpeg, gif')
	    return redirect(request.url)

    import convert 
    return render_template('index.html')
     

