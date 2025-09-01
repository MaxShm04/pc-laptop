import os
import shutil

# Pfade zu den Ordnern
master_folder = '/Volumes/T7/python/testPics'
second_folder = '/Volumes/T7/python/alrGallery'


# Hole alle Dateien im zweiten Ordner (der Ordner mit den bereits vorhandenen Bildern)
second_folder_files = set(os.listdir(second_folder))

# Durchlaufe alle Dateien im Master-Ordner
for filename in os.listdir(master_folder):
    # Überprüfen, ob die Datei im zweiten Ordner vorhanden ist
    if filename in second_folder_files:
        file_path = os.path.join(master_folder, filename)
        # Lösche die Datei, wenn sie im zweiten Ordner existiert
        os.remove(file_path)
        print(f"Die Datei {filename} wurde aus dem Master-Ordner gelöscht.")

