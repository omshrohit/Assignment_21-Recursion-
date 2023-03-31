# write a recursive python function to  print a number in reverse order.
def reverseNum(n, rem=0):
   if n == 0:
      return (rem)//10
   else:
      return reverseNum(n//10, (rem+(n%10))*10)

        
r=reverseNum(123)
print(r)

