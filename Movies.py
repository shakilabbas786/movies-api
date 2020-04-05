from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'ut-mysql01.do-blr.mpgpsdc.com'
app.config['MYSQL_USER'] = 'testuser'
app.config['MYSQL_PASSWORD'] = 'test@1235'
app.config['MYSQL_DB'] = 'testdb'
mysql = MySQL(app)

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
    cursor = mysql.connection.cursor()
    cursor.execute("select * from users;");
    row = cursor.fetchall()
    print str(row)
    return 'Testing'

if __name__ == '__main__':
   app.run('0.0.0.0',8080, True)
