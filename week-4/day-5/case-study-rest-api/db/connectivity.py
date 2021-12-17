import pymysql


class Connectivity:
    def __init__(self):
        self.db = None
        try:
            self.db = pymysql.connect(
                host="localhost",
                user="root",
                password="password",
                database="bankcasestudydb",
                cursorclass=pymysql.cursors.DictCursor
            )
            print('----- DB Connected Successfully -----')
        except:
            print('Your credentials are wrong')
            self.db = None
