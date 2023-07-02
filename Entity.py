class GymMember:
    def __init__(self, member_id, name, age, gender):
        self._member_id = member_id
        self._name = name
        self._age = age
        self._gender = gender


    @property
    def member_id(self):
        return self._member_id
    @member_id.setter
    def member_id(self, member_id):
        self._member_id = member_id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age

    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, gender):
        self._gender = gender