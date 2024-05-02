from datetime import time

import mysql.connector
from flask import Flask, jsonify
import random
config = {
    'user': 'jonas',
    'password': 'oaskidf32904324n#',
    'host': '185.197.251.229',
    'database': 'stock_db',
    'raise_on_warnings': True
}

def get_data_unternehmenIndex(cursor, i_id):  # get data from each unternehmen in certain index
    cursor.execute(
        f"WITH data AS (SELECT *, ROW_NUMBER() OVER(PARTITION BY u_id ORDER BY timestamp DESC) AS rn FROM kursdaten) SELECT d.timestamp, d.u_id, d.aktienWert, u.name, d.rn, u.anteileGesamt FROM data d JOIN unternehmen u ON d.u_id = u.u_id JOIN indexVerwaltung iV ON d.u_id = iV.u_id WHERE d.rn= 1 AND iV.i_id = {i_id} ORDER BY u.u_id;")
    rows = cursor.fetchall()
    print(rows)
    return rows


def get_data_Index(cursor):  # last data from each index
    cursor.execute(
        "WITH data AS (SELECT *, ROW_NUMBER() OVER(PARTITION BY i_id ORDER BY timestamp DESC) AS rn FROM kursdatenIndex) SELECT d.i_id, d.indexWert FROM data d JOIN indizes i ON d.i_id = i.i_id WHERE d.rn= 1;")
    rows = cursor.fetchall()
    print(rows)
    return rows


def generate_new_stock_value(cursor, i_id):
    data = get_data_unternehmenIndex(cursor, i_id)
    values = []
    sum_cap = 0
    out = 0
    for u_id, i in data:
        if u_id[4] == 2:
            value_old = u_id[2]
            if data[i - 1][4] == 2:  # corrupt data, only one dataset available, need 2
                print(f"corrupt data, {u_id[1]}")
                continue
            value_current = data[i - 1][2]
            diff = (value_current - value_old) / value_old  # relative difference
            cap = value_current * u_id[5]
            values.append([diff, cap])
            sum_cap += cap

    for u in values: # calculating weighted average
        weighting_factor = (u[1] / sum_cap) * u[0]
        out += weighting_factor

    return out

def insert_data(cursor, i_id, gen):
    # Erstellen Sie hier Ihre INSERT-Anweisung. Zum Beispiel:
    query = f"INSERT INTO kursdatenIndex(indexWert, i_id) VALUES ({gen}, {i_id})"
    print(query)
    cursor.execute(query)


def main(config):
    # Eine Verbindung zur Datenbank herstellen
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    try:
        while True:  # Das sorgt für eine Endlosschleife
            # Daten abrufen
            data = get_data_Index(cursor)
            print(data)
            # Führen Sie für jede u_id die Daten ein
            for i_id in data:  # for each index
                # print(u_id[1])
                gen = generate_new_stock_value(cursor, i_id[0])
                insert_data(cursor, i_id[0], gen)  # u_id[0], da jede u_id ein Tupel ist

            # Wichtig: Commit nach dem Einfügen, um sicherzustellen, dass die Daten gespeichert werden
            conn.commit()

            # Warte für 1 Sekunde
            time.sleep(1)

    except KeyboardInterrupt:
        # Benutzer hat manuell beendet, schließen Sie sauber
        print("Prozess durch Benutzer beendet.")

    except Exception as e:
        # Bei einer anderen Art von Fehler
        print(f"Ein Fehler ist aufgetreten: {e}")

    finally:
        cursor.close()
        conn.close()

    cursor.close()
    conn.close()


main(config)
