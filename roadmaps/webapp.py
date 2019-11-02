from flask import Flask, render_template
from network.edge import Edge
from network.node import Node
from network.graph import Graph

app = Flask(__name__)

@app.route('/')

def hello_world():
    new_dict={'car1': [{'lat': 42.436483, 'lng': -76.507386}, {'lat': 42.438501, 'lng': -76.464116}, {'lat': 42.447367, 'lng': -76.470143}]}
    return render_template("index-2.html", cars=new_dict)

if __name__ == '__main__':
    app.run()
