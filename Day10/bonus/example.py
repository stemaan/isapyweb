class Client:
    def __init__(self, firstname, lastname, *args, **kwargs):
        self.firstname = firstname
        self.lastname = lastname
        print(args)
        print(kwargs)

    @classmethod
    def from_json(cls, data):
        return cls(**data)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


if __name__ == '__main__':
    something = {'firstname': 'jan', 'lastname': 'kowalski', 'age': 40}
    something2 = ['jan', 'kowalski', '40']
    person = Client(**something)
    print(person)
    print('*' * 80)
    person2 = Client(*something2)
    print(person2)
    print('*' * 80)
    person3 = Client.from_json(something)
    print(person3)
    some_data = {'1': 'abc', '2': 'def'}
    person4 = Client.from_json(**some_data)
    print(person4)
