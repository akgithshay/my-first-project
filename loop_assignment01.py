# Explain with an example each when to use a for loop and a while loop.

# example of for loop : print square of a number using for loop

for i in range (10):
    print(i**2)


# example of while loop : print square of a number using while loop

i = 0
while i<11:
    print(i**2)
    i = i+1

print("\n\nSecond Question Start:\n\n")
#  Write a python program to print the sum and product of the first 10 natural numbers using for and while loop.

# sum using for loop
sum = 0
for i in range(11):
    sum = sum +i
print("the sum of first n natural number is " , sum)

# sum using while loop
sum = 0
i=0
while i < 11:
    sum = sum + i
    i = i+1
print("the sum of first n natural number usin while loop is  ",sum )

print("\n \n")

print("Third Question Start:\n")


# product  using while loop

product = 1
for i in range(1,11):
    product = product *i
print(product)

product=1
i = 1
while i < 11:
    product = product * i
    i=i+1
print(product)



# # Q.3 The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
# # unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
# # be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.
# # You are required to take the units of electricity consumed in a month from the user as input.
# # Your program must pass this test case: when the unit of electricity consumed by the user in a month is
# # 310, the total electricity bill should be 2250.


unit = int(input("Enter the amount of unit consumed in a month"))
charge = 1
if unit <= 100:
    charge = 4.5* unit

elif  unit <=200:
    charge = (100*4.5) + (unit-100)*6

elif   unit <=300:
    charge = (100*4.5)+(100*6)+(unit-200)*10
else:
    charge = (100*4.5)+(100*6)+(100*10) + (unit-300)*20

print(charge)

print("\n\nfourth question start")

# Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
# number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print that list.

list1 =  list(range(101))
# print(list1)
arr= []

# using for loop
for i in range(len(list1)):
    cube = (list1[i]**3)
    print(cube)
    if cube % 5 == 0 or cube %4 == 0:
        arr.append(cube)
print(arr)

# using while loop

i=0
while i < len(list1):
    cube = (list1[i]**3)
    i=i+1
    print(cube)

    if cube % 4 ==0 or cube %5 == 0:
        arr.append(cube)
print(arr)


print("\n\n question  5th start \n")

# # Write a program to filter count vowels in the below-given string.
# # string = "I want to become a data scientist"

count = 0

call = "I want to become a data scientist"
# print(len(call))
for i in range(len(call)):
    # print(call[i])
    if(call[i] == 'a' or call[i] == 'A' or call[i] == 'e'  or call[i] == 'E'  or call[i] == 'i' or call[i] == 'I' or call[i] == 'o' or call[i] == 'O' or call[i] == 'u' or call[i] == 'U' ):
        count = count+1
print("total vowels are ", count)

        





