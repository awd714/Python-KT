class User:
    count = 0

    def __init__(self, name, login, password, grade):
        self._name = name
        self._login = login
        self._password = password
        self.__grade = grade

        if type(self) == User:
            User.count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        print('Невозможно изменить логин!')

    @property
    def password(self):
        return '********'

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def grade(self):
        return 'Неизвестное свойство grade'

    @grade.setter
    def grade(self, value):
        print('Неизвестное свойство grade')

    def showInfo(self):
        print(f'Name: {self.name}, Login: {self.login}')

    def show_info(self):
        self.showInfo()

    def eq(self, user):
        return self.__grade == user.__grade

    def lt(self, user):
        return self.__grade < user.__grade

    def gt(self, user):
        return self.__grade > user.__grade

    def __eq__(self, user):
        return self.eq(user)

    def __lt__(self, user):
        return self.lt(user)

    def __gt__(self, user):
        return self.gt(user)


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role, grade):
        super().__init__(name, login, password, grade)
        self._role = role
        SuperUser.count += 1

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def show_info(self):
        print(f'Name: {self.name}, Login: {self.login}, Role: {self.role}')

    def showInfo(self):
        self.show_info()


user1 = User('Paul McCartney', 'paul', '1234', 3)
user2 = User('George Harrison', 'george', '5678', 2)
user3 = User('Richard Starkey', 'ringo', '8523', 3)

admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)


user1.show_info()
admin.show_info()


users = User.count
admins = SuperUser.count

print(f'Всего обычных пользователей: {users}')
print(f'Всего супер-пользователей: {admins}')


print(user1 < user2)
print(admin > user3)
print(user1 == user3)


user3.name = 'Ringo Starr'
user1.password = 'Pa$$w0rd'

print(user3.name)
print(user2.password)
print(user2.login)

user2.login = 'geo'

print(user1.grade)
admin.grade = 10
