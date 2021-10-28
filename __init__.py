from flask import Flask, g, render_template, request
from .app import insert_message, random_message

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('base.html')

@app.route('/submit/', methods=['POST', 'GET'])
def submitDemo():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        try:
            insert_message(request)
            return render_template('submit.html', thanks = True)
        except:
            return render_template('submit.html')

@app.route('/view/')
def main():
    return render_template('view.html')