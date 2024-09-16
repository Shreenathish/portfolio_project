from flask import Flask,render_template
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
Bootstrap5(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project')
def project():
    name = "Project"
    return render_template('project_temp.html',name = name)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
