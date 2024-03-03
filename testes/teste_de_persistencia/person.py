class Person:
    uuid: int
    name: str
    age: int

    def __init__(self, uuid, name, age):
        self.id = uuid
        self.name = name
        self.age = age

    def __str__(self):
        return f"Pessoa(nome='{self.name}', idade={self.age})"
