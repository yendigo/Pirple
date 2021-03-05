input1 = 99
input2 = 54
input3 = "99"

# "" means that the value is a string and when the function executes it, the value of the string and number will be not equal

var1 = int(input1)
var2 = int(input2)
var3 = int(input3)

# so here we put the function int() to allow the program to read the string into integer

if var1 == var2 or var1 == var2 or var1 == var3 or var2 == var3:
    print(True)
else:
    print(False)    

# and this makes the statement true because there are two number that are the same even the other one is string