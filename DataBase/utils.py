import os
import sqlite3
from typing import List


def execute_query(query_sql: str) -> List:
    """
    Function to execute a request
    :param query_sql: request
    :return: query result
    """
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result


def unwrapper(records: List):
    """
    Function for displaying the result of query execution
    :param records: db response list
    """
    for record in records:
        return ' _|_ '.join(str(item) for item in record)


def get_filter_customers(city=None, state=None) -> List:
    """
    Returns customers filtered by city and state
    :param city: city of residence, string
    :param state: state of residence, string
    :return: list of clients
    """
    query_sql = '''
        SELECT *
          FROM customers
    '''
    if city and state:
        query_sql += f" WHERE City = '{city}' AND State = '{state}';"
    elif city:
        query_sql += f" WHERE City = '{city}';"
    elif state:
        query_sql += f" WHERE State = '{state}';"
    return execute_query(query_sql)


def get_unique_customers_by_sql() -> List:
    query_scl = '''
        SELECT FirstName, count(*) 
        FROM customers GROUP BY FirstName HAVING count(*);
    '''
    return execute_query(query_scl)


def get_total_orders():
    """
    Function for calculating the total cost of orders
    :return: String with value
    """
    db = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    query = '''
        SELECT SUM(UnitPrice*Quantity)
            FROM invoice_items
    '''
    cursor.execute(query)
    result = cursor.fetchone()[0]
    return float(result)
