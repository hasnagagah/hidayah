import flask
from flask import jsonify

app=flask.Flask(__name__)
app.config["DEBUG"]=True

books=[
    {'id':0,
     'title':'A fire Upon the Deep'},
    {'id':1,
     'title':'The One Who Walk'},
]

@app.route('/',methods=['GET'])
def home():
    return\
        '<h1>Distant Reading Archive</h1>'\
        '<p>'\
        'This site is a prototype API '\
        'for distance reading of '\
        'science fiction novels</p>'

@app.route('/api/v1/resources/books/all',
    methods=['GET'])
def api_all():
    return jsonify(books)






app.run()
