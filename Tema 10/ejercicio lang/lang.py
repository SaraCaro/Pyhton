import sqlite3

conn = sqlite3.connect("./lang.db")
cur = conn.cursor()

# # cur.execute("INSERT INTO movies (title,director,duration) VALUES (?,?,?)",("Gladiator","Ridley Scott",155))
# # cur.executemany("INSERT INTO movies (title,director,duration) VALUES (?,?,?)",
# # [("La vita e bella","Roberto Benigni",116),
# # ("Todo sobre mi madre","Pedro Almodovar",101)])
# # conn.commit()

# user = input("Escriba una pelicula: ")
# query = "SELECT title,director,duration FROM movies WHERE title='%s'"
# result = cur.executescript(query % user)
# row = cur.fetchall()
# print(row)
# conn.close()