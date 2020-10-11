import random
loop = 0
while True:
    number = random.randint(0,4496388)
    if number == 1:
        print number
        print 'After',loop,'attempts, and spending $',(loop*3000),'you finally won the lottery!'
        break
    else:
        loop = loop + 1
        print number
input("Press enter to close.")