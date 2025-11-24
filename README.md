Vehicle Fuel and Maintenance TrackerThis is a simple command-line Python program designed to help you track your vehicle's fuel consumption, calculate efficiency, and monitor maintenance schedules.✨ 

Features:
Trip Logging: Record the distance traveled and fuel used for each trip.
Fuel Efficiency: Calculates and displays the fuel efficiency for individual trips and the overall average efficiency.
Maintenance Tracking: Based on the last maintenance date, it calculates and shows the Next Due Date (assuming a 180-day interval) and the Days Remaining.
Data Visualization: Generates a Fuel Efficiency Chart using matplotlib to visualize the efficiency over recorded trips.
Error Handling: Includes basic date validation for the maintenance input.

Prerequisites:
To run this script, you need to have Python 3 installed, along with the following libraries:
datetime: Used for handling dates and calculating maintenance status (Standard library - no installation needed).
matplotlib: Used for generating the fuel efficiency chart.

How to Run:
1. Save the code below into a Python file such as tracker.py
2. open in your terminal or command line 
3. change into the directory you've saved the file in. 
4. Run the script : Bashpython tracker.py

Initial Setup:
The first time you run the script, it will ask you for initial vehicle details:    
including:
Vehicle name and model
Vehicle type - Car/Bike/etc.
Fuel tank capacity (in liters)
Last maintenance date (in the format YYYY-MM-DD)

Main Menu:
Once set up, the Menu will display, prompting you to select an action (1-5):
1.Add Trip: You can record the distance and fuel used for a new journey.
2.Check Fuel Efficiency: The overall average fuel efficiency in km/l will be displayed.
3.Maintenance Status: The last maintenance date, the next due date, and the days remaining will be displayed.
4.Fuel Efficiency Chart: A line chart displaying the efficiency history of your recorded trips will be shown.
5.Exit: The program will terminate. 

Code Overview:
Global Variables
vehiclename, vehicletype, fuelcapacity: These store the initial data about the vehicle. 
lastmaintdate: This holds the last maintenance date as a datetime.date object.
totaldistance, totalfuel: These variables accumulate the overall distance traveled and fuel consumed.
effhistory: This is a list to store the fuel efficiency in km/l of every trip recorded.

Key Logic:
1. Add Trip Records new distance and fuel data. eff = distance / fuelused
2. Check Fuel EfficiencyCalculates the average efficiency. avg = totaldistance / totalfuel
3. Maintenance StatusComputes next maintenance due date. datetime.timedelta(days=180)
4. Fuel Efficiency ChartPlots efficiency data. matplotlib.pyplot (plt)

Example Workflow:
1.Start the program.
2.Input vehicle details like Vehicle name and model: Honda Civic, Last maintenance date: 2025-05-01.
3.Choose 1. Add Trip. 
4.Input: Distance travelled: 350, Fuel used : 20. - Output is Trip Efficiency: 17.5 km/l.
5.Choose 3. Maintenance Status. - Output is Next Due date is 180 days after 2025-05-01 
6.Choose 4. Fuel Efficiency Chart to view the graph for the single trip.


output screenshot:
<img width="1416" height="866" alt="image" src="https://github.com/user-attachments/assets/6a075361-22fe-494d-960c-d968cbfe4ce7" />

flowchart:
<img width="885" height="792" alt="image" src="https://github.com/user-attachments/assets/8585464f-bfbc-4fda-b429-454aa0fb07c7" />

