import sqlite3

connection = sqlite3.connect('filmes.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS filmes (nome TEXT, Diretor TEXT, Ano INT)''')

connection.commit
connection.close