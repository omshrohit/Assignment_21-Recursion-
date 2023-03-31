# write a recursive python function to print first N odd  natural numbers
def odd(num):
    if num>0:
        odd(num-1)
        print(num*2-1)
odd(10)