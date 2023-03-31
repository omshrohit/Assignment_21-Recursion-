# write a recursive python  function to print first N  multiples of a given number.
def multiple(n):
    num=5
    if n>0:
        multiple(n-1)
        print(num*n)
multiple(10)
