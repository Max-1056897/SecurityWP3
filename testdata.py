import sqlite3

conn = sqlite3.connect('aanwezigheidssysteem.db')

c = conn.cursor()

# c.execute("INSERT INTO leerlingen (naam, gebruikersnaam, wachtwoord, rooster) VALUES (?, ?, ?, ?)", ("David Coffa", "0994739", "admin", "rooster1"))
# c.execute("INSERT INTO leerlingen (naam, gebruikersnaam, wachtwoord, rooster) VALUES (?, ?, ?, ?)", ("Max Looij", "1056897", "admin", "rooster1"))
# c.execute("INSERT INTO leerlingen (naam, gebruikersnaam, wachtwoord, rooster) VALUES (?, ?, ?, ?)", ("Wesley", "12345", "admin", "rooster1"))

# c.execute("INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES (?, ?, ?)", ("Jelle van der Loo", "jellevanderloo", "admin"))
# c.execute("INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES (?, ?, ?)", ("Dana Mol", "danamol", "admin"))
# c.execute("INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES (?, ?, ?)", ("Gayatri Goyal", "gayatrigoyal", "admin"))
# c.execute("INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES (?, ?, ?)", ("Tjidde Maijer", "tjiddemaijer", "admin"))
# c.execute("INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES (?, ?, ?)", ("Bas van Rijswijk", "basvanrijswijk", "admin"))
# c.execute("INSERT INTO docenten (naam, gebruikersnaam, wachtwoord) VALUES (?, ?, ?)", ("Eva Schaap", "evaschaap", "admin"))


# c.execute("INSERT INTO lessen (vak, datum, starttijd, eindtijd, docent_id) VALUES (?, ?, ?, ?, ?)", ("Databases", "06-03-2023", "8:30", "11:20", 1))
# c.execute("INSERT INTO lessen (vak, datum, starttijd, eindtijd, docent_id) VALUES (?, ?, ?, ?, ?)", ("Studieloopbaancoaching", "06-03-2023", "11:20", "13:00", 1))
# c.execute("INSERT INTO lessen (vak, datum, starttijd, eindtijd, docent_id) VALUES (?, ?, ?, ?, ?)", ("Proffesionele vorming 2", "06-03-2023", "13:00", "15:50", 1))
# c.execute("INSERT INTO lessen (vak, datum, starttijd, eindtijd, docent_id) VALUES (?, ?, ?, ?, ?)", ("Studieloopbaancoaching", "06-03-2023", "11:20", "13:00", 1))
# c.execute("INSERT INTO lessen (vak, datum, starttijd, eindtijd, docent_id) VALUES (?, ?, ?, ?, ?)", ("User Experience", "07-03-2023", "11:20", "13:00", 1))
# c.execute("INSERT INTO lessen (vak, datum, starttijd, eindtijd, docent_id) VALUES (?, ?, ?, ?, ?)", ("Basis Wiskunde", "07-03-2023", "13:00", "14:40", 1))
# c.execute("INSERT INTO lessen (vak, datum, starttijd, eindtijd, docent_id) VALUES (?, ?, ?, ?, ?)", ("Werkplaats 3", "08-03-2023", "8:30", "16:40", 1))

# c.execute("INSERT INTO aanwezigheid (leerling_id, les_id, aanwezig, reden) VALUES (?, ?, ?, ?)", (1, 1, 1, None))
c.execute("INSERT INTO aanwezigheid (leerling_id, les_id, aanwezig, reden) VALUES (?, ?, ?, ?)", (2, 2, 2, "Ziek"))

conn.commit()
conn.close()

