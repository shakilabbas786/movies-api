from flask import Flask, request
from imdb import data
from flask_mysqldb import MySQL
import json
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

@app.route('/update_movies/', methods=["POST"])
def update_movies():
    cur = mysql.connection.cursor()
    for d in data:
        try:
            cur.execute("select id from movies where name = '"+d.get('name')+"' and director = '"+d.get('director')+"'")
            movieID = cur.fetchall()[0][0]
            print(movieID)
            query = """update movies set genre = '"""+json.dumps(d.get('genre'))+"""' where id = %s"""%(movieID)
            print(query)
            cur.execute(query)
            mysql.connection.commit()
        except Exception as e:
            pass

@app.route('/get_movies/', methods=["GET"])
def get_movies():
    result = []
    name = request.form['name']
    cur = mysql.connection.cursor()
    cur.execute("select name, director, imdb_score, popularity, genre from movies where name like '"+name+"%'")
    row = cur.fetchall()
    for r in row:
        result.append({"name":r[0], "director":r[1], "imdb":r[2], "popularity":r[3], "genre":r[4]})
    return json.dumps(result)

if __name__ == '__main__':
   app.run('139.59.66.134',8080, True)
