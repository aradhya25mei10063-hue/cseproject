# cseproject
Vityarthi Project

Introduction: 
This project is a Python-based application designed 
to help vehicle owners track fuel efficiency and 
maintenance schedules. It provides an interactive 
menu to add trip data, calculate fuel efficiency, 
monitor maintenance dates, and visualize fuel 
efficiency trends over multiple trips. 
Problem Statement: 
Vehicle owners often find it difficult to manually 
track fuel usage and maintenance schedules. This 
project aims to automate and simplify these tasks, 
helping users maintain their vehicles efficiently and 
economically. 


Functional Requirements: 
Input vehicle details and last maintenance date. 
Add trip records with distance and fuel used. 
Calculate and display trip-specific and overall 
fuel efficiency. 
Track maintenance due date based on last 
maintenance. 
Generate a graph displaying fuel efficiency 
trends across trips. 
Provide a user-friendly menu for ease of 
operation 


Non-functional Requirements: 
The program should validate inputs, such as 
dates and numerical values. 
It must run in any standard Python 3 
environment with matplotlib installed. 
The interface is text-based for simplicity and 
compatibility. 
The system should handle errors gracefully 


System Architecture: 
The system follows a simple interactive loop 
architecture, where user input drives the flow. 
Core components include: 
Data input and validation 
Computation of efficiency 
Maintenance date calculations 
Data visualization with matplotlib

Design Decisions & Rationale: 
Chose a command-line interface for simplicity 
and portability. 
Used datetime for date validation and 
maintenance checks. 
Employed matplotlib for visual representation of 
efficiency trends. 
Input validation avoids crashes from invalid data 
entries. 


Implementation Details:  
The program starts by collecting vehicle 
information and validating the last maintenance 
date. 
Users input trip distances and fuel 
consumption; trip efficiency is calculated and 
stored. 
Overall fuel efficiency is computed 
cumulatively.  
Maintenance status is assessed by calculating 
days left until the next scheduled maintenance 
(180 days from last maintenance date). 
Fuel efficiency trends are displayed graphically 
using matplotlib 


Testing Approach: 
Tested with valid and invalid dates for last 
maintenance. 
Tested trip input with both normal and boundary 
values (e.g., zero fuel used).  
Verified calculations for trip and overall 
efficiency. 
Tested maintenance status for overdue and not 
overdue conditions. 
Confirmed chart displays accurately with 
multiple trip data.


Challenges Faced: 
Handling invalid date entries and other invalid 
inputs without program termination. 
Ensuring graphical output works across different 
platforms. 
Managing cumulative calculations correctly as 
new trips are added 


Learnings & Key Takeaways:  
Practical experience with Python input 
validation using exceptions. 
Hands-on use of datetime for scheduling 
calculations. 
Introduction to data visualization 
with matplotlib. 
Importance of user-friendly menu-driven 
program design


Future Enhancements: 
Adding persistent storage (e.g., file or database) to 
save trip and maintenance data. 
Extending to support multiple vehicles. 
Incorporating alerts/notifications for upcoming 
maintenance. 
Creating a graphical user interface (GUI) for 
improved usability 


References:  
Official Python Documentation: datetime and 
input handling. 
Matplotlib Documentation for plotting graphs. 
Online tutorials for building menu-based Python 
applications.
