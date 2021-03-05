myUniqueList = []
myLeftovers = []

# the lists are empty

print("Please input three numbers or words: ")

# title
# the user will enter 3 inputs
# i limit this to 3 inputs to be not that complicated because my way of coding are long

input1 = input("Input1: ")

if input1 != myUniqueList:
    print(True)
    myUniqueList.append(input1)
else:
    print(False)

# adding the 1st input into the list

input2 = input("Input2: ")

if input2 != input1:
    print(True)
    myUniqueList.append(input2)
else:
    print(False)
    myLeftovers.append(input2)

# testing if the 2nd input and the 1st input are not the same
# if True, add the value to the list
# if False, add the value to the other list

input3 = input("Input3: ")

if input3 != input2 and input3 != input1:
    print(True)
    myUniqueList.append(input3) 
else:
    print(False)
    myLeftovers.append(input3)

# testing if the 3rd input, 2nd input and the 1st input are not the same 
# if True, add the value to the list 
# if False, add the value to the other list

print(myUniqueList)
print(myLeftovers)
