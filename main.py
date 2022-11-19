from flask import Flask, render_template, request
from scraper import main

app: Flask = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == "POST":
        url1 = request.form["url1"]
        url2 = request.form["url2"]
        main_result = main(url1, url2)
        return render_template("result.html",
                               name1=main_result[0],
                               name2=main_result[1],
                               course_list=main_result[2],
                               dups=main_result[3])
    if request.method == "GET":
        return render_template("index.html")
    else:
        return render_template("index.html")


app.run(host='0.0.0.0', port=81)