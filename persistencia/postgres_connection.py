import psycopg2

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="teste_python",
            user="postgres",
            password='postgres',
            host='localhost'
        )

    def __str__(self):
        return super().__str__()

