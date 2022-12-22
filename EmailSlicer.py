#get user email
email=input("Enter your email:").strip()


#slice out the user_name from user input
user_name=email[:email.index('@')]


#slice out the domain_name from user input
domain_name=email[email.index('@')+1:]



#format message
output = "Your username is '{}' and your domain name is '{}'".format(user_name,domain_name)


#display required output
print(output)