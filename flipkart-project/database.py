import mysql.connector
import sys
class ap:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hit-db-demo"
            )

            self.mycursor = self.conn.cursor()
            

        except:
            print("Some error:")
            sys.exit(1000);
        else:
            print("Connected to database")
    
    def registor(self, name, email, password):
        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`id`, `name`, `email`, `password`) 
             VALUES (NULL, '{}', '{}', '{}')""".format(name, email, password))
            self.conn.commit()
        except:
             return -1
        else:
           return 1
    def search(self,email,password):
        self.mycursor.execute("""
        select * from users whrer email like '{}'and password 
        like '{}'""".format(email,password));
        data=self.mycursor.fetchall()
        return data;