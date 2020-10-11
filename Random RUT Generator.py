import random
while True:
    RUT = random.randint(1000000 , 22999999)
    RUT1 = RUT
    sum = 0
    times = 2
    for largo in str(RUT1):
        if times < 7:
             sum = sum + ((RUT1%10) * times)
             times = times + 1
             RUT1 = RUT1 // 10
        if times == 7:
            sum = sum + ((RUT1%10) * times)
            times = times + 1
            RUT1 = RUT1 // 10
            times = 2
    verifier = 11 - (sum % 11)
    if verifier == 10:
        verifier = "K"
    if verifier == 11:
        verifier = 0
    print 'RUT is: ',str(RUT),'-',str(verifier)