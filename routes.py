from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import SignupForm, LoginForm

app = Flask(__name__)

# With the below line, Flask app is now connected to the Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@0.0.0.0:9092/learningflask'
db.init_app(app)  # Initialize this flask app for the database setup

app.secret_key = "development-key"  # To protect the form against Cross Site Request Forgery

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup", methods=['GET','POST'])
def signup():
    if 'email' in session:
        return redirect(url_for('home'))

    form = SignupForm()

    if request.method =="POST":
        # If any form fields are empty(means validation check returns false) and return false, the signup page shud be returned back to the user upon hitting Submit
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            #Create new user instance, and initialize it with data from signup form
            newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

#Once a new user is signed up for the app, it creates a new session and should then redirect to the homepage
            session['email'] = newuser.email
            return redirect(url_for('home'))

    elif request.method == "GET":
        return render_template('signup.html', form=form)

@app.route("/home")
def home():
    if 'email' not in session:
        return redirect(url_for('login'))

    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if 'email' in session:
        return redirect(url_for('home'))

    form = LoginForm()

    if request.method == "POST":
        if form.validate()==False:
            return render_template('login.html', form = form)
        else: # Fetch the user fields, compare with DB if user exists, if exists, login user creating a new session with email ID and redirect to homepage
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session['email'] = form.email.data
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))

    elif request.method =="GET":
        return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    # 1. delete the cookie
    session.pop('email', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
