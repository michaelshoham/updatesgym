class GymMember:

    def __init__(self, name, member_id, age, gender, phone_num, email):
        self._name = name
        self._member_id = member_id
        self._age = age
        self._gender = gender
        self._phone_num = phone_num
        self._email = email

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if name != "":
            self._name = name
        else:
            print("Name cannot be empty!")
    @property
    def member_id(self):
        return self._member_id
    @member_id.setter
    def member_id(self, member_id):
        if member_id != "":
            self._member_id = member_id
        else:
            print("Member ID cannot be empty!")

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if age != "":
            self._age = age
        else:
            print("Age cannot be empty!")

    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, gender):
        if gender != "":
            self._gender = gender
        else:
            print("Gender cannot be empty!")

    @property
    def phone_num(self):
        return self._phone_num
    @phone_num.setter
    def phone_num(self, phone_num):
        if phone_num != "":
            self._phone_num = phone_num
        else:
            print("Phone number cannot be empty!")

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        if email != "":
            self._email = email
        else:
            print("Email cannot be empty!")

    def print_member_info(self):
        print(f"Name: {self._name} \nMember ID: {self._member_id}"
              f"\nAge: {self._age} \nGender: {self._gender}"
              f"\nPhone number: {self._phone_num} \nEmail: {self._email}")
    