from weather import *
myFile =  "weather.dat"
myChoice = 0
while(True):
    print("      *** TUFFY TITAN WEATHER LOGGER MAIN MENU")
    print()
    print("1. Set data filename")
    print("2. Add weather data")
    print("3. Print daily report")
    print("4. Print historical report")
    print("9. Exit the program")
    print()
    myChoice = int(input("Enter menu choice:"))
    print()
    if myChoice == 1:
        myFile = input("Enter data filename:")
        weather = read_data(filename = myFile)
    elif myChoice == 2:
        dt = input("Enter date (YYYYMMDD):")
        tm = input("Enter time (hhmmss):")
        t = int(input("Enter temperature:"))
        h = int(input("Enter humidity:"))
        r = float(input("Enter rainfall:"))
        weather[dt+tm] = {'t':t, 'h':h, 'r':r}
        write_data(data = weather, filename = myFile)
    elif myChoice == 3:
        d = input("Enter date (YYYYMMDD):")
        display = report_daily(data = weather, date = d)
        print(display)
    elif myChoice == 4:
        display = report_historical(weather)
        print(display)
    elif myChoice == 9:
        break
