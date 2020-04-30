class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
    user_list = []

    def save_user(self):
        self.user_list.append(self)


if __name__ == '__main__':
    main()
