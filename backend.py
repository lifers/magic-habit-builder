from flask import Flask, render_template, session
from forms import ThreeBoxForm
from temp_main import get_blocking_times, generate_prompt, run_scraper, parse_answer

# Create the application.
APP = Flask(__name__)
APP.config['SECRET_KEY'] = "121r2h3oh23h45jh23l4"


# @APP.route('/', methods=['get', 'post'])
# def home():
#     # TODO: Implement the home page
#     pass
#

@APP.route('/habits', methods=['get', 'post'])  # TODO: Add hyperlink to habits "page"
# TODO: change route to #habits
def habit():
    form = ThreeBoxForm()
    if not (form.box1.data is None or form.box2.data is None or form.box3.data is None):
        session['habits'] = [form.box1.data, form.box2.data, form.box3.data]
    return render_template("habits.html", form=form)


if __name__ == '__main__':
    APP.debug = True
    APP.run()

