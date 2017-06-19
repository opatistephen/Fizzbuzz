def fizzbuz():

    while True:

      print("Enter the checkNum")
      checkNum=int(input())

      if checkNum%3!=0 and checkNum%5!=0:
        print('Oop! The number does not match the criterion please try again')
        continue
      #print("Enter the checkNum")
      #else:5

      if checkNum%5==0 and checkNum%3==0:
        print("FizzBuz")
      elif checkNum%5==0:
        print("Buzz")
      elif checkNum%3==0:
        print("Fizz")
      else:
        print("checkNum")
      break

fizzbuz()