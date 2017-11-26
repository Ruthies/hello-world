#Write a function that takes in two numbers and recursively multiplies them together.
print('--Multiply 2 numbers recursively')
def multiply2(a,b):
    if a>=0 and b>=0:
        multiply2(a-1,b-1)
        print(a*b)
#print(multiply2(2,3))
#print(multiply2(10,15))

"""Write a function that takes in a base and an exp and recursively computes baseexp. You are not allowed to
use the ** operator!"""
print('--Compute exponent value')
def expComp(b,e):
    if e==1:
        return b
    return b*expComp(b,e-1)

#print(expComp(2,5))
#print(expComp(3,4))
#print(expComp(6,7), "compare with", 6**7)

"""Write a function using recursion to print numbers from n to 0"""
print('--Print numbers from n to 0')
def prntNums(n):
    if n>=0:
        print(n)
        prntNums(n-1)

#prntNums(5)

"""Write a function using recursion to print numbers from 0 to n (you just need to change one line in the program
of problem 1)"""
print('--Print numbers from 0 to n')
def prntNums1(n):
    if n>=0:
        prntNums1(n-1)
        print(n)

#prntNums1(4)

"""Write a function using recursion that takes in a string and returns a reversed copy of the string. The only
string operation you are allowed to use is string concatenation."""
print('--print reversed string')
def strReverse(mys):
    if mys=='':
        return mys
    return strReverse(mys[1:])+mys[0]
print(strReverse('Hello'))

"""Write a function using recursion to check if a number n is prime (you have to check whether n is divisible by
any number below n)."""
print('--Check if a number is prime')
def checkPrime(n,t):
   if n==0:
       return "Not prime"
   if n==1 or n==2:
       return "prime"
   if t==1:
       return "prime"
   if n%(t-1)==0:
       return "Not prime"
   if checkPrime(n, t - 1)=='Not prime':
       return "Not prime"
   print('a')
print('2 is', checkPrime(2,2))
print('3 is', checkPrime(3,3))
print('4 is', checkPrime(4,4))
print('21 is', checkPrime(21,21))
print('25 is', checkPrime(25,25))


"""Write a recursive function that takes in one argument n and computes Fn, the nth value of the Fibonacci
sequence. Recall that the Fibonacci sequence is defined by the relation Fn = Fn−1 + Fn−2
where F0 = 0 and F1 = 1"""
print('--Compute the Nth value of the fiboncci sequence')
def getFibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return getFibonacci(n-1)+getFibonacci(n-2)

print(getFibonacci(9))