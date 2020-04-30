#!/usr/bin/env python3.7
from credentials import Credential
from user import User

def create_user(username,password):

	new_user = User(username,password)
	return new_user

def save_user(user):

	User.save_user(user)


def verify_user(first_name,password):

	checking_user = Credential.check_user(username,password)
	return checking_user

def create_credential(account_name,username,password):

    new_credential = Credential(account_name,username,password)
    return new_credential

def save_credential(credential):

    credential.save_credential()

def del_credential(credential):

    credential.delete_credential()

def find_credential(username):

    return Credential.find_by_username(username)

def check_existing_credentials(username):

    return Credential.credential_exist(username)

def display_credentials():

    return Credential.display_credentials()

def main():
	print(' ')
	print('Hello! SafePass at your service! ')
	print('\n')

	while True:

		print('Use these codes to navigate: \n ca-Create an Account \n li-Log In \n ex-Exit')

		short_code = input().lower()

		if short_code == 'ca':
			print('To create a new account:')
			print("-"*10)

			username = input('Enter your username - ').strip()
			password = input('Enter your password - ').strip()

			save_user(create_user(username,password))

			print('\n')
			print(f"New Account Created for: {username} using password: {password}")
			print ('\n')

		elif short_code == "li":
			print('To Log in, enter account details:')
			username = input('Enter your username  ').strip()
			password = str(input('Enter your password - '))
			# user_exists = verify_user(username,password)
			# if user_exists == username:
			print('\n')
			print(f'Welcome {username}. Choose an option to continue.')
			print(' ')
			while True:
				print("\n")
				print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit')
				short_code = input('Enter a choice: ').lower().strip()
				print("\n")

				if short_code == 'ex':
					print("")
					print (f"See You later {username}")
					break

				elif short_code == 'cc':
					print("")
					print("Lets save your Credentials")
					print("Account name ...")
					account_name = input()

					print("Username ...")
					username = input()

					print("Password ...")
					password = input()

					save_credential(create_credential(account_name,username, password))
					print('\n')
					print (f"New Credentials for {account_name} using {username} as username and {password} as password has been created and stored successfully")
					print("\n")

				elif short_code == 'copy':
					print("")
					if display_credentials():
						print("Here is a list of all your credentials")
						print('\n')

						for credential in display_credentials():
							print(f"{credential.account_name} {credential.username} .....{credential.password}")
							print('\n')
					else:
						print ('\n')
						print("You dont seem to have any credentials saved yet")
						print('\n')

				elif short_code == 'dc':
					print("")
					if display_credentials():
						print("Here is a list of all your credentials")
						print('\n')

						for credential in display_credentials(username):
							print(f"{credential.account_name} {credential.username} .....{credential.password}")
							print('\n')
					else:
						print ('\n')
						print("You dont seem to have any credentials saved yet")
						print('\n')

				else:
					print("I really didn't get that. Please use the short codes")


		elif short_code == "ex":
		            print("Bye .......")
		            break

		else:
			print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
	main()
