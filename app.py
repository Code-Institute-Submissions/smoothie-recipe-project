import os
from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] =''

@app.route('/')
def hello():
    return 'hello me'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)