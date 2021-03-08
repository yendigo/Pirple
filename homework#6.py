InputRow = int(input("Enter the number of rows: "))
InputColumn = int(input("Enter the number of columns: "))

if InputRow == 3:

    # specific value to draw the desired playing board

    for row in range(InputRow+2): 

    # plus 2 to make it 5
    
        if row % 2 == 0:
            if InputColumn == 3:
                for column in range(1,InputColumn+3):

                    # plus 3 to make the stoping value of 6

                    if column % 2 == 1:
                        if column != 5:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print(False)       
        else:
            print("-----")
    print(True)
else:
    print(False)
