hours = int(input("enter numbero f hours"))
minutes = int(input("enter number of minutes"))
amOrPm = input("am or pm")
totalMinutes = (hours * 60) + minutes
if amOrPm == "pm":
    totalMinutes += (12 * 60)

print(totalMinutes)
