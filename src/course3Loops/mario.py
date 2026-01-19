'''def main():
    print_column(3)

def print_column(height):
    print("#\n" * height , end="")

main()'''

def main():
    print_square(3)

def print_square(size):
    #for each row in square
    for i in range(size):
        #foe each brick in row 
        for j in range (size):
            #print brick 
            print("@",end="")
        #change line
        print()

main()