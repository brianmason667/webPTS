import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
    except Error as err:
        return connection
connection = create_server_connection("localhost", "root", "Good2goo")

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except Error as err:
    
    create_database_query = "CREATE DATABASE school"
    create_database(connection, create_database_query)
    
def application(environ,start_response):
    status = '200 OK'
    html = '<html>\n' \
           '<body>\n' \
           '<div style="width: 100%; font-size: 50px; font-weight: bold; text-align: center;">\n' \
           'testing wsgi2 \n' \
           '</div>\n' \
           '</body>\n' \
           '</html>\n'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    return [html]