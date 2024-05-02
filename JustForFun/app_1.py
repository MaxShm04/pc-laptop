from __future__ import print_function  # In python 2.7
from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS
import sys
app = Flask(__name__)
CORS(app)
# Replace these values with your database connection info
config = {
    'user': 'jonas',
    'password': 'oaskidf32904324n#',
    'host': '185.197.251.229',
    'database': 'stock_db',
    'raise_on_warnings': True
}


@app.route('/get_data', methods=['GET'])
def get_data():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # replace 'your_table' with your actual table name
    query = "WITH data AS (SELECT *, ROW_NUMBER() OVER(PARTITION BY u_id ORDER BY timestamp DESC) AS rn FROM kursdaten) SELECT d.timestamp, d.u_id, d.aktienWert, u.name, d.rn FROM data d JOIN unternehmen u ON d.u_id = u.u_id WHERE d.rn= 1 or d.rn = 60;"
    cursor.execute(query)

    rows = cursor.fetchall()

    # Convert query to row dicts (optional)
    row_dicts = []
    for row in rows:
        row_dicts.append(dict(zip(cursor.column_names, row)))

    cursor.close()
    conn.close()

    return jsonify(row_dicts)


@app.route('/get_data_user', methods=['GET'])
def get_data_user():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    u_id = request.args.get('u_id')
    # replace 'your_table' with your actual table name
    query = f"WITH data AS (SELECT wl_id FROM watchlists w JOIN user u ON u.us_id = w.us_id WHERE u.us_id={u_id}), chartA AS (SELECT *, ROW_NUMBER() OVER (PARTITION BY u_id ORDER BY timestamp DESC) AS rn FROM kursdaten), chartI AS (SELECT *, ROW_NUMBER() OVER (PARTITION BY i_id ORDER BY timestamp DESC) AS rn FROM kursdatenIndex) SELECT cA.timestamp, wA.u_id, NULL AS i_id, cA.aktienWert AS wert, u.name AS name, data.wl_id, cA.rn FROM chartA cA JOIN watchlistAktie wA ON wA.u_id = cA.u_id JOIN data ON wA.wl_id = data.wl_id JOIN unternehmen u ON u.u_id = wA.u_id WHERE (cA.rn= 1 OR cA.rn=60) UNION SELECT cI.timestamp, NULL AS u_id, wI.i_id, cI.indexWert AS wert, i.name AS name, data.wl_id, cI.rn FROM chartI cI JOIN watchlistIndex wI ON wI.i_id = cI.i_id JOIN data ON wI.wl_id = data.wl_id JOIN indizes i ON i.i_id = wI.i_id WHERE cI.rn = 1 OR cI.rn = 60 ORDER BY u_id, i_id;"
    cursor.execute(query)

    rows = cursor.fetchall()

    # Convert query to row dicts (optional)
    row_dicts = []
    for row in rows:
        row_dicts.append(dict(zip(cursor.column_names, row)))

    cursor.close()
    conn.close()

    return jsonify(row_dicts)


@app.route('/get_laender', methods=['GET'])
def get_laender():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    query = "SELECT l.* FROM laender l"
    cursor.execute(query)

    rows = cursor.fetchall()

    # Convert query to row dicts (optional)
    row_dicts = []
    for row in rows:
        row_dicts.append(dict(zip(cursor.column_names, row)))

    cursor.close()
    conn.close()

    return jsonify(row_dicts)


@app.route('/get_data_main', methods=['GET'])
def get_data_main():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    query = "SELECT * FROM unternehmen"  # replace 'your_table' with your actual table name
    cursor.execute(query)

    rows = cursor.fetchall()

    # Convert query to row dicts (optional)
    row_dicts = []
    for row in rows:
        row_dicts.append(dict(zip(cursor.column_names, row)))

    cursor.close()
    conn.close()

    return jsonify(row_dicts)


@app.route('/get_unternehmen_info', methods=['GET'])
def get_unternehmen_info():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    u_id = request.args.get('u_id')
    query = f"SELECT * FROM unternehmen WHERE u_id = {u_id}"
    query2 = f"SELECT * FROM aktionaere JOIN aktionaereVerwaltung ON aktionaere.a_id = aktionaereVerwaltung.a_id WHERE u_id = {u_id}"
    cursor.execute(query)

    rows = cursor.fetchall()

    # Convert query to row dicts (optional)
    row_dicts = []
    for row in rows:
        row_dicts.append(dict(zip(cursor.column_names, row)))

    cursor.execute(query2)
    rows = cursor.fetchall()
    # Convert rows from the second query to row dicts and directly append them to "data" key
    data_dicts = []
    for row in rows:
        data_dicts.append(dict(zip(cursor.column_names, row)))

    cursor.close()
    conn.close()
    row_dicts[0]['data'] = data_dicts

    return jsonify(row_dicts)


@app.route('/get_unternehmen_kurs', methods=['GET'])
def get_unternehmen_kurs():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    u_id = request.args.get('u_id')
    query = f"SELECT k.aktienWert, k.timestamp FROM kursdaten k JOIN stock_db.unternehmen u on k.u_id = u.u_id WHERE u.u_id = {u_id} ORDER BY k.timestamp"
    cursor.execute(query)

    rows = cursor.fetchall()

    # Convert query to row dicts (optional)
    row_dicts = []
    for row in rows:
        row_dicts.append(dict(zip(cursor.column_names, row)))

    cursor.close()
    conn.close()

    return jsonify(row_dicts)


@app.route('/get_data_unternehmen', methods=['GET'])
def get_data_unternehmen():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    u_id = request.args.get('u_id')
    # replace 'your_table' with your actual table name
    query = f"SELECT k.* FROM stock_db.kursdaten k JOIN unternehmen u ON k.u_id = u.u_id WHERE u.u_id = {u_id}"
    cursor.execute(query)

    rows = cursor.fetchall()

    # Convert query to row dicts (optional)
    row_dicts = []
    for row in rows:
        row_dicts.append(dict(zip(cursor.column_names, row)))

    cursor.close()
    conn.close()

    return jsonify(row_dicts)


@app.route('/authenticate', methods=['POST'])
def login():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    username = request.form.get('username')
    password = request.form.get('password')

    # TODO: Form data set
    # replace 'your_table' with your actual table name
    query = f"SELECT * FROM user WHERE benutzername = '{username}' AND passwortHash = '{password}'"
    cursor.execute(query)

    rows = cursor.fetchall()

    # Convert query to row dicts (optional)
    row_dicts = []
    for row in rows:
        row_dicts.append(dict(zip(cursor.column_names, row)))

    cursor.close()
    conn.close()
    return jsonify(row_dicts)


@app.route('/get_unternehmen', methods=['GET'])
def get_unternehmen():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    land1 = request.args.get('land')
    query = f"SELECT u.* FROM unternehmen u JOIN stock_db.laender l on u.land = l.kuerzel WHERE land = '{land1}'"
    print(query)
    cursor.execute(query)

    rows = cursor.fetchall()

    # Convert query to row dicts (optional)
    row_dicts = []
    for row in rows:
        row_dicts.append(dict(zip(cursor.column_names, row)))

    cursor.close()
    conn.close()

    return jsonify(row_dicts)


if __name__ == '__main__':
    app.run(debug=True, host='185.197.251.229', port=5000)  # Runs on port 5000, accessible to any device on the network
