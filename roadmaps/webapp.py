from flask import Flask, render_template
import sys
import generate_planar_graph

app = Flask(__name__)

@app.route('/')

#ogging.basicConfig(level=logging.DEBUG)
def run_app():
    #new_dict={'car1': [{'lat': 42.436483, 'lng': -76.507386}, {'lat': 42.438501, 'lng': -76.464116}, {'lat': 42.447367, 'lng': -76.470143}]}
    temp_planar_graph = generate_planar_graph.getPlanarGraphAsDict()
    return render_template("index.html", cars=temp_planar_graph)

if __name__ == '__main__':
    app.run()
