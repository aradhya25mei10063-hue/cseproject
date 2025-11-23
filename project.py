import datetime
import matplotlib.pyplot as plt

print("Vehicle Fuel and Maintenance Tracker")

#basic data
vehiclename = input("Vehicle name and model: ")
vehicletype = input("Vehicle type (Car/Bike/etc): ")
fuelcapacity = float(input("Fuel tank capacity (liters): "))
lastmaintenance = input("Last maintenance date (YYYY-MM-DD): ")

#date conversion
try:
    lastmaintdate = datetime.datetime.strptime(lastmaintenance, "%Y-%m-%d").date()
except:
    print("Invalid date entered, using today's date we proceed further ")
    lastmaintdate = datetime.date.today()

totaldistance = 0     #to store distance 
totalfuel = 0      #to store fuel 
effhistory = []      # to store efficiency of each trip

#main menu loop
while True:
    print("Menu:")
    print("1.Add Trip")
    print("2.Check Fuel Efficiency")
    print("3.Maintenance Status")
    print("4.Fuel Efficiency Chart")
    print("5.Exit")

    choice = input("Choose (1-5): ")

    #add trip
    if choice == "1":
        distance = float(input("Distance travelled (km): "))
        fuelused = float(input("Fuel used (liters): "))

        if fuelused > 0:
            efficiency = distance / fuelused
            print(f"Trip Efficiency: {efficiency} km/l")
            effhistory.append(efficiency)
        else:
            print("Fuel used must be greater than 0")
            continue

        totaldistance += distance
        totalfuel += fuelused

    #show overall efficiency
    elif choice == "2":
        if totalfuel > 0:
            avg = totaldistance / totalfuel
            print(f"Overall Efficiency: {avg:} km/l")
        else:
            print("No trip data recorded yet.")

    #maintenance check
    elif choice == "3":
        nextdue = lastmaintdate + datetime.timedelta(days=180)
        daysleft = (nextdue - datetime.date.today()).days

        print(f"Last Maintenance: {lastmaintdate}")
        print(f"Next Due: {nextdue}")

        if daysleft > 0:
            print(f"{daysleft} days remaining.")
        else:
            print("Maintenance overdue.")

    #fuel efficiency chart
    elif choice == "4":
        if len(effhistory) == 0:
            print("No trip data to display chart.")
        else:
            trips = list(range(1, len(effhistory) + 1))
            plt.plot(trips, effhistory, marker='o')
            plt.xlabel("Trip Number")
            plt.ylabel("Efficiency (km/l)")
            plt.title("Fuel Efficiency Chart")
            plt.grid(True)
            plt.show()

    #exit
    elif choice == "5":
        print("Exiting program")
        break

    else:

        print("Invalid option")
