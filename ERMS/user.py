import json
class InvalidLogin(Exception):
    pass

class InValidPassword(Exception):
    pass

class TooManyAttempts(Exception):
    pass

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.__password = password
        self.role = role
        self.loginAttempt = 3

    def validate_user(self):
        try:
            with open('/data/users.json', mode='r') as file:
                data = json.load(file)
                for i in data:
                    if i['username'] == self.username and  i['password'] == self.__password:
                            return True

                return False

        except json.JSONDecodeError:
            print("Error: Corrupt Json file")
        except FileNotFoundError:
            print("Error: File not found...")
            return False
        except ValueError:
            print("Error: Missing data")
            return False



    def login(self):
        try:
            if self.loginAttempt <= 0:
                raise TooManyAttempts("Error: too many attempts, try again later")
            with open('/data/users.json', mode='r') as file:
                data = json.load(file)

                for i in data:
                    if i['username'] == self.username:
                        if i['password'] == self.__password:
                            print("Login successful....")
                            return True
                        else:
                            self.loginAttempt -=1
                            raise InvalidLogin("Error: Username and password doesn't match")

                #adding new user
                new_data = {
                    'username': self.username,
                    'password': self.__password,
                    'role': self.role
                }
                data.append(new_data)
            with open('/data/users.json', mode='w') as file_reopen:
                json.dump(data, file_reopen)
                return True

        except json.JSONDecodeError:
            print("Error: Corrupt Json file")
            return False

        except FileNotFoundError:
            print("Error: file not found...")
            return False

        except InvalidLogin:
            print("Error: Username and password doesn't match")
            return False

        except ValueError:
            print("Error: Missing data")
            return False


    def change_password(self, newPassword):
        try:
            login_success = self.validate_user()
            if login_success:
                if len(newPassword) < 8:
                    raise InValidPassword('Error: Password length cannot be less than 8')
                with open('/data/users.json', mode='r') as file:
                    data = json.load(file)

                    for i in data:
                        if i['username'] == self.username:
                            i['password'] = newPassword
                            self.__password  = newPassword

                with open('/data/users.json', mode='w') as dataFile:
                    json.dump(data, dataFile)
                    return True

        except json.JSONDecodeError:
            print("Error: Corrupt Json file")
        except InValidPassword:
            print('Error: Password length cannot be less than 8')
            return False

        except FileNotFoundError:
            print("Error: FIle not found")
            return False

        except ValueError:
            print("Error: Missing data")
            return False







