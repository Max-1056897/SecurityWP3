# import json
# import sqlite3

# def update_json_from_database():

#     # Open the JSON file and load its contents
#     with open('lessen.json') as f:
#         data = json.load(f)

#     # Connect to the SQLite database
#     conn = sqlite3.connect('aanwezigheidssysteem.db')
#     c = conn.cursor()

#     # Iterate over each lesson in the JSON data
#     for lessen in data:
#         les_id = lessen['les_id']
#         vak = lessen['vak']
#         datum = lessen['datum']
#         starttijd = lessen['starttijd']
#         eindtijd = lessen['eindtijd']
#         docent_id = lessen['docent_id']

#         # Replace the lesson into the "lessen" table if it already exists
#         c.execute('INSERT OR IGNORE INTO lessen (les_id, vak, datum, starttijd, eindtijd, docent_id) VALUES (?, ?, ?, ?, ?, ?)',
#                 (les_id, vak, datum, starttijd, eindtijd, docent_id))
#     # Commit the transaction and close the database connection
#     # conn.commit()
#     # conn.close()


#         # Open the JSON file and load its contents
#     with open('lessen.json') as f:
#         data = json.load(f)

#     # Connect to the SQLite database
#     conn = sqlite3.connect('aanwezigheidssysteem.db')
#     c = conn.cursor()

#     # Iterate over each lesson in the JSON data
#     for lessen in data:
#         les_id = lessen['les_id']
#         vak = lessen['vak']
#         datum = lessen['datum']
#         starttijd = lessen['starttijd']
#         eindtijd = lessen['eindtijd']
#         docent_id = lessen['docent_id']

#         # Check if the lesson already exists in the "lessen" table
#         c.execute('SELECT les_id FROM lessen WHERE les_id = ?', (les_id,))
#         existing_lessen = c.fetchone()

#         # If the lesson already exists, update the existing row
#         if existing_lessen:
#             c.execute('UPDATE lessen SET vak = ?, datum = ?, starttijd = ?, eindtijd = ?, docent_id = ? WHERE les_id = ?',
#                     (vak, datum, starttijd, eindtijd, docent_id, les_id))
#         # If the lesson doesn't exist, insert a new row
#         else:
#             c.execute('INSERT INTO lessen (les_id, vak, datum, starttijd, eindtijd, docent_id) VALUES (?, ?, ?, ?, ?, ?)',
#                     (les_id, vak, datum, starttijd, eindtijd, docent_id))

#     # Commit the transaction and close the database connection
#     conn.commit()
#     conn.close()
