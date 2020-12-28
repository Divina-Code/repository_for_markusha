print("Hello, Random User !")

user_name = input("What is your name? ")

print("Hello, ", user_name, ", You have letters in your name: ", len(user_name))

user_year = int(input("What year were you born in? "))
if len(str(user_year)) == 4:
    print("Oh, i like your year of birth,", user_year)
    print("You're so young !", 2020-user_year)
else:
    print("You made a mistake ! Correct it soon !")
