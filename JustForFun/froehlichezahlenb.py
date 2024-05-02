import pyshark

file_path = r'C:\Users\MrXam\Documents\6.pcapng'
capture = pyshark.FileCapture(file_path)

# Dictionary zum Speichern der Daten für jede IP-Adresse
ip_data = {}

# Durchlaufen der Pakete in der Datei
for packet in capture:
    try:
        # Extrahieren der notwendigen Informationen
        src_ip = packet.ip.src
        packet_length = int(packet.length)
        timestamp = float(packet.sniff_timestamp)

        # Wenn die IP-Adresse bereits vorhanden ist, aktualisieren Sie die Daten
        if src_ip in ip_data:
            ip_data[src_ip]['total_bytes'] += packet_length
            ip_data[src_ip]['timestamps'].append(timestamp)
        else:
            # Neue IP-Adresse: Initialisieren der Daten
            ip_data[src_ip] = {'total_bytes': packet_length, 'timestamps': [timestamp]}
    except AttributeError:
        # Ignorieren von Paketen, die nicht die benötigten Attribute haben
        continue

# Berechnung der Datenrate für jede IP-Adresse und Gesamtbandbreite
total_bandwidth = 0
data_rates = {}

for ip, data in ip_data.items():
    total_time = max(data['timestamps']) - min(data['timestamps'])
    if total_time > 0:
        data_rate = (data['total_bytes'] / total_time) * 8 / 10**6  # Umrechnung in Mbit/s
    else:
        data_rate = 0
    data_rates[ip] = data_rate
    total_bandwidth += data_rate

# Sortierung nach Datenrate in absteigender Reihenfolge
sorted_data_rates = sorted(data_rates.items(), key=lambda x: x[1], reverse=True)

# Ausgabe der sortierten Datenraten
for ip, rate in sorted_data_rates:
    print(f"IP Adresse: {ip}, Datenrate: {rate:.2f} Mbit/Sekunde")

# Ausgabe der gesamten genutzten Bandbreite
print(f"Gesamte genutzte Bandbreite: {total_bandwidth:.2f} Mbit/Sekunde")
