'''colors'''
A = str(input())
B = str(input())
if A + B =="RedYellow" or A + B =="YellowRed":
    print("Orange")
elif A +B =="RedBlue" or A+ B    =="BlueRed":
    print("Violet")
elif A + B =="YellowBlue" or A + B =="BlueYellow":
    print("Green")
elif A == "Red" and B == "Red":
    print("Red")
elif A == "Yellow" and B == "Yellow":
    print("Yellow")
elif A == "Blue" and B == "Blue":
    print("Blue")
else:
    print("Error")
