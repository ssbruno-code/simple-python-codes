print("This software generates how many weeks of life you have if you leave 90 years")

def lifeWeeks(idade):
    lifeDays = int(idade * 365)
    weeksOfLife = round(int(lifeDays / 7))
    totalWeeks = round(int((90 * 365) / 7))
    output = totalWeeks - weeksOfLife
    print(f"You have {output} weeks of life untill your 90s")


lifeWeeks(int(input("Your age?(Only Numbers)")))

