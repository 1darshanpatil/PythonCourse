print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
if input('Choose direction "left" or "right"? ').lower() == "left":
	if input("It's a river swim or wait for a boat? ") == "wait":
		door = input("There are three doors on of Red, Yellow, and Blue, Which to choose? ")
		if door == "Red":
			print("Red means fire it's a room of fire... Game Over!")
		elif door == "Blue":
			print("Eaten by a blue giant, Game Over!")
		elif door == "Yellow":
			print("Yellow means treasure, You win!")
		else:
			print("You invented your own door, Door of Hell, Game Over!")
	else:
		print("Attacked by trout Game Over.")

else:
	print("Right is not always right, sometimes left is also right, Game Over!")

	
	
#Map of the treasure ok flow chart

'''
https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
'''
