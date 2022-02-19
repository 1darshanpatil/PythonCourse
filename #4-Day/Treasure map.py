row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
for rows in map:
    print(rows)
position = input("Where do you want to put the treasure? ")
pst = int(position)
x, y = int(pst/10), int(pst%10)
map[y - 1][x - 1] = "X"
for rows in map:
    print(rows)
