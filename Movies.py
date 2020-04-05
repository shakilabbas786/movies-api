from flask import Flask, request
app = Flask(__name__)


@app.route('/sign_up/',methods=["POST"])
def new_customer():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    username = request.form["username"]
    print last_name
    return '16-digit-token'

@app.route('/add_movie/', methods=["PUT"])
def add_movie():
    return "Movie Added"

@app.route('/get_movies/', methods=["GET"])
def get_movies():
    return 'Testing'

if __name__ == '__main__':
   app.run('0.0.0.0',8080, True)
