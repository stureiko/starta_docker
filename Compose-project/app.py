from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime
import socket
from netifaces import interfaces, ifaddresses, AF_INET
import psycopg2
from psycopg2.extras import RealDictCursor
import json

app = Flask(__name__)

# Настройки подключения к базе данных MySQL
mysql_config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql',  # Имя сервиса MySQL в Docker Compose
    'database': 'testdb',
}

postgre_config = {
    'dbname': 'my_new_database',
    'user': 'postgres',
    'password': 'postgres_password',
    'host': 'postgres',  # Имя сервиса PostgreSQL в Docker Compose
    'port': '5432',
}

def get_ip():
    ip_addr = {}
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        if addresses != ['No IP addr']:
            ip_addr[ifaceName] = addresses
    return ip_addr

def mysql_query():
    try:
        # Подключение к базе данных MySQL
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor(dictionary=True)

        # Получение последней записи
        cursor.execute("SELECT * FROM `test_table` ORDER BY id DESC LIMIT 1")
        last_record = cursor.fetchone()
        if last_record is None:
            last_record = {}
        else:
            last_record

        now = datetime.now()
        ip_address = get_ip().__str__()
        cursor.execute(
                "INSERT INTO `test_table` (date_time, ip) VALUES (%s, %s)",
                (now.strftime('%Y-%m-%d %H:%M:%S'), ip_address)
            )
        conn.commit()

        cursor.close()
        conn.close()

        return last_record

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


def postgers_query():
    try:
        # Подключение к базе данных PostgreSQL
        conn = psycopg2.connect(**postgre_config)
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # Получение последней записи
        cursor.execute("SELECT * FROM test_table ORDER BY id DESC LIMIT 1")
        last_record = cursor.fetchone()
        if last_record is None:
            last_record = {}
        else:
            last_record  = json.dumps(last_record, default=str)

        now = datetime.now()
        ip_address = get_ip().__str__()
        cursor.execute(
                "INSERT INTO test_table (date_time, ip) VALUES (%s, %s)",
                (now.strftime('%Y-%m-%d %H:%M:%S'), ip_address)
            )
        conn.commit()

        cursor.close()
        conn.close()

        return last_record
    
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

@app.route('/', methods=['GET'])
def last_entry():
    mysql_response = mysql_query()
    postgre_response = postgers_query()

    return {"mysql": mysql_response, "postgre": postgre_response}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3256)
