from flask import Flask, render_template, send_file
from forms import ThreeBoxForm, BlockTimeForm

# Create the application.
APP = Flask(__name__)
APP.config['SECRET_KEY'] = "121r2h3oh23h45jh23l4"

habits_lst = []
blocks = []


@APP.route('/', methods=['get', 'post'])
def home():
    return render_template("home.html")


@APP.route('/habits', methods=['get', 'post'])
def habits():
    form = ThreeBoxForm()
    habits_lst.clear()
    if not (form.box1.data is None or form.box2.data is None or form.box3.data is None):
        habits_lst.extend([form.box1.data, form.box2.data, form.box3.data])
    return render_template("habits.html", form=form)


@APP.route('/blocktimes', methods=['GET', 'POST'])
def blocktimes():
    form = BlockTimeForm()
    blocks.clear()
    for field in form.fields:
        if not (field.begin.data is None or field.end.data is None or field.begin.data > field.end.data):
            # print(str(field.begin.data)[:-3])
            blocks.append((str(field.begin.data)[:-3], str(field.end.data)[:-3]))

    return render_template('blocktimes.html', form=form)


@APP.route('/style.css')
def serve_static():
    return send_file('templates/style.css')

if __name__ == '__main__':
    APP.debug = True
    APP.run()


