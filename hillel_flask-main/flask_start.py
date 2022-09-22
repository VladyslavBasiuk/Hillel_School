import time
from flask import Flask, request
from utils import get_currency_exchange_rate

app = Flask(__name__)


@app.route("/")
def request_example():
    return "<p>Request example: <br> http://127.0.0.1:5000/rates?date=01.12.2014&bank=NB&c1=UAH&c2=USD " \
           "<br> http://127.0.0.1:5000/rates?date=01.12.2014&bank=PB&c1=UAH&c2=USD " \
           "<br> You can specify the 'date=xx.xx.xxxx' parameter of your choice!</p>"


@app.route("/rates", methods=['GET'])
def get_rates():
    date = request.args.get('date', default='01.12.2014')
    bank = request.args.get('bank', default='NB')
    c1 = request.args.get('c1', default='UAH')
    c2 = request.args.get('c2', default='USD')
    result = get_currency_exchange_rate(date=date, bank=bank, c1=c1, c2=c2)
    return result
