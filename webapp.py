from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/entertext')
def entertext():

    return render_template("entertext.html")

@app.route('/data', methods=['GET', 'POST'])
def save_content():
    if request.method == 'POST':
        name = request.form['Your Name']
        thoughts = request.form['Share your idea!']
        file = open("saveddata.txt", "a")
        file.write("[ " + name + ' -')
        file.write(" " + thoughts + "] \n")
        file.close()
        return render_template("index.html")

def data_opener():

    file = open("saveddata.txt", "r")
    line= file.read()
    return line

@app.route('/read')
def read_saved_data():

    return data_opener()

if __name__ == '__main__':
    app.run(debug=True)
