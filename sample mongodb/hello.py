import os
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb+srv://m001-student:m001-mongodb-basics@cluster0-k0dmp.mongodb.net/test?retryWrites=true&w=majority')
db = client.test

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    new = False
    if request.method == 'POST' and 'name' in request.form:
        name = request.form['name']
        if db.test.names.find_one({'name': name}) is None:
            # this is a new name, add it to the database
            db.test.names.insert({'name': name})
            new = True
    return render_template('index.html', name=name, new=new)

if __name__ == '__main__':
    app.run(debug=True)