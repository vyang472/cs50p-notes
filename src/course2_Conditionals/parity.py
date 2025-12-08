def main():
    x = int(input("What is x? "))
    if is_even(x):
        print (x,"Is even")
    else:
        print (x,"Is odd")
    
def is_even(N):
    if N % 2 == 0:
        return True
    else:
        return False 
    #you can also do 
    #return N % 2 == 0


main()