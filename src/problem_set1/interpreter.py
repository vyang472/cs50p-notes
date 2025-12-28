x =input("Expression: ").strip().split( )
y = int(x[0])
z = int(x[2])
if x[1] == "*":
    print("{:.1f}".format(y * z))
elif x[1] == "+":
    print("{:.1f}".format(y + z))
elif x[1] == "/":
    print("{:.1f}".format(y / z))
elif x[1] == "-":
    print("{:.1f}".format(y - z))
