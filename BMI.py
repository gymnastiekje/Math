print("Geef uw massa in kilogram: ")
massa_kg = float(input())
print("Geef uw lengte in meter: ")
lengte_m = float(input())
bmi = round(massa_kg / (lengte_m * lengte_m),1)
print("Uw BMI bedraagt: ", bmi, ".")
if bmi<18.5:
    print("U hebt ondergewicht.")

elif 18.5<=bmi<25:
    print("Uw gewicht is normaal.")

elif 25<=bmi<27:
    print("U heeft licht overgewicht.")

elif 27<=bmi<30:
    print("U heeft matig overgewicht.")

elif 30<=bmi<40:
    print("U heeft ernstig overgewicht.")

else:
    print("U heeft ziekelijk overgewicht.")

print("Druk op enter op af te sluiten.")
val = input()

