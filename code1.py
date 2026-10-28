#for iron man
FN = "Tony"
LN = "Stark"
Ag = 51
H = 1.85
SP = True

#for Captain America
FN2 = "Steve"
LN2 = "Rogers"
Ag2 = 35
H2 = 1.88
SP2 = True

#for Hulk
FN3 = "Bruce"
LN3 = "Banner"
Ag3 = 45
H3 = 1.80
SP3 = True

superhero_name = input("Enter your superhero name: ")

if superhero_name == "Iron Man":
    print("First Name:", FN)
    print("Last Name:", LN)
    print("Age:", Ag)
    print("Height:", H)
    print("IS He an Superhero:", SP)

if superhero_name == "Captain America":
    print("First Name:", FN2)
    print("Last Name:", LN2)
    print("Age:", Ag2)
    print("Height:", H2)
    print("IS He an Superhero:", SP2)

if superhero_name == "Hulk":
    print("First Name:", FN3)
    print("Last Name:", LN3)
    print("Age:", Ag3)
    print("Height:", H3)
    print("IS He an Superhero:", SP3)