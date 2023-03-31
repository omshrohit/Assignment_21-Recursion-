# write a recursive python function to  print cubes of first N natural numbers
def cubes(num):
    if num>0:
        cubes(num-1)
        print(num**3)
cubes(10)