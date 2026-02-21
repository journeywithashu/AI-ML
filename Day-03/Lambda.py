sum = lambda a,b: a+b
print(sum(4,5))

#avg
avg = lambda a,b: (a+b)/2
print(avg(4,5))

#calculate factorial

def calc_factorial(n):
     fact = 1
     for i in range(1, n+1):
          fact *= i
     return fact

n = int(input("enter n:"))
print(calc_factorial(n))