import pyperclip
import unittest # Importing the unittest module
from credentials import Credential # Importing the credential class
from user import User


class TestCredential(unittest.TestCase):



    def test_check_user(self):

        self.new_user = User('Jane','11111')
        self.new_user.save_user()
        user2 = User('John','222222')
        user2.save_user()

        for user in User.user_list:
            if user.username == user2.username and user.password == user2.password:
                current_user = user.username
                return current_user

                self.assertEqual(current_user,Credential.check_user(user2.password,user2.username))

    def tearDown(self):

        Credential.credentials_list = []

    def setUp(self):

        self.new_credential = Credential("James","Muriuki","0712345678") # create credential object


    def test_init(self):

        self.assertEqual(self.new_credential.account_name,"James")
        self.assertEqual(self.new_credential.username,"Muriuki")
        self.assertEqual(self.new_credential.password,"0712345678")

    def test_save_credential(self):

        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credentials_list),1)

    def test_save_multiple_credential(self):

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","0712345678",) # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),2)

    def test_delete_credential(self):

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","0712345678",)
        test_credential.save_credential()

        self.new_credential.delete_credential()

    def test_find_credential_by_username(self):

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","0711223344") # new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_username("user")

        self.assertEqual(found_credential.account_name,test_credential.account_name)

    def test_credential_exists(self):

        self.new_credential.save_credential()
        test_credential = Credential("Mighty", "Diamonds", "Marcus" )
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("Marcus")
        self.assertTrue(credential_exists)

    # def test_display_credentials(self):
    #
    #     self.new_credential.save_credential()
    #     twitter = Credential("Jane", "Twitter", "maryjoe" )
    #     twitter.save_credential()
    #     gmail = Credential('Jane','Gmail','maryjoe')
    #     gmail.save_credential()
    #     self.assertEqual(len(Credential.display_credentials(twitter.username)),2)


if __name__ == '__main__':
    unittest.main()
