from person import Person
import psycopg2

class Repository:
    def __init__(self, connection):
        self.connection = connection

    def save(self, person):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO tb_person (id, nome, age) VALUES (%s, %s, %s)', (person.uuid, person.name, person.age))
        self.connection.commit()
        cursor.close()

    def findById(self, uuid):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM tb_person WHERE id = %s', (uuid,))
        person_fetched = cursor.fetchone()
        cursor.close()
        if person_fetched:
            return Person(uuid=person_fetched[0], name=person_fetched[1], age=person_fetched[2])
        return None

    def findAll(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM tb_person')
        data = cursor.fetchall()
        people = []
        for tuple in data:
            people.append(Person(uuid=tuple[0], name=tuple[1], age=tuple[2]))
        return people