import bcolors

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

print(bcolors.WARNING +"Interest calculator"+ bcolors.ENDC)

#Multiply money_start with 100 -> integers are exact, floats aren't because of the way the computer saves it. 
money_start = int(float(input(bcolors.FAIL+"With how many money will you start?"+bcolors.ENDC))*100)
interest = float(input(bcolors.FAIL+"What is the yearly interest?(in %)"+bcolors.ENDC))
nYears = int(input(bcolors.FAIL+"How many years will you save the money?"+bcolors.ENDC))

#devide money_end by 100 -> money is back in euros.
money_end = (money_start*(1+(interest/100))**nYears)/100

print(bcolors.OKGREEN + "After", nYears, " year(s) you'll have €", round(money_end,2), bcolors.ENDC)


close = input(bcolors.OKBLUE+"Press enter to quit"+bcolors.ENDC)
