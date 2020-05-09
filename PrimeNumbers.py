import IsPrime
import os
is_prime = IsPrime.is_prime

print(is_prime(1))

_ = os.system("clear")

print("""Hello I'm the PrimeNumberAtron 3000

	      Menu

  0) Check if a number is prime
  1) List prime numbers up to any number
  2) Play global thermonuclear war
  """)
mode = int(input(""))
if mode == 0:
  number = int(input("What number would you like to check?"))
  if is_prime(number):
    print("It is prime")
  else:
    print ("It is not prime")

if mode == 1:
  checkToNumber = int(input("What number would you like to list numbers up to?"))
  checkToNumberList = list(range(1,checkToNumber))
  for number in checkToNumberList:
    if is_prime(number):
      print(number)
      
if mode == 2:
  _ = input("Are you sure (Y/N)?")
  _ = input("What about a nice game of chess (Y/N)?")
  _ = input("What about the children (Y/N)?")
  print("Launching in 3, 2, 1")