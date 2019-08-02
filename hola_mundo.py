from flask import Flask

app = Flask(__name__)  # instance new object


@app.route('/')  # wrap o decorator (the route where user can enter)
def index():
    return 'Hola Mundo!'  # Return a String


app.run()  # Execute the server in the port 5000
