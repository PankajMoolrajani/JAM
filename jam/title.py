from flask import Flask, request, render_template
app = Flask(__name__)

from helper import DB
from jam import app

import json


class Title:

    @app.route("/title", methods=['GET'])
    def title():
        obj = Title()
        return obj.getTitle()

    def getTitle(self):
        table = "title"
        columns = "name"
        obj = DB()
        id_row, list_rows = obj.querySelect(table, columns)
        list_titles = []
        for title in list_rows:
            list_titles.append(title[0])
        print list_titles
        values = list_titles
        return render_template('titles.html', list_titles=values)

    @app.route("/title/create", methods=['POST'])
    def createTitle():
        table = "title"
        columns = "name"
        values = request.form['textbox-title']
        print values
        obj = DB()
        id_row = obj.queryInsert(table, columns, values)
        print id_row
        obj = Title()
        return obj.getTitle()
        #return render_template('titles.html', title=values)

    @app.route("/test", methods=['GET'])
    def createTest():

        title = "AppSec Engineer"
        return render_template('titles.html', title=title)





