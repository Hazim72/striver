n = 20
def recursion(num):
    if num == 1:
        print(num)
        return
    print(num)
    recursion(num-1)

recursion(n)