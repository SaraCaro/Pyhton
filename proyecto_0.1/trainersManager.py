from trainers import Trainers

class TrainerManager:
    '''
    Gestiona los objetos de la clase Trainers en la base de datos.
    '''
    
    def __init__(self, connection):
        self.__connection = connection
        self.__cursor = connection.cursor()


    def get_all_saved_trainers(self):
        sql = 'SELECT id, nombre, phone '
        sql += 'FROM trainers'
        self.__cursor.execute(sql)
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            trainer = Trainers(
                self.__connection, 
                row[0], 
                row[1],
                row[2]
            )
            result.add(trainer)
            
        return result
