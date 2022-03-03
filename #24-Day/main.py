#Basically, the mail_merge project is to send invitation to my old friends for my fake wedding
#Theare are two files one with template and another with list of names
#We need to create new files(letters) by replacing names from template
#SEe, I can' type anymore just try to understand by running the code....plzz mann


with open("names_of_invited_people.txt") as frnds:
    names = frnds.readlines()



with open("invitation_template.txt") as template:
    templet = template.read()
    for name in names:
        replaced_temp = templet.replace('[name]', name.strip())              #.replace() method returns to other variable it doesn't change th object
        with open(f"./letters/letter_for_{name.strip()}.txt", mode = 'w') as lettr:
            #on above line we used mode = 'w' because by default it's 'r' mode
            lettr.write(replaced_temp)