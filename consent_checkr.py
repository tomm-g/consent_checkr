# half the age plus 7 to check age range
# if user is over 18 minimum age of other person must be >= 18
# Ver. 0.9

print('**************************')
print('Welcome to Consent Checkr!')
print('**************************\n')


print("Enter your age: ")
user_age = input()
user_age = int(user_age)


print("Enter other person's age: ")
other_age = input()
other_age = int(other_age)

lowest_age = (user_age // 2) + 7

if user_age >= 18 and other_age < 18:
    print("NONCE DETECTED")

elif other_age >= 18 and user_age < 18:
    print("NONCE DETECTED")

elif other_age >= lowest_age:
    print("You're good to go")

elif other_age < lowest_age:
    print("You're in dangerous territory....")

