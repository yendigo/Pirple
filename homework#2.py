def Title():
    print("Like You")
    return Title

def Artist():
    print("Tatiana Manaois")
    return Artist

def Released():
    print("December 07, 2015")
    return Released

Title()
Artist()
Released()

#calling the function

Title1 = Title()
print(Title1)

#extra credit: Booleans

def Title(title):
    if title == "Like You":
        print('True')
    else:
        print('False')

Title("Like You")
Title("Like Me")
