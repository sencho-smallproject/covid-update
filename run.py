import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/covid')
def covid():
    source = requests.get('https://www.stlouis-mo.gov/customcf/endpoints/covid-19/cases-deaths-rnaught.cfm?format=json')
    json_data = source.json()
    return render_template('covid.html', datas=json_data)


app.run(debug=True)
