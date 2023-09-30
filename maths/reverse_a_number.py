# 12345
# i = 12345
# 
# n = 0
# while (i>0):
    # n = (n*10)+i%10
    # i=i//10
# 
# print ("Reverse=",n)



# i = 9179846462
# n = 0
# while (i>0):
#     n=(n*10)+i%10
#     i=i//10

# print("Reverse=",n)

def reverse(number:int)->int:
    n = 0
    while (number>0):
        n=(n*10)+number%10
        number=number//10
    return n
