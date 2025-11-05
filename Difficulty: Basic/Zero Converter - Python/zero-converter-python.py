def pos(n):
    ## Write the code
    if n!=0:
        while n > 0:
            n -= 1
            print(n, end=" ")
    else:
        print("already Zero")
    
def neg(n):
    ##Write the code

    if n!=0:
        while n <= 0:
            print(n, end=" ")
            n += 1
    else:
        print("already Zero")
            
    