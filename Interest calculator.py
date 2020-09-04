print("Interest calculator")


#Multiply money_start with 100 -> integers are exact, floats aren't because of the way the computer saves it. 
money_start = int(float(input("With how many money will you start?"))*100)
interest = float(input("What is the yearly interest?(in %)"))
nYears = int(input("How many years will you save the money?"))

#devide money_end by 100 -> money is back in euros.
money_end = (money_start*(1+(interest/100))**nYears)/100

print("After", nYears, "you'll have €", round(money_end,2))


close = input("Press enter to quit")
