# FizzBuzz
# bikin 1 function 1 param => FizzBuzz
# bilangan kelipatan 3 => Fizz
# bilangan kelipatan 5 => Buzz
# bilangan kelipatan 3 dan 5 => FizzBuzz
def  FizzBuzz (x):
    for i in range (1, x+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0: 
            print('Fizz')
        elif i % 5 == 0: 
            print('Buzz')
        else: 
            print(i)

FizzBuzz (15)