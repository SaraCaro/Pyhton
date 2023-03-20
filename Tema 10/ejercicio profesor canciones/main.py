import sqlite3


from song import Song
from artist import Artist
from disc import Disc
from artistManager import ArtistManager
from discManager import DiscManager
from songManager import SongManager

conn = sqlite3.connect('./music.db')
# artista = Artist(conn, 6,'Camaron', 'España', '1950-12-05')
# artista.save()

# disco = Disc(conn, 7, 'Leyenda del Tiempo','1979-06-16','Universal')
# disco.save()
# print(disco)

# cancion = Song(conn, 9, 'Volando Voy', None,205,'Flamenco', artista, disco)
# cancion1 = Song(conn, 3)
# cancion2.delete()
# cancion1.load()
# print(cancion1)
# cancion.save()
# print(cancion)

# artista2 = Artist(conn, 3, 'Estopa', 'España')
# artista2 = Artist(conn, 3)
# artista2.load()
# artista2.save()
# artista2.reload()
# print(artista2.getId())
# print(artista2)


# MANAGER ARTIST
# manager = ArtistManager(conn)
# manager_ar = manager.getByIds(1,2,5)
# for element in manager_ar:
#     print(element)
# print(len(manager_ar))

# manager = ArtistManager(conn)
# manager_name = manager.getByName('e')
# for element in manager_name:
#     print(element)
# print(len(manager_name))

# manager = ArtistManager(conn)
# manager_ar = manager.getByNacionality('españa')
# for element in manager_ar:
#     print(element)
# print(len(manager_ar))

# manager = ArtistManager(conn)
# manager_ge = manager.getBySongType('pop')
# for element in manager_ge:
#     print(element)
# print(len(manager_ge))


# MANAGER DISCO

# manager = DiscManager(conn)
# manager_ti = manager.getByYear('1979')
# for element in manager_ti:
#     print(element)
# print(len(manager_ti))

manager = DiscManager(conn)
manager_ti = manager.getByTypes('Pop')
for element in manager_ti:
    print(element)
print(len(manager_ti))

# manager = DiscManager(conn)
# manager_ti = manager.getByArtistIds(2)
# for element in manager_ti:
#     print(element)
# print(len(manager_ti))



# MANAGER CANCION
# manager = SongManager(conn)
# songs = manager.getByIds(2,4,5)

# for element in songs:
#     print(element)

# song = manager.getByTitle('on')
# for element in song:
#     print(element)