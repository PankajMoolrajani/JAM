from flask import Flask, request
app = Flask(__name__)

from helper import DB
from jam import app



class Company:

    @app.route("/company/create", methods=['POST'])
    def createCompany():
        data = request.get_json()
        table = "company"
        columns = "name"
        values = str(data['name'])

        obj = DB()
        id_row = obj.queryInsert(table, columns, values)
        return id_row