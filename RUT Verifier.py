RUT = input("Enter RUT:")
sum = 0
times = 2
for largo in str(RUT):
    if times < 7:
         sum = sum + ((RUT%10) * times)
         times = times + 1
         RUT = RUT // 10
    if times == 7:
        sum = sum + ((RUT%10) * times)
        times = times + 1
        RUT = RUT // 10
        times = 2
verifier = 11 - (sum % 11)
if verifier == 10:
    verifier = "K"
if verifier == 11:
    verifier = 0
print("Verifier is " , verifier)
a = input("Press enter to close.")