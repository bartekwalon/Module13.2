import sqlite3


conn = sqlite3.connect("todo.db")

c = conn.cursor()

c.execute(
    """ CREATE TABLE todo (
   task_id int AUTO_INCREMENT,
   title text NOT NULL,
   description text NOT NULL,
   PRIMARY KEY (task_id)
)"""
)
