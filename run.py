#PLANTILLA O BASE PARA NUESTROS PROYECTOS 
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Flask'


if __name__ == '__main__':
    # We use debug = True to have the changes in the program in real time
    app.run(debug=True, port=8000)
