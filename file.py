num1 = 42 #variable decloration
num2 = 2.3 #variable decloration
boolean = True #boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#strings
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))#strings
print(pizza_toppings[1])#log statement
pizza_toppings.append('Mushrooms')#change value
print(person['name'])#log statement 
person['name'] = 'George' #change value
person['eye_color'] = 'blue' #change value
print(fruit[2])#log statement

if num1 > 45: #if statement 
    print("It's greater") #log statement 
else: #else statment
    print("It's lower") #log statement

if len(string) < 5: #if statement
    print("It's a short word!")#log statement 
elif len(string) > 15: #error 
    print("It's a long word!")#log statement
else:#else statement
    print("Just right!")#log statement 

for x in range(5): #for loop
    print(x)#log statement
for x in range(2,5): #for loop
    print(x)#log statement
for x in range(2,10,3):#for loop
    print(x)#log statment 
x = 0 #variable decloration
while(x < 5): #while loop
    print(x)#log statment
    x += 1 #change value

pizza_toppings.pop()
pizza_toppings.pop(1)#delete value

print(person)#log statement
person.pop('eye_color')#delete value
print(person)#log statment

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni':#if statment boolean
        continue#continue
    print('After 1st if statement')#log statment
    if topping == 'Olives': #if statment 
        break#break

def print_hello_ten_times(): #function
    for num in range(10):#for loop
        print('Hello')#log statement

print_hello_ten_times()#log statement

def print_hello_x_times(x):#function
    for num in range(x):#for loop
        print('Hello')#print statement

print_hello_x_times(4)#print statement

def print_hello_x_or_ten_times(x = 10):#functoion, change value
    for num in range(x):#for loop
        print('Hello')#log statment

print_hello_x_or_ten_times()#function
print_hello_x_or_ten_times(4)#function


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)