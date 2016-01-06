import MySQLdb

from flask import Flask, request
app = Flask(__name__)

import Application

@app.route("/hello")
def hello():
    return "Hello Worlddd!"


@app.route("/authenticate", methods=['POST'])
def authenticate():
    content = request.get_json()
    print content
    return str(content)

@app.route("/db", methods=['GET'])
def connection():
    print "con setup"
    con = MySQLdb.connect('dev.monoxor.com', 'jam', 'jam', 'jam')
    print con
    cursor = con.cursor()
    cursor.execute("select * from company")
    data = cursor.fetchone()
    print data
    return str(data)


if __name__ == "__main__":
    app.run()
    connection()
