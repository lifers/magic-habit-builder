from flask import Flask, redirect, url_for, render_template, session
from forms import ThreeBoxForm
import main as mn

# Create the application.
APP = Flask(__name__)
APP.config['SECRET_KEY'] = "121r2h3oh23h45jh23l4"


@APP.route('/', methods=['get', 'post'])
def home():
    form = ThreeBoxForm()
    print(form.box1.data)
    print(form.box2.data)
    print(form.box3.data)
    print(form.date.data)
    return render_template("home.html", form=form)


@APP.route('/result', methods=['get', 'post'])
def result():
    if "habits" in session and "schedule" in session:
        habits = session["habits"]
        schedule = session["schedule"]
        prompt = mn.generate_prompt(habits, schedule)
        reply = mn.run_scraper(prompt)
        raw_res = mn.parse_answer(reply)
        res = raw_res
        return f"{res}"
    elif "schedule" not in session:
        return redirect(url_for(""))
    elif "habits" not in session:
        return redirect(url_for(""))
    else:
        return redirect(url_for("home"))


if __name__ == '__main__':
    APP.debug = True
    APP.run()


