answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
answer = answer.strip().title()

if answer == "42" or answer == "Forty-Two" or answer == "Forty Two":
    print("Yes")
else:
    print("No")