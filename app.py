from flask import Flask, request, jsonify, render_template
from textsummarizer import *
from PyPDF2 import PdfReader
from transformers import pipeline

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize',methods=['POST'])
def summarize():
    
    if request.method == 'POST':
        #fetching file from html form
        text = request.files['myfile']
        text.save(text.filename)

        #for getting file extension
        find_file = text.filename
        x = find_file.split(".")
        extension = x[1]


        if extension == "pdf":
            reader = PdfReader(text.filename)
            
            # getting a specific page from the pdf file
            page = reader.pages[0]
            
            # extracting text from page
            file_text = page.extract_text()
        else:
            #for txt file
            f = open(text.filename, "r")
            file_text = f.read()


        if not request.form['numOfLines']:
            numOfLines = 3
        else:
            numOfLines = int(request.form['numOfLines'])
            
        # summary = generate_summary(file_text)
        print("Text of file: ",file_text)
        summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")
        summarize_text = summarizer(file_text)
        listToStr = ' '.join([str(elem) for elem in summarize_text])
        return render_template('result.html',
                               text_summary=listToStr,
                            #    lines_original = original_length,
                               lines_summary = numOfLines,
                               file_name = text.filename)
    
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)
    