import os
import pymysql
from urllib.request import urlopen
import requests

db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}

def get_user_input():
    user_input = input('Enter your name: ')
    return user_input

def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')

def get_data():
    """
    A02:2021 - Cryptographic Failures Fix
    - Uses HTTPS for secure encrypted communication.
    - Verifies server cerftificates (verify=True by default).
    - Adds timeout and error handling.
    """
    url = 'https://secure-api.com/get-data'   # Fixed: changed to HTTPS
    
    try:
        response = requests.get(url, timeout=5)  # verifies SSL certs by default
        response.raise_for_status()
        return response.text  # or response.json() if the API returns JSON
    except requests.exceptions.SSLError:
        print("SSL certificate verification failed. Connection not secure.")
    except requests.exceptions.RequestException as e:
        print("Error fetching data securely:", e)
    return data

def save_to_db(data):
    query = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"   # Fix: Use parameterized queries to prevent SQL injection
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query, (data, 'Another Value'))   # safely pass parameters
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
