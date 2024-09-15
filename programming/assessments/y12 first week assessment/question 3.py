minutes = int(input("enter number of minutes past midnight"))
hours = int(minutes/60)
minutesClock = int(((minutes/60) - hours) * 60)
if minutes == (0 or 1440):
    hours = "00"
    minutesClock = "00"

print(str(hours) + ":" + str(minutesClock))