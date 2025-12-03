print("----- AQUILA-1 : UAV Mission Health Scoring Engine -----")
print("Please enter task parameters ")

battery=int(input("battery level (%):  "))
gps=int(input("Gps signal quality (1-100):   "))
temperature=int(input("temperaturee(°C):   "))
wind=int(input("wind level(0-100) :     "))
route=int(input("route stability (0-100):    "))
motor_temp=int(input("motor temperature (0-100)"))
altitude_acc=int(input("altitude accuary (0-100):    "))
speed_stab=int(input("speed stability(0-100)"))

print("\n\n\n\n\n CALCULATİNG MİSSİON HEALTH SCORE\n")
score =0

if battery>70:
    score+=20
elif battery>40:
    score+=10

if gps>80:
    score+=15
elif gps>50:
    score+=7

if 20 <= temperature <= 45:
    score += 15
elif 10 <= temperature < 20 or 45 < temperature <= 55:
    score += 5

if wind < 30:
    score += 10
elif wind < 60:
    score += 5

if route > 75:
    score += 10
elif route > 50:
    score += 5

if motor_temp < 60:
    score += 10
elif motor_temp < 80:
    score += 5

if altitude_acc > 80:
    score += 5

if speed_stab > 80:
    score += 5

print(f"total mission score :{score}/90")

if score >= 70:
    status = "SAFE ✅"
elif score >= 40:
    status = "RISKY ⚠️"
else:
    status = "CRITICAL ❌"

print(f"mission status: {status}")
print("\nAQUILA-1 Analysis Complete.")