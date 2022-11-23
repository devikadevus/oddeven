#def myfunc():
 #   num = int(input("Whether the given number is odd or even:"))
 #   if (num % 2 == 0):
 #        print(" the given number is even")
    # else:
   #     print("the given number is odd")
  #      myfunc()


def oddEven(n):
    if(n == 0):
        return True
    elif(n==1):
        return False
    else:
        return oddEven(n-2)

num = int(input("enter  number whethr checking it is odd or even:"))
if(oddEven(num)):
    print(num,"num is even")
else:
    print(num,"num is odd")