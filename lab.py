### PRINTING
#1)
print('Hello World')

#2 & 3) Data Types & Printing:
# Int
number = 1
print(number)
# Float
float_num = 7.41
print(float_num)
# String
pineapple = 'This is the Way'
print(pineapple)
# Boolean 
status = True
print(status)
# Boolean (The other boolean value)
fstatus = False
print(fstatus)
# Lists ( 4 items in list min.)
listotings = (3, 11, "Coach Prime Time", True)
print(listotings)
# Dictionaries  ( 4 key/value pairs min.)
webster = {
    "word" : 33,
    "picture" : 55,
    "meaning" : 741
}
print(webster)

#4# What is the python equvalent for: console.log(`int: ${intVariable}, string ${stringVariable}`)
print(f"This is the python equivalend for console log {pineapple} and is {status}")

# 6. Write a FOR LOOP in python that prints "David Rocks" 5 times
loop = "David rocks"

for _ in range(5):
    print("David Rocks")

# 7. Declare a function what print "Alex Rocks". Invoke that function 5 times. 
counter = "Alex Rocks"
for _ in range(5):
    print(counter)

# 8. Declare a function that takes in 2 parameters. 
# It will print "P1(your parameter1) and P2(your parameter2) Rocks"
# Now call that function using "Kyle" and "Winston" as the arguments 
# invoke that function 4 more times

Kyle = ("Tis our Method")
Winston = ("that makes us WIN!")

for _ in range(4):
    print(f"We awake in the night because {Kyle}, because {Winston}")

# 9. Remember the list variable in step 2. 
# a. Print the index at 3. Then comment it out
print(listotings[3])
# b. Now print the index at 100. Does this error? comment it out
# print(listotings[100])
# e. Now print the index at -1 index. Observe what it prints. Then comment it out
print(listotings[-1])
# f. Now print the index at -100.  Does this error? comment it out
# print(listotings[-100])

# 10. Write a FOR LOOP in python that prints each item in the list variable in step 2.  
# The staring number MUST be a negative number. The ending number MUST be postive number
# Looking to get each item printed once in order and then a second time in order

for _ in range(-1, 1):
    for _ in listotings:
        print(_)

# 11. Write a WHILE LOOP in python that does the same thing as 10.

counter = 0 
while counter <2:
    print(listotings)
    counter +=1

# 12. For loops.
# Write a FOR LOOP in python that prints each item in list variable in step 2.  
# Hint: type this into google "loop python"

for item in listotings:
    print(item)

# 13. Repeat step 12 but instead of the list variable, use the dictionary variable. 
# Print each key

for item in webster:
    print(item)


# 14. Repeat step 13. Instead of printing each key, print each value
# Hint: google "dictionary values python"

for value in webster.values():
    print(value)

###LISTS LABBY
# 1. Write a program that sum of all elements:
one = [613, 955, 291, 497, 562, 483, 165, 210, 864, 789]
total_s = 0

for number in one:
    total_s += number
print(f"The sum of all one elemetns is {total_s}")

# 2.  Write a program that find the largest element:
two = [386, 850, 274, 316, 526, 937, 998, 249, 269, 922]

largest_e = max(two)
print(largest_e)

# 3. Write a program that duplicates that doubles the value of each elements in the list:
# for example: [1,2,3] should result in [2,4,6]
three = [211, 36, 295, 455, 147, 977, 381, 253, 327, 617]
doubled_it = [x * 2 for x in three]
print(doubled_it)

# 4. Write a program that concatenates these two list into a single list:
four_a = [582, 427, 534, 143, 567, 604, 12, 48, 686, 825]
four_b = [357, 728, 406, 989, 380, 800, 201, 410, 452, 141]

concantenate_l = four_a + four_b
print(concantenate_l)


# 5. Write a program that removes a specific element from a list by its value.
five = [456, 942, 944, 762, 836, 451, 314, 559, 954, 211]
remove_e = 762
if remove_e in five:
    five.remove(remove_e)
print(five)

# 6. Write a program that removes a specific element from a list by its index.
six = [993, 245, 896, 250, 226, 313, 918, 877, 793, 695]
remove_i = 1
if remove_i < len(six):
    six.pop(remove_i)
print(six)

# 7. Write a program that sorts a list of numbers in ascending order.
seven = [887, 106, 368, 603, 35, 455, 728, 449, 108, 47]
seven.sort()
print(seven)

# 8. Write a program that filters out all elements in a list that are less than a specified value.
# use for loop and conditionals
eight = [309, 122, 27, 240, 453, 174, 193, 649, 804, 171]
threshold = 200

