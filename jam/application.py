from flask import Flask, request, render_template
app = Flask(__name__)

from helper import DB
from jam import app



class Application:

    @app.route("/application", methods=['GET'])
    def application():
        obj = Application()
        return obj.getApplication()

    def getApplication(self):
        table = "application"
        columns = "title, company, location, next_action"
        obj = DB()
        id_row, list_rows = obj.querySelect(table, columns)
        list_applications = []

        for row in list_rows:
            application = {}
            application['title'] = row[0]
            application['company'] = row[1]
            application['location'] = row[2]
            application['next_action'] = row[3]
            list_applications.append(application)
        print list_applications
        values = list_applications
        return render_template('applications.html', list_applications=values)


    @app.route("/application/create", methods=['POST'])
    def createApplication():
        print "insdie application create"
        table = "application"
        columns = ""
        values = ""

        dict_form_data = request.form
        for key in dict_form_data:
            columns = columns + "," + key
            values = values + "," + "'" + dict_form_data[key] + "'"
        columns = columns[1:]
        values = values[1:].strip()
        print values

        obj = DB()
        id_row = obj.queryInsert(table, columns, values)
        print id_row
        obj = Application()
        return obj.getApplication()



