from flask import Flask, request, render_template
from numerology import score, mini_score

app = Flask('app')


@app.route('/')
def get_values():
    return render_template("get_values.html")


@app.route('/results', methods=['POST', 'GET'])
def results():
    if request.method == "POST":
        firstname = request.form["firstname"]
        middlename = request.form["middlename"]
        lastname = request.form["lastname"]
        birthday = request.form["bday"]
        birthday = birthday.replace('-', "").replace('/', "")
        bday = birthday[:2]
        firstname_score = score(firstname)
        middlename_score = score(middlename)
        lastname_score = score(lastname)
        try:
          bday_score = mini_score(bday)
          birthday_score = mini_score(birthday)
        except TypeError:
          bday_score = 0
          birthday_score = 0
        final_score = score(firstname + middlename +lastname)
    return render_template("results.html", **locals())


app.run(host='0.0.0.0', port=8080)
