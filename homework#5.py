# FizzBuzz with the twist of Prime 
# placing continue at the end of each condition so that it will continue in the loop if the condition was met 

for num in range(1,101):
    prime = True
    for interval in range(2,num):
        if num % interval == 0:
            prime = False
            break

# this is the condition for determining prime numbers

    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        if prime:  
            print("Prime")
            continue
        continue

# replacing FizzBuzz if the number is multiple of three and five or with Prime if the number is prime

    if num % 3 == 0:
        print("Fizz")
        if prime:
            print("Prime")
            continue     
        continue 

# replacing Fizz if the number is multiple of three or with Prime if the number is prime

    if num % 5 == 0:
        print("Buzz")
        if prime:
            print("Prime")
            continue
        continue

# replacing Buzz if the number is multiple of five or with Prime if the number is prime

    if num != 1 and prime:
        print("Prime")
        continue

# replacing Prime if the number is prime

    print(num)           

# if no condition was met, then print the number itself
# sorry for the comments, trying to insert notes for reviewing in the future ^_^  
