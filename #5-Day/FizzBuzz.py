for x in range(1, 101):
    if x%3 == 0 and x%15 != 0:
        print("Fizz")
    elif x%5 == 0 and x%15 != 0:
        print("Buzz")
    elif x%15 == 0:
        print("FizzBuzz")
    else:
        print(x)

'''
for x in range(1, 101):
    if x%15 == 0:
        print("FizzBuzz")
    if x%3 == 0:
        print("Fizz")
    elif x%5 == 0:
        print("Buzz")
    else:
        print(x)
'''
