# num1 = int (input ("First number"))
# num2 = int (input ("second number"))

# def solve(a,b):
#     if a==0:
#         return b
#     return solve(b%a,a)
# print ("HCF=",solve(num1,num2))


num1 = int(input("First no."))
num2 = int(input("Second NO."))

def solve(a,b):
    if a==0:
        return b
    return solve(b%a,a)
print (solve(num1,num2))