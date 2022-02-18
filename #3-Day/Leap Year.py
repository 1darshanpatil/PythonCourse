yr = int(input("Which year do you want to check? "))
condition = yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0)
if condition:
    print("Leap year.")
else:
    print("Not leap year.")



#import calendar as cl
#print(cl.isleap(yr))
