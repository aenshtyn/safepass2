import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("NewUser", "12345")

    def test_init(self):
        self.assertEqual(self.new_user.username, "NewUser")
        self.assertEqual(self.new_user.password, "12345")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()
