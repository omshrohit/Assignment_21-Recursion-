# write a recursive python function to print squares of First N natural numbers.
def square(num):
    if num>0:
        square(num-1)
        print(num**2)
square(10)