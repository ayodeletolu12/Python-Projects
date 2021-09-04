'''
This program slices inputted user email addresses into their usernames and domain names

Program developed by Tolulope Olorunfemi
Information Security expert
USA
'''

# Users are requested to enter their email addresses and stored in a variable name called email address

emailAddress = input("Hello User, please kindly enter your email address? ")

# inputted email addresses are sliced into the username and domain names

username = emailAddress[:emailAddress.index("@")]

domain = emailAddress[emailAddress.index("@") + 1:]

result = print("Please note that your username is {} and domin name is {}".format(username, domain))
