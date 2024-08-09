# Create a Computation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.

# Create a method called Factorial() which allows to calculate the factorial of an integer n. Integer n as parameter for this method

# Create a method called naturalSum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Integer n as parameter for this method.

# Create a method called testPrime() in the Calculation class to test the primality of a given integer n, n is Prime or Not? Integer n as parameter for this method.

# Create a method called testPrims() allowing to test if two numbers are prime between them. Two integers are prime to one another if they have only 1 as their common divisor. Eg. 4 and 9 are prime to each other.

# Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.

# Create a static listDiv() method that gets all the divisors of a given integer on new list called Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer
import math

class Computation():
    def __init__(self):
        pass # No need to initialize anything in default constructor...

    def Factorial(self, n):
      if n <= 1 or n == 0:
        return 1
      else:
        return n * self.Factorial(n-1)
    
    def naturalSum(self, n):
      sum = 0
      for i in range(1, n + 1):
        sum +=i
      return sum
    
    
    def testprime(self, n):
      if isinstance(n, int):
        count= 0
        i = 1
        while (i<=n):
          if n%i==0:
            count += 1
          i += 1
        if count ==2:
          print("Prime")
        else:
          print("Not Prime")
      else:
        print("Error")

    def numbetween(self, a, b):
      if isinstance(a, int) and isinstance(b, int):
        gcd = math.gcd(a, b)

        if gcd == 1:
          print("Number are prime to each other")
        else:
          print("Number are not prime to each other")
      else:
        print("Invalid input")

    def tableMult(self, a):
      if isinstance(a, int):
        for i in range(1, 11):
          print(f"{a} x {i} = {i*a}")

    def allTablesMult(self):
      print("Multiplication Tables from 1 to 9:")
      for i in range(1, 11):
        for j in range(1, 11):
          print(f"{i} x {j} = {i*j}")


    def listdiv(self, a):
      if isinstance(a, int):
        num =[]
        for i in range(1, a+1):
          if a % i == 0:
            num.append(i)
        return num
      else:
        print('Invalid Input')