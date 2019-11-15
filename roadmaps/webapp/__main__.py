import temep
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
#ogging.basicConfig(level=logging.DEBUG)
def run_app():
    temp = temep.getPlanarGraphAsDict()
    return render_template("index.html", cars=temp)

if __name__ == '__main__':
    app.run()
