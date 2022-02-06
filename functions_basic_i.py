#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# output is 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#output would be an error because of an undefined item


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#output would be 5. the first return would cancel out the rest of the code block


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#output would be 5. the first return would cancel out the rest of the code block


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# output would be 5 none. none is because our function has an empty parameter so x doesn't get a real value.

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# output would be 3 5. it would pass over the first print because b and c aren't given values at that time

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# output would be 25. rather than 7 because of the added in str in the return.


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# output is 100 10. first print reads normal with b = 100. first if statement is false so move to else statement which is true so returning 10. that return cancels out rest of code block.


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# output is 7, 14, 21. the first print 2<3 returns 7. second print 5<3 is false returns 14. third print adds both returns to be 21. 


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# output is 8. 3+5 = 8 which is the return.


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# output is 500 500 300 500. first print line = 500. we skip the function until it is called so the next print line is 500, then function call gives print line 300, then goes back to 500 for last print line.


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# output is 500 500 300 500. first print line = 500. we skip the function until it is called so the next print line is 500, then function call gives print line 300, the return cancels the rest of code block, then goes back to 500 for last print line.


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# output is 500 500 300 300. first print line b = 500 so we log 500. skip function till called. print b again log another 500. foobar is now given value of 500 but function itself changes value to 300. print 300. return 300 so last print line gives another 300.

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# output is 1 3 2. first print line is 1 and the second one is skipped until next function where we print 3. then when our first function is called again it then prints 2. 


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# output is 1 3 5 10. 1 from the first print line, we skip print x because x has no given value at this point. move to next function we print 3 and then print 5 from return. y is then equal to foo() which was given a return value of 10 which is our last print line. 