from flask import Flask, request
app = Flask(__name__)

from helper import DB
from jam import app



class Location:

    @app.route("/location/create", methods=['POST'])
    def createLocation():
        data = request.get_json()
        table = "location"
        columns = "name"
        values = str(data['name'])

        obj = DB()
        id_row = obj.queryInsert(table, columns, values)
        return id_row
