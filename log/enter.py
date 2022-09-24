import json
import hashlib


class User_lib:
    def __init__(self, iin, name, surname, age, hashed_password):
        self.iin = iin
        self.name = name
        self.surname = surname
        self.age = age
        self.hashed_password = hashed_password
        #creates a library with user data referring to exactly that attribute(private) in the function
        self._user_dict = {"IIN": self._iin, "name": self._name,
                           "surname": self._surname, "age": self._age, "hashed_password": self._hashed_password}
    #they use encapsulation so that the user does not have direct access to the attributes, so I use getter and setter
    @property
    def iin(cls):
        return cls._iin

    # they use encapsulation so that the user does not have direct access to the attributes, so I use getter and setter
    @iin.setter
    def iin(cls, iin):
        if len(iin)==12:
            cls._iin = iin
        else:
            print("Invalid IIN\n")
            return menu()
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @property
    def age(self):
        return self._age

    # they use encapsulation so that the user does not have direct access to the attributes, so I use getter and setter
    @age.setter
    def age(self, age):
        if 1 < age < 100:
            self._age = age
        else:
            print("invalid variable\n")
            return menu()

    @property
    def hashed_password(self):
        return self._hashed_password

    @hashed_password.setter
    def hashed_password(self, hashed_password):
        self._hashed_password = hashed_password
    #a function for the user to enter data
    @classmethod
    def get_user_info(cls):
        iin = input("IIN: ")
        name = input("Name: ")
        surname = input("Surname: ")
        age = int(input("Age: "))
        hashed_password = Users_auth.hash_password(input("Password: "))
        return cls(iin, name, surname, age, hashed_password)
    #saves the data entered by the user in a json file
    def write_json(self, filename):
        with open(filename, "r+") as file:
            file_data = json.load(file)
            file_data["users"].append(self._user_dict)
            file.seek(0)
            json.dump(file_data, file, indent=4)


class Users_auth:
    #method for creating a "user registration" object in a json file
    @classmethod
    def user_reg(cls):
        user = User_lib.get_user_info()
        user.write_json("datajson.json")
    #method to getting data to login
    @classmethod
    def user_login_data(cls):
        iin = input("IIN: ")
        password = input("Password: ")
        return iin, password

    @classmethod
    def user_login_system(cls):#get information to enter the system
        #then hashed the password
        iin, password = cls.user_login_data()
        hashed_password_log = cls.hash_password(password)
        with open("datajson.json", "r+") as file:#read users data from json
            file_data = json.load(file)
        #runs all the data in the json file for a match to log in otherwise it throws an error
        for enter in file_data["users"]:
            if enter["IIN"]==iin:
                if enter["hashed_password"]==hashed_password_log:
                    return enter
                else:
                    return False
        return False
    # @classmethod
    # def user_notes(cls):
    #     print("You need login to change your password")
    #     text=input("You can make notes:\n")
    #     if cls.user_login_system():
    #         set.
    #         with open("datajson.json", "w") as file:#write notes users
    #             json.dump(text,file,indent=4)
    #             file.seek(0)
    #     else:
    #         print("Wrong username or password")

    @classmethod
    def change_password(cls):
        print("You need login to change your password")
        #using the condition checks whether the user is logged in, if not, it gives an error
        if player := cls.user_login_system():
            hashed_password = player["hashed_password"]

            new_password = input("New password: ")
            check_password = input("New password again: ")

            if new_password == check_password:
                hashed_new_password = cls.hash_password(new_password)
                with open("datajson.json", "r+") as file:
                    file_data = json.load(file)
                    index = 0
                    for enter in file_data["users"]:
                        if hashed_password == enter["hashed_password"]:
                            file_data["users"][index]["hashed_password"] = hashed_new_password
                            file.seek(0)
                            json.dump(file_data, file, indent=4)
                            break
                        index += 1
            else:
                print("Passwords don't match")
        else:
            print("Wrong username or password")
    #function for password hashing and encoding
    @classmethod
    def hash_password(cls, password):
        password = password.encode("utf-8")
        hashed_password = hashlib.sha256(password).hexdigest()
        return hashed_password

def menu():
    user_input = int(input("\nPLEASE ENTER APPROPRIATE DATA\n"
                           "\n1.Registration to the system\n"
                           "2.Login in system\n"
                           "3.Change Password\n"
                           "Choose options: "))
    if user_input == 1:
        Users_auth.user_reg()
    elif user_input == 2:
        if Users_auth.user_login_system():
            print("\nYou are enter to the system")
            # Users_auth.user_notes()
        else:
            print("\nUnknown user\n"
                  "Check your data\n")
            return menu()
    elif user_input == 3:
        Users_auth.change_password()
    # elif user_input==4:
    #     Users_auth.user_notes()
    else:
        print("\nINPUT CORRECT NUMBER")
        return menu()


if __name__ == "__main__":
    menu()