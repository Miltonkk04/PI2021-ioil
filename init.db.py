import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Giovaneti', 'Rua dos Alecrins 33 Centro')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Bar do Ze', 'Rua Uirapuru 60 Jardim America')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Mercado Real', 'Rua Jequetibas 12 Chapadão')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Padaria Pao Fresco', 'Rua do Sol Nascente 33 Jardim Brasil')
            )

connection.commit()
connection.close()