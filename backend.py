from flask import Flask, render_template
from forms import ThreeBoxForm

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


if __name__ == '__main__':
    APP.debug = True
    APP.run()


