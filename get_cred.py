from getpass import getpass

def get_credentials():
	email = input('Please enter your HackerRank username or email address \n')
	password = getpass('Please enter your HackerRank password \n')
	print ('Thank you')
	return email, password