import random
print('Hello, What is your name?')
name = input()
print('well ' + name +' , are you able to guess my no in the mind between 1 and 20')
secretnumber = random.randint(1,20)
for guesstaken in range(1,9):
    print('Take a guess')
    guess = int(input())

    if guess < secretnumber:
        print("too low")
    elif guess > secretnumber:
        print('too high') 
    elif guess == secretnumber:
        print("Well done!!!") 
        break  

print('you took  ' + str(guesstaken)+ ' guess and the correct number is ' + str(secretnumber)) 