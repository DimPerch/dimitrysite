from flask import render_template, flash, redirect, url_for, request
from app import app
from .forms import TestForm

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/easytest", methods=["GET", "POST"])
def easytest_form():
    form = TestForm()
    if form.validate_on_submit():
        return redirect(url_for("easytest_result",
                                test=form.test.data,
                                name=form.name.data,
                                end_date=form.end_date.data,
                                time=form.time.data,
                                score=form.score.data))
    else:
        return render_template("easytest.html",
                               form=form)

            
@app.route("/easytest/result")
def easytest_result():
    data = dict(test=request.args.get("test"),
                name=request.args.get("name"),
                end_date=request.args.get("end_date"),
                time=request.args.get("time"),
                score=request.args.get("score"))
    return render_template("result.html", form=data)