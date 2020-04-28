def fizzbuzz(n):
    if n % 5 == 0 & n % 3 == 0:
        print("FizzBuzz!")
    elif n % 3 == 0:
        print("Fizz!")
    elif n % 5 == 0:
        print("Buzz!")

fizzbuzz(30)
