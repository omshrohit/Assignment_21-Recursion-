# write a recursive python  function to print first N natural numbers.
def natural(num):
    if num>0:
        natural(num-1)
        print(num)
natural(10)