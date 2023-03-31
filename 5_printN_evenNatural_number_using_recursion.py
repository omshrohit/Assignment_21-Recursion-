# write a recursive python function to  print   first N even natural numbers.
def even(num):
    if num>0:
        even(num-1)
        print(num*2)
even(10)