#  write a recursive python function to print first N odd natural number in reverse order.
def reverseOdd(num):
    if num>0:
        print(num*2-1)
        reverseOdd(num-1)
        
reverseOdd(10)