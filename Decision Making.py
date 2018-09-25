# if ,if else in Python:~
# if else statement in use for check conditions.

# so First 'if' Statement:
a = 5
if a == 5:                  # ':' colon is use
    print('Yes its Equal')

# Now suppose the condition is false:
if a == 6:
    print('yes its equals')     # the Code is Not execute

# There will nothing show if Condition is false than we use 'if esle'

# We use 'if else' whether the condition is false:~
if a == 6:
    print('its equal')

else:
    print('its not equal')

# 'if' and 'if else' should be stat from the first line or it will show the error
# Syntax
#if:
#   print()             # if the condition is true, the code will stop here <==
#else:
#   print()             # other wise the condition is false the code runt to the next block 'else' block <==

# 'if' , 'if else' using in logic of login:
username = 'ashfaq'
password = 123
if username == 'ashfaq' and password == 123:
    print('Welcome '+username)

else:
    print('check your username or pass')

# 'elif' , 'Nested if' in Python:~
# elif statement:
# elif statement use for multiples statement condition.

name = 'kareem'
if name == 'ashfaq':
    print('I will give you blue suit')

elif name == 'kareem':
    print('I will give you black suit')

elif name == 'afaq':
    print('I will give you red suit')

else:
    print('No one in the list')

# Nested 'if':
# In Nested if check if in the if statement.

email = 'ashfaq@gmail.com'
password = 123

if email == 'ashfaq@gmail.com':
    if password == 123:
        print('Welcome '+email)

    else:
        print('please check your password')
else:
    print('Check your user name or password')