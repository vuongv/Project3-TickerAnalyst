from flask import Flask, jsonify, render_template
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DECIMAL
import plotly 
import plotly.express as px
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/ticker'

db = SQLAlchemy(app)

class Ticker(db.Model):
    __tablename__ = 'Ticker'

    volume = db.Column(db.Integer, primary_key=True)
    volume_weighted_average_price = db.Column(DECIMAL(precision=10, scale=2))
    open_price = db.Column(DECIMAL(precision=10, scale=2))
    closing_price = db.Column(DECIMAL(precision=10, scale=2))
    day_highest = db.Column(DECIMAL(precision=10, scale=2))
    day_lowest = db.Column(DECIMAL(precision=10, scale=2))
    date = db.Column(db.Date)
    number_of_transactions = db.Column(db.Integer)

@app.route('/VolumeTrade')
def VolumeTrade():
    conn = psycopg2.connect("postgresql://postgres:admin@localhost:5432/ticker")
    cur = conn.cursor()
    cur.execute("SELECT \"Volume\" FROM \"Ticker\"")

    results= cur.fetchall()
    records = [ ]

    for row in results:
        records.append(float(row[0]))

    return records

@app.route('/VolumeWeightedAverage')
def VolumeWeightedAverage():
    conn = psycopg2.connect("postgresql://postgres:admin@localhost:5432/ticker")
    cur = conn.cursor()
    cur.execute("SELECT \"Volume_Weighted_Average_Price\" FROM \"Ticker\"")

    results= cur.fetchall()
    records = [ ]

    for row in results:
        records.append(float(row[0]))

    return records

@app.route('/OpenPrice')
def OpenPrice():
    conn = psycopg2.connect("postgresql://postgres:admin@localhost:5432/ticker")
    cur = conn.cursor()
    cur.execute("SELECT \"Open_Price\" FROM \"Ticker\"")

    results= cur.fetchall()
    records = [ ]

    for row in results:
        records.append(float(row[0]))

    return records

@app.route('/ClosingPrice')
def ClosingPrice():
    conn = psycopg2.connect("postgresql://postgres:admin@localhost:5432/ticker")
    cur = conn.cursor()
    cur.execute("SELECT \"Closing_Price\" FROM \"Ticker\"")

    results= cur.fetchall()
    records = [ ]

    for row in results:
        records.append(float(row[0]))

    return records

@app.route('/DayHighest')
def DayHighest():
    conn = psycopg2.connect("postgresql://postgres:admin@localhost:5432/ticker")
    cur = conn.cursor()
    cur.execute("SELECT \"Day_Highest\" FROM \"Ticker\"")

    results= cur.fetchall()
    records = [ ]

    for row in results:
        records.append(float(row[0]))

    return records

@app.route('/DayLowest')
def DayLowest():
    conn = psycopg2.connect("postgresql://postgres:admin@localhost:5432/ticker")
    cur = conn.cursor()
    cur.execute("SELECT \"Day_Lowest\" FROM \"Ticker\"")

    results= cur.fetchall()
    records = [ ]

    for row in results:
        records.append(float(row[0]))

    return records

@app.route('/Date')
def Date():
    conn = psycopg2.connect("postgresql://postgres:admin@localhost:5432/ticker")
    cur = conn.cursor()
    cur.execute("SELECT \"Date\" FROM \"Ticker\"")

    results= cur.fetchall()
    records = [ ]

    for row in results:
        records.append((row[0]))

    return records

@app.route('/NumberOfTransaction')
def NumberOfTransaction():
    conn = psycopg2.connect("postgresql://postgres:admin@localhost:5432/ticker")
    cur = conn.cursor()
    cur.execute("SELECT \"Number_of_Transaction\" FROM \"Ticker\"")

    results= cur.fetchall()
    records = [ ]

    for row in results:
        records.append(float(row[0]))

    return records

@app.route('/VolumeChart')
def VolumeChart():
    conn = psycopg2.connect("postgresql://postgres:admin@localhost:5432/ticker")
    cur1 = conn.cursor()
    cur2 = conn.cursor()
    cur1.execute("SELECT \"Volume\" FROM \"Ticker\"")

    VolumeResults= cur1.fetchall()
    VolumeRecords = [ ]

    for row in VolumeResults:
        VolumeRecords.append(float(row[0]))

    cur2.execute("SELECT \"Date\" FROM \"Ticker\"")
    DateResult = cur2.fetchall()
    DateRecords = []

    for row in DateResult:
        DateRecords.append(row[0])

    data = [
        plotly.graph_objs.Bar(
            x=DateRecords,
            y=VolumeRecords
        )
    ]

    layout = plotly.graph_objs.Layout(
        title='Volume Trade',
        xaxis=dict(title="Date"),
        yaxis=dict(Title="Volume")
    )

    fig = plotly.graph_objs.Figure(data=data, layout=layout)

    return render_template('index.html', graphJSON=fig.to_json())

if __name__ == "__main__":
  app.run()