from distutils.log import debug
import email
from unicodedata import name
from flask import Flask, redirect, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from pandas import read_parquet
import csv
import os
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class addData(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    city = db.Column(db.String(50), nullable=True)
    date = db.Column(db.String, nullable=True)
    time = date = db.Column(db.String, nullable=True)
    place = date = db.Column(db.String, nullable=True)
    name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(10), nullable=True)
    email = db.Column(db.String(200), nullable=True)        
    opening = db.Column(db.String(800), nullable=False)
    opening_comments = db.Column(db.String(800), nullable=True)
    route = db.Column(db.String(800), nullable=False)
    route_comments = db.Column(db.String(800), nullable=True)
    closing = db.Column(db.String(800), nullable=False)
    closing_comments = db.Column(db.String(800), nullable=True)
    special_area = db.Column(db.String(800), nullable=False)
    special_area_comments = db.Column(db.String(800), nullable=True)
    other_events = db.Column(db.String(800), nullable=True)

    def __repr__(self):
        return '<%r>' % self.id  

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = addData.query.filter_by(city = request.form['city']).all()
        # data = addData.query.order_by(addData.name).all()
        return render_template('index.html', data=data)
    else:
        data = ""
        return render_template('index.html', data=data)

@app.route('/add', methods=['POST', 'GET'])
def add():    
    if request.method == 'POST':   
        new_data = addData(
            city = request.form['city'],
            date = request.form['date'],
            time = request.form['time'],
            place = request.form['place'],
            phone = request.form['phone'],
            email = request.form['email'],
            name = request.form['name'],
            # Comments
            opening_comments = request.form['opening_comments'],
            closing_comments = request.form['closing_comments'],     
        )

        try:            
            db.create_all()   
            db.session.add(new_data)
            db.session.commit()
            print(request.form.getlist('cbClosingSpecialArea'))
            return redirect('/')
        except Exception as e:
            print(e)

    else:
        return render_template('add.html')
if __name__ == "__main__":
    app.run(debug=True)