Passengers = [['A1', 'Messi','DCMB- B12A1'], ['A2', 'Neymar', 'DCMB- B12A2'], ['A3', 'Rooney', 'DCMB- B12A3'], ['B2', 'Beckham', 'DCMB- B12B2'], ['B4', 'Eriksen', 'DCMB- B12B4'], ['C2', 'Kaka', 'DCMB- B12C2'], ['C3', 'Drogba', 'DCMB- B12C3'], ['C4','Sancho', 'DCMB- B12C4'], ['D1', 'Xavi', 'DCMB- B12D1'], ['D3', 'Iniesta', 'DCMB- B12D3']]
# Considering that all seats are vacant
Seats = [['A1','Vacant'], ['A2', 'Vacant'],['A3','Vacant'],['A4','Vacant'],['B1','Vacant'],['B2', 'Vacant'], ['B3', 'Vacant'], ['B4','Vacant'], ['C1', 'Vacant'], ['C2','Vacant'], ['C3','Vacant'], ['C4', 'Vacant'], ['D1', 'Vacant'], ['D2', "Vacant"],['D3','Vacant'],['D4','Vacant']]
# Updating the booking bus seat
for i in range (0, len(Passengers)):
  for j in range (0, len(Seats)):
    if Passengers [i][0] == Seats[j][0]:
      Seats[j][1] = 'Booked'
def ShowAllseats():
   for k in range (0, len(Seats)):
     print(f"Seat Number {Seats[k][0]} is {Seats[k][1]}")
def ShowAllVacants():
   print("List of all Vacant Seats: ")
   for k in range (0,len(Seats)):
     if Seats[k][1] == "Vacant":
      print(f"Seat Number {Seats[k][0]}")
def CheckingSeat():
  SeatCheck = input("Enter a seat number: ")
  Found = False
  for k in range (0,len(Seats)):
    if Seats[k][0] == CheckingSeat:
      print(f"Seat Number {Seats[k][1]}")
      Found = True
    if Found == False:
     print("The seat was not found.")
def BookingSeat():
   PassengerName = input("Enter your Name: ")
   Found = False
   Booked = False
   while Booked == False:
     ChooseSeat = input("Enter the seat you want to book: ")
     for k in range (0,len(Seats)):
       if Seats[k][1] == "Booked":
         print("Sorry, This seat is already booked,choose another one please.")
       else:
           print(f"Seat{Seats[k][0]} Booking successfull!!!")
   Ticket = "DCMB-B12" + Seats[k][0]
   NewBooking = [Seats[k][0]] = "Booked"
   if Found == False:
      print("This seat does not exit, thank you")
def CancelBooking():
    Cancel = False
    Found = False
    while Cancel == False:
      Cancelseat = input("Please enter the number of the seat you want to cancel: ")
      for k in range (0, len(Passengers)):
        if Passengers[k][0] == Cancelseat:
          Found = True
          Remove = k
          print(f"Seat{Passengers[k][0]} booking has been successfully cancelled.")
          Cancel = True
        if Found == False:
          print("The seat is not found.")
    Removed = Passenger.pop(Remove)
    print(Removed)
    return Cancelseat

    Option = 10
    print("1---> Showing the current status of all seat.")
    print("2---> Showing the seats which are vacant. ")
    print("3---> Cheking the current status of any seat.")
    print("4---> Booking a seat.")
    print("5---> Cancelling a booking.")

    while Option != 0:
       Option = int(input("What do you want to do? "))
       if Option == 1:
          ShowAllseats()
       elif Option == 2:
          ShowAllVacant()
       elif Option == 3:
          CheckingSeat()
       elif Optiob == 4:
          BookingSeat()
       elif Option == 5:
          ToVacate = CancelBooking()
          for i in range (0,len(Seats)):
            if Seats[i] [0] == Tovacate:
              Seats[i][0] = "Vacant"