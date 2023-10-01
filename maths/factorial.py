
def factorial(n):
    if n<=1:
        return n
    else:
        return(n)*factorial(n-1)

n = int(input("type a no."))

print(factorial(n))