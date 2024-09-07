# compound interest

principal = 0
time = 0
rate = 0

while True:
    principal = float(input("Enter the principal: "))
    if principal < 0:
        print("Principal must not be less than zero.")
    else:
        break

while True:
    time = int(input("Enter the time: "))
    if time < 0:
        print("Time must not be less than zero.")
    else:
        break

while True:
    rate = float(input("Enter the rate: "))
    if rate < 0:
        print("Rate must not be less than zero.")
    else:
        break

total = principal * pow((1 + rate/100), time)
compoundInterest = total - principal

print(f"Your compound interest of ${principal} at the rate of {rate}% for a period of {time} year/s is: {compoundInterest:.2f}")