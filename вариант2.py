class Person:

    name = str()
    surname = str()
    qualify = int()
    sex = str()

    def __init__(self, name, surname, qualify = 1, sex='male'):
        self.name = name
        self.surname = surname
        self.qualify = qualify
        self.sex = sex


    def prints(self):
        ls = [self.name, self.surname, str(self.qualify)]
        return str(' '.join(ls))

    def __del__(self):
        ls = [self.name, self.surname]

        if self.sex == 'male':
            text = "Мистр. "
        else:
            text = "Мисис. "

        print('Goodbye, ' + text + str(' '.join(ls)))

if __name__ == '__main__':
    a = Person("Иван", "Иванов", 20)
    b = Person("Никита", "Попов", 15)
    c = Person("Сара", "O'Connor", 100, "female")

print(a.prints())
print(b.prints())
print(c.prints())
del(b)
input('>')