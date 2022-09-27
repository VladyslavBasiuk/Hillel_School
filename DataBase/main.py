from flask import Flask, request
from utils import unwrapper, get_filter_customers, get_unique_customers_by_sql, get_total_orders

app = Flask(__name__)


@app.route('/')
def home():
    return '<p><b>Example:</b><br><b>http://127.0.0.1:5000/filter</b>' \
           '<br><b>http://127.0.0.1:5000/filter?city=Boston&state=MA</b>' \
           '<br><b>http://127.0.0.1:5000/firstname</b>' \
           '<br><b>http://127.0.0.1:5000/total_orders</b></p>'


@app.route('/filter')
def filters():
    city = request.args.get('city', default='Boston')
    state = request.args.get('state', default='MA')
    return f'{unwrapper(get_filter_customers(city, state))}'


@app.route('/firstname')
def firstname():
    """
        Function to display usernames and the number of repetitions
        :return: List with names and number of repetitions
    """
    return f"""
        <xmp>
            {get_unique_customers_by_sql()}
        </xmp>
    """


@app.route('/total_orders')
def total_orders():
    return f'Earnings = {get_total_orders()}'


if __name__ == '__main__':
    app.run(debug=True)
