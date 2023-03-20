import sqlite3


from song import Song
from artist import Artist
from disc import Disc

conn = sqlite3.connect('./music.db')
artista = Artist(conn, 6,'Camaron', 'España', '1950-12-05')
artista.save()

disco = Disc(conn, 7, 'Leyenda del Tiempo','1979-06-16','Universal')
disco.save()

cancion = Song(conn, 9, 'Volando Voy', None,205,'Flamenco', artista, disco)
cancion.save()

