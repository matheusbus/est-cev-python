from person import Person
from database import Database
from repository import Repository

pessoa = Person(uuid=1, name='Maria', age=32)

db = Database()

pessoa_repo = Repository(db.connection)

pessoa_recuperada = pessoa_repo.findById(4)
if pessoa_recuperada:
    print(pessoa_recuperada.name)


people = pessoa_repo.findAll()
if people:
    for person in people:
        print(person)

print(db)