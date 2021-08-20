from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from summarizer import summarize
import nltk

app = Flask(__name__)

@app.route('/upload')
def index():
   return render_template('upload.html') 
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploads_file():
    if request.method == 'POST':
        f = request.files['file']
        filepath=secure_filename(f.filename)
        f.save(filepath)
        with open(filepath,'r') as w:
            text=w.read()
        test=summarize(text)
        test=test['summary']
        str = ""
        for ele in test: 
            str += ele 
        return render_template('summary.html',result=str)

if __name__ == '__main__':
    app.run(debug = True)