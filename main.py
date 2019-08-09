from flask import Flask, request, render_template
from numerology import score, mini_score

app = Flask("app")


@app.route("/")
def get_values():
    return render_template("get_values.html")


@app.route("/results", methods=["POST", "GET"])
def results():
    if request.method == "POST":
        try:
            firstname = request.form["firstname"]
            firstname_score = score(firstname)
        except:
            firstname = ""
            firstname_score = 0

        try:
            middlename = request.form["middlename"]
            middlename_score = score(middlename)
        except:
            middlename = ""
            middlename_score = 0

        try:
            lastname = request.form["lastname"]
            lastname_score = score(lastname)
        except:
            lastname = ""
            lastname_score = 0

        try:
            birthday = request.form["bday"]
            birthday = birthday.replace("-", "").replace("/", "")
            bday = birthday[:2]
            bday_score = mini_score(bday)
            birthday_score = mini_score(birthday)
        except:
            bday_score = 0
            birthday_score = 0

        final_score = score(firstname + middlename + lastname)
    return render_template("results.html", **locals())


app.run(host="0.0.0.0", port=8080)
