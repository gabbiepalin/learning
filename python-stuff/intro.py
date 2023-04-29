print("What is your name?")
myName = input()

print("What is your age?")
# ""  = "55" as a string
myAge = input()
# "55" = int(myAge)
myAge = int(myAge)


print("what is her name?")
herName = input()

print("what is her age?")
herAge = input()
herAge = int(herAge)


# print("The data type of age is:", type(myAge), "Age as a value:", myAge)
print("Your name is:", myName, "and your age is:", myAge, "years old.")
print("her name is:", herName, "and her age is:", herAge, "years old")

# If she is younger then we will take her age from his age
if herAge < myAge:
    print("the difference is:", myAge - herAge, "years old")
else:
    # if she is older then we will take his age from her age
    print("the difference is:", herAge - myAge, "years old")
    
