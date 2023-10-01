
def solve(n):
    if n <= 1:
        return n
    else:
        return(n)+ solve(n-1)
n = int(input("type the no."))

print(solve(n))