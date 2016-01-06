from flask import Flask, render_template
app = Flask(__name__)

from jam import app



class Title:

    @app.route("/", methods=['GET'])
    def getDashboard():
        return render_template('index.html')






