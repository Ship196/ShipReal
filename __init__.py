from flask import Flask, render_template, flash, request, url_for, redirect, session
from create_object import User_list, User, read, Profile
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
from functools import wraps

from dbconnect import connection
import gc

#TOPIC = Content()
TOPIC = "Big Dicks"

app = Flask(__name__)
app.secret_key = 'super secret key'

class RegistrationForm(Form):
        username = TextField('Username', [validators.Length(min=4, max=20)])
        email = TextField('Email Address', [validators.Length(min=6, max=50)])
        password = PasswordField('Password', [validators.Required(),
                                              validators.EqualTo('confirm', message="Passwords must match.")])
        confirm = PasswordField('Repeat Password')

        accept_tos = BooleanField('I accept the <a href="/tos/">Terms of Service</a> and the <a href="/privacy/">Privacy Notice</a> (Last updated never)', [validators.Required()])


@app.errorhandler(405)
def method_not_found(e):
        return render_template("405.html")

def login_required(f):
        @wraps(f)
        def wrap(*args, **kwargs):
                if 'logged_in' in session:
                        return f(*args, **kwargs)
                else:
                        flash("You need to login first!")
                        return redirect(url_for('login_page'))

        return wrap

@app.route('/', methods=["GET", "POST"])
def homepage():
	return render_template("index.html")

@app.route('/dashboard', methods=["GET", "POST"])
@login_required
def dashboard():
    #if request.method = "POST":
    #    new_val = User(())
    user_stuff, profile_stuff = read(session['email'])



    if request.method == "POST":
        profile_stuff.update_nickname(request.form['nickname'])
        #print(request.form['nickname'])
        profile_stuff.update_year(request.form['year'])
        profile_stuff.update_dorm(request.form['residencehall'])
        profile_stuff.update_gender(request.form['gender'])
        profile_stuff.update_interestedIn(request.form['horny'])
        profile_stuff.update_major(request.form['major'])
        profile_stuff.update_secondMajor(request.form['secondarymajor'])
        profile_stuff.update_minor(request.form['minor'])
        profile_stuff.update_location(request.form['spendtime'])
        profile_stuff.update_cityOrgin(request.form['city'])
        profile_stuff.update_stateOrigin(request.form['state'])
        profile_stuff.update_countryOrigin(request.form['country'])
        profile_stuff.update_music(request.form['music'])
        profile_stuff.update_eats(request.form['greenstreeteats'])
        profile_stuff.update_about(request.form['aboutme'])

        profile_stuff.update_profile()
        #c.execute("INSERT INTO users (firstname, lastname, email, birthday, password) VALUES (%s, %s, %s, %s, %s)",
        #(thwart(firstname), thwart(lastname), thwart(email), thwart(birthday), thwart(password)))
        #c.execute("INSERT INTO profile (nickname, year) values (%s, %s)", (thwart(nickname), thwart(year)))
        #conn.commit()
        print("This went well")
    return render_template("dashboard.html", TOPIC = TOPIC)

@app.errorhandler(404)
def page_not_found(e):
        return render_template("404.html")



@app.route("/logout")
@login_required
def logout():
        session.clear()
        flash("You have been logged out!")
        gc.collect()
        return redirect(url_for('dashboard'))


@app.route('/login', methods = ['GET', 'POST'])
def login_page():
        error = ''
        c, conn = connection()
        if request.method == "POST":
            data = c.execute("SELECT * FROM users WHERE email = '%s' " % (request.form["email"]))
            data = c.fetchone()[5]

            if sha256_crypt.verify(request.form['password'], data):
                session['logged_in'] = True
                session['email'] = request.form['email']

                flash("You are now logged in")
                return redirect(url_for("dashboard"))
            else:
                error = "Invaild credentials. Try again."
                return render_template("login.html", error = error)
            gc.collect()

        return render_template("login.html", error = error)

    #except Exception as e:
                #flash(e)
        #error = "Invaild credentials. Try again."
        #return render_template("login.html", error = error)


@app.route('/register', methods = ['GET', 'POST'])
def register_page():
    form = request.form
    print("Test")
    if request.method == "POST":
        #username = form.username.data
        firstname = form['firstname']
        lastname = form['lastname']
        email = form['email']
        birthday = form['birthday']
        password = sha256_crypt.encrypt((str(form['password'])))
        c, conn = connection()
        print("This is our print statement")
        print(firstname, lastname)
        x = c.execute("SELECT * FROM users WHERE email = (%s)",
        (email,))
        print("checks email")
        if int(x) > 0:
            flash("That email has already been taken, please choose another.")
            print("email Takken")
            return render_template("login.html", form = form)

        else:
            data = User((0,firstname, lastname, email, birthday, password))
            data.write()
            print("Come thus far****************************************************************************")
            flash("Thanks for registering!")
            c.close()
            conn.close()
            gc.collect()

            session['logged_in'] = True
            session['email'] = email
            return redirect(url_for('dashboard'))

    return render_template("dashboard.html", form = form)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/newsfeed")
def newsfeed_page():
    return render_template("newsfeed.html")

@app.route("/chat")
def chat_page():
    return render_template("chat.html")

@app.route("/create")
def create_page():
    return render_template("create.html")

if __name__ == "__main__":

    app.config['SESSION_TYPE'] = 'filesystem'


    app.debug = True
    app.run()
