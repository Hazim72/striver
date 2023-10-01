n = int(input("type the number"))
def printDivisorsBruteForce(n):
    print("The Divisors of ",n," are:")
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end=" ")
if __name__ == "__main__":
    printDivisorsBruteForce(n)
