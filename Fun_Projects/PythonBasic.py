##tuples
corrdinates =[(4, 5), (6,7), (80,34)]
print(corrdinates)

##Functions
def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))

say_hi("Mike", 35)
say_hi("Steven", 70)

##return statement
def cube(num):
    return num*num*num

result = cube(4)
print(result)

##if statement
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")

##if statement&comparision ==;!=;
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return  num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(50,40,5))

##dictionaries
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

print(monthConversions.get("Lav","Not a vaild key"))

##while loop
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")


secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You Lose!")
else:
    print("You win!")

##For loop
for letter in "Giraffe Academy":
    print(letter)
friends = ["Jim", "Karen", "Kevin"]
len(friends)
for index in range(len(friends)):
    print(friends[index])
    friends[2]

##Exponent Function
print(2**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num

print(raise_to_power(2,3))


#2Dlists&Nested Loops
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])

for row in number_grid:
    for col in row:
        print(col)



#Try expect
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")

#reading files
employee_file = open("employees.txt",'r')
for emplotee in employee_file.readlines():
    print(employee)
employee_file.close()

employee_file = open("employees.txt","a")
employee_file.write("\nToby - Human Resources")
employee_file.close()

name = input("Enter Your Name: ")
age = input("Enter Your age: ")
print("Hello " + name + "!" + "You are " + age)

##### input/build basic calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result)

color = input("Enter a color: ")
plural_noun =("Enter Plural: ")
celebrity = input("Enter a celebrity: ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

#### lists
friends = ["Kevin", "Karen", "Jim","Oscar", "Tim"]
print(friends[0])
print(friends[1:])

friends[1] = "Mike"

####lists function
lucky_numbers =[4,8,15,16,23,42]
friends =["Kevin", "Karen", "Jim","Oscar", "Tim"]
friends.append("Creed")
friends.insert(1, "Kelly")
friends.clear()
friends.pop()
lucky_numberw.sort()
print(friends)
