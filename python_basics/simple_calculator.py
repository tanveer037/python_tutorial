print('This is a very simple calculator that can only do adding, substracting, multiplying and deviding for two numbers')
print('Your options are "add", "substract", "multiply", "Divide"')
print('Any other command will return invalid command statement')

def adding(x,y):
    return x + y

def substracting(x,y):
    return x - y

def multiplying(x,y):
    return x*y

def dividing(x,y):
    return x/y

def taking_input():
    print('Now enter your inputs')
    x = int(input("Enter your first input "))
    y = int(input("Enter your second input "))
    return x,y

action = input('What you want to do? ')

if action == 'add':
    x,y = taking_input()
    print(adding(x,y))
    
elif action == 'substract':
    x,y = taking_input()
    print(substracting(x,y))
    
elif action == 'multiply':
    x,y = taking_input()
    print(multiplying(x,y))

elif action == 'divide':
    x,y = taking_input()
    print(dividing(x,y))

else: print('Invalid input')