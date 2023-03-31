# write a recursive python function to print  n even natural number in reverse order.
def reverseeven(num):
    if num>0:
        print(num*2)
        reverseeven(num-1)
reverseeven(10)