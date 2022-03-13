import sqlite3

connection = sqlite3.connect('filmes.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS filmes (nome TEXT, Diretor TEXT, Ano INT)''')

filmesData = [('Pulp Fiction', 'Quentin Tarantino', 1994),
('Back to the future', 'Steven Spielberg', 1985),
('Avengers', 'Marvel', 2014)]

cursor.executemany('Insert INTO filmes VALUES (?,?,?)', filmesData)

#valores = cursor.execute("SELECT * from filmes")

anoLancamento = (2014,)

#print(cursor.fetchall())
cursor.execute("SELECT * FROM filmes WHERE ano=?", anoLancamento)

print(cursor.fetchall())

connection.commit
connection.close