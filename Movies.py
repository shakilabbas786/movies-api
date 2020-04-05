from flask import Flask, request
from imdb import data
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'ut-mysql01.do-blr.mpgpsdc.com'
app.config['MYSQL_USER'] = 'testuser'
app.config['MYSQL_PASSWORD'] = 'test@1235'
app.config['MYSQL_DB'] = 'testdb'
mysql=MySQL(app)

@app.route('/sign_up/',methods=["POST"])
def new_customer():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    username = request.form["username"]
    print last_name
    return '16-digit-token'

@app.route('/add_movie/', methods=["PUT"])
def add_movie():
    cur = mysql.connection.cursor()
    for d in data:
        cur.execute("INSERT INTO movies (name, director, popularity, imdb_score) VALUES ('%s', '%s', %s, %s)"%(d.get("name"), d.get("director"), d.get("99popularity"), d.get("imdb_score")))
        mysql.connection.commit()
    return "Movie Added"

@app.route('/get_movies/', methods=["GET"])
def get_movies():
    name = request.form['name']
    cur = mysql.connection.cursor()
    cur.execute("select * from movies where name like '"+name+"%'")
    row = cur.fetchall()
    print str(row)
    return 'Testing'

if __name__ == '__main__':
   app.run('139.59.66.134',8080, True)
