num1 = int (input ("First number"))
num2 = int (input ("second number"))

def solve(a:int,b:int) ->int:
    if a==0:
        return b
    return solve(b%a,a)
print ("HCF=",solve(num1,num2))
