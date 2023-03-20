from itertools import count
from multiprocessing.sharedctypes import Value
import sqlite3

class MyAvg:
    def __init__(self):
        self.count = 0
        self.registro = 0
    
    def step(self,value):
        self.count += value
        self.registro += 1
    
    def finalize(self):
        self.count = self.count / self.registro
        return self.count

con = sqlite3.connect("./lang.db")
con.create_aggregate("myavg", 1, MyAvg)
cur = con.cursor()
cur.execute("SELECT myavg(duration) FROM movies")
print(cur.fetchone()[0])
