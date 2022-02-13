email = input("Kindly type in your email address:").strip()

user_name = email[:email.index("@")]

user_domain = email[email.index("@")+1:]

email_split = "Hi, Your username is '{}' and your user domain is '{}'".format(user_name, user_domain)

print(email_split)