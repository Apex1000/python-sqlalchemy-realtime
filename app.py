from flask import Flask, request, jsonify, render_template, redirect,flash, redirect,url_for,session,logging,request
import pusher
from database import db_session
from models import User,Users,Bids,User_bids
from datetime import datetime
import os
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)
app.secret_key = "any_random_string’"

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('index'))
    return wrap


@app.route("/home")
@is_logged_in
def home():
    flights = Bids.query.all()
    return render_template('index.html', flights=flights)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['uname']
        email = request.form['mail']
        password = request.form['passw']

        register = User(name,email,password)
        db_session.add(register)
        db_session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('index'))
    return wrap


@app.route('/',methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        
        login = User.query.filter_by(name=uname, password=passw).first()
        if login is not None:
            session['uname'] = request.form["uname"]
            session['logged_in'] = True
            return redirect(url_for("home"))
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/backend', methods=["POST", "GET"])
def backend():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        phone = request.form['phone']
        coine = request.form['coine']
        password = request.form["password"]

        new_flight = Users(name,username,phone,coine,password)
        db_session.add(new_flight)
        db_session.commit()

        
        return redirect("/backend", code=302)
    else:
        flights = Users.query.all()
        print (flights)
        return render_template('backend.html', flights=flights)

@app.route('/edit/<int:id>', methods=["POST", "GET"])
def update_record(id):
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        phone = request.form["phone"]
        coine = request.form["coine"]
        password = request.form["password"]

        update_flight = Users.query.get(id)
        update_flight.name = name
        update_flight.username = username
        update_flight.phone = phone
        update_flight.coine = coine
        update_flight.password = password

        db_session.commit()

       
        return redirect("/backend", code=302)
    else:
        new_flight = Users.query.get(id)
        new_flight.name = new_flight.name
        new_flight.username = new_flight.username

        return render_template('update_flight.html', data=new_flight)

@app.route('/bid', methods=["POST", "GET"])
def bid():
    if request.method == "POST":
        team1 = request.form["team1"]
        team2 = request.form["team2"]
        rate = request.form['rate']
        baaw1 = request.form['baaw1']
        baaw2 = request.form["baaw2"]

        new_flight = Bids(team1,team2,rate,baaw1,baaw2)
        db_session.add(new_flight)
        db_session.commit()

        
        return redirect("/bid", code=302)
    else:
        flights = Bids.query.all()
        print (flights)
        return render_template('bid.html', flights=flights)

@app.route('/bid/edit/<int:id>', methods=["POST", "GET"])
def update_bid(id):
    if request.method == "POST":
        name = request.form["team1"]
        username = request.form["team2"]
        phone = request.form["rate"]
        coine = request.form["baaw1"]
        password = request.form["baaw2"]

        update_flight = Bids.query.get(id)
        update_flight.bids_team1 = name
        update_flight.bids_team2 = username
        update_flight.rate = phone
        update_flight.baaw_team1 = coine
        update_flight.baaw_team2 = password

        db_session.commit()

       
        return redirect("/bid", code=302)
    else:
        new_flight = Bids.query.get(id)
        new_flight.bids_team1 = new_flight.bids_team1
        new_flight.bids_team2 = new_flight.bids_team2

        return render_template('update_bids.html', data=new_flight)

@app.route('/place_bid/<int:id>', methods=["POST", "GET"])
def place_bid(id):
    if request.method == "POST":
        name = request.form["team1"]
        username = request.form["team2"]
        phone = request.form["rate"]
        coine = request.form["baaw1"]
        password = request.form["baaw2"]

        update_flight = Bids.query.get(id)
        update_flight.bids_team1 = name
        update_flight.bids_team2 = username
        update_flight.rate = phone
        update_flight.baaw_team1 = coine
        update_flight.baaw_team2 = password

        db_session.commit()

       
        return redirect("/", code=302)
    else:
        new_flight = Bids.query.get(id)
        new_flight.bids_team1 = new_flight.bids_team1
        new_flight.bids_team2 = new_flight.bids_team2

        return render_template('place_bid.html', data=new_flight)

# run Flask app
if __name__ == "__main__":
    app.run(debug=True)