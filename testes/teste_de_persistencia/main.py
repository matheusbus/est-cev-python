from person import Person
from database import Database
from repository import Repository

pessoa = Person(uuid=1, name='Maria', age=32)
db = Database()
pessoa_repo = Repository(db.connection)

def print_people():
    people = pessoa_repo.findAll()
    if people:
        for person in people:
            print(person)

def print_people_by_id(id):
    pessoa_recuperada = pessoa_repo.findById(id)
    if pessoa_recuperada:
        print(pessoa_recuperada.name)

print_people()
new_person = Person(6, 'Fabricio', 54)
pessoa_repo.save(new_person)
print_people()