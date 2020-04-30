import pyperclip


class Credential:

    credentials_list = []
    user_credentials_list = []
    def check_user(cls,username,password):

        current_user = ''
        for user in User.user_list:
            if (user.username == username and user.password == password):
                current_user = user.username
                return current_user

    def __init__(self,account_name,username,password):

        self.account_name = account_name
        self.username = username
        self.password = password

    def save_credential(self):

        Credential.credentials_list.append(self)

    def delete_credential(self):

        Credential.credentials_list.remove(self)

    @classmethod
    def find_by_username(cls,username):

        for credential in cls.credentials_list:
            if credential.username == username:
                return credential

    @classmethod
    def credential_exist(cls, password):
        """This method allows users to locate existing credentials"""
        for credential in cls.credentials_list:
            if credential.password == password:
                return True

    @classmethod
    def display_credentials(cls, username):

            user_credentials_list = []

            for credential in cls.credentials_list:
                if credential.username == username:
                    user_credentials_list.append(credential)
            return user_credentials_list

    @classmethod
    def copy_password(cls,username):
        credential_found = Credential.find_by_username(username)
        pyperclip.copy(credential_found.password)
