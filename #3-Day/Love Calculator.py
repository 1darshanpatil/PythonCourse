# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
cnt = 0
sentence = (name1 + name2).lower()
for x in "true":
    cnt += sentence.count(x)
cnt2 = 0
for y in 'love':
    cnt2 += sentence.count(y)
score = 10*cnt + cnt2
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score in range(40, 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
    
 #Fun fact: After writing this code I entered my name and then I started thinking what name should I enter, I couldn't find name of any girl that I would have liked to enter and know the score.....😂