filterd_l = []
for element in eight:
    if element >= threshold:
        filterd_l.append(element)

print(filterd_l)

# 9. Calculate and print the length (number of elements) of a given list.
nine = [679, 697, 657, 171, 503, 582, 656, 82, 724, 796]
length = len(nine)
print(length)

# 10. Write a program that take a list and print a subset of its elements by specifying a start and end index.
ten = [64, 800, 662, 185, 630, 612, 181, 210, 738, 12]
start_index = 1
end_index = 4

if start_index >= 0 and end_index <=len(ten):
    subset = ten[start_index:end_index]
    print(subset)
else:
    print("Wrong input, pleasa ensure index provided within perscribed range")


# 11. Write a program iterates the list and
# prints 'FizzBuzz' when divisable by 3 and 5.  
# prints 'Fizz' when divisable by 3 .  
# prints 'Buzz' when divisable by 5. 
eleven = [213, 927, 265, 39, 860, 421, 550, 884, 991, 1500]

for number in eleven:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# 12. Write a program that appends an element to the end of a list.
twelve = [36, 632, 155, 350, 746, 642, 113, 534, 9, 34]
element_tap = 1776

twelve.append(element_tap)
print(twelve)

# 13. Write a program that inserts an element at a specific position in a list.
thirteen = [191, 871, 990, 163, 687, 747, 606, 799, 373, 851]
element_to_insert = 4
posi_insert = 7
thirteen.insert(posi_insert, element_to_insert)

print(thirteen)

# 14. Write a program that counts how many times a specific element appears in a list.
fourteen = [1, 1, 1, 2, 2, 1, 3, 3, 2, 1]
element_to_count = 1
count = fourteen.count(element_to_count)
print(f"The {element_to_count} is present {count} times in the list")

# 15.  Write a program that extracts all even numbers from a list and stores them in even_only:
# use for loop and conditionals
fifteen = [267, 688, 88, 755, 680, 746, 559, 710, 283, 451]
even_only = []
for number in fifteen:
    if number %2 == 0:
        even_only.append(number)

print(even_only)


# 16. Write a program that reverses this list but does not change the original sixteen variable:
# The answer is not sixteen.reverse(). 
sixteen = [378, 763, 856, 566, 847, 795, 313, 540, 67, 219]
rev_sixteen = sixteen[::-1]
print(rev_sixteen)

# 17. Write a flattens this double nested listbelow:
# Result should be [1, 2, 3, 4, 5, 6, 7, 8]
# Hint: try a nested loop (2 for in loops) 
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat_list = []
for subkust in nested_list:
    for item in subkust:
        flat_list.append(item)

print(flat_list)


# 18. Write a program that finds duplicates from the 2 lists below:
# Hint: try a nested loop (2 for in loops) and use equality
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
duplicate = []
for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            duplicate.append(item1)
duplicate = list(set(duplicate))

print(duplicate)



# Go back to Alex's lesson on Wednesday August 30th as a guide

# 1. Create a class called Wolf. When this class is instantiated it takes in a name and age. 
# the class is also to have a method called back which will print its name and 'Ahhhoooo'

# 2. Instantiate: Create an Object from the Wolf class and use the bark method

# 3. Create a class called Dog. This class will Inherit from the class Wolf. 
# Do not define any methods

# 4. Instantiate: Create an Object from the Dog class and try the bark method

# 5. Remember the class Fighter from Aug 30th.
# Change the attack method. 
# In the attack method, damage is strength subtracted by defense. 
# This needs change to: Any integer value between zero and strength subtracted by defense.
# Look up how to generate random number python
# Look up how to round to nearest intergy python

# 6. Change ryu and ken to have the same stats. Fight until ken win 2 times
# While the advantage will still be on the first attacker's side the result should be closer to 50/50
# I like an even match
import random 
class Fighter:
    def __init__(self, name, hp, strength, defence):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.defence = defence
        
    def attack(self, opponent):
        damage = round(self.strength * random.random()) - opponent.defence
        if (damage < 0):
            damage = 0
        opponent.hp -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage")
        
ryu = Fighter("Ryu", 100, 10, 5)
ken = Fighter("Ken", 100, 12, 3)

while(True):
    ryu.attack(ken)
    
    if (ken.hp <= 0):
        print(f"{ryu.name} wins!")
        break
        
    ken.attack(ryu)
    
    if (ryu.hp <= 0):
        print(f"{ken.name} wins!")
        break
