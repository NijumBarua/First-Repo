Passengers = [['A1', 'Messi','DCMB- B12A1'], ['A2', 'Neymar', 'DCMB- B12A2'], ['A3', 'Rooney', 'DCMB- B12A3'], ['B2', 'Beckham', 'DCMB- B12B2'], ['B4', 'Eriksen', 'DCMB- B12B4'], ['C2', 'Kaka', 'DCMB- B12C2'], ['C3', 'Drogba', 'DCMB- B12C3'], ['C4','Sancho', 'DCMB- B12C4'], ['D1', 'Xavi', 'DCMB- B12D1'], ['D3', 'Iniesta', 'DCMB- B12D3']]
Seats = [['A1','Vacant'], ['A2', 'Vacant'],['A3','Vacant'],['A4','Vacant'],['B1','Vacant'],['B2', 'Vacant'], ['B3', 'Vacant'], ['B4','Vacant'], ['C1', 'Vacant'], ['C2','Vacant'], ['C3','Vacant'], ['C4', 'Vacant'], ['D1', 'Vacant'], ['D2', "Vacant"],['D3','Vacant'],['D4','Vacant']]
for i in range (0, len(Passengers)):
 for j in range (0, len(Seats)):
    if Passengers [i][0] == Seats[j][0]:
      Seats[j][1] = 'Booked'
 PassengerName = input("Please enter your name: ")
 Found = False
 Booked = False
 while Booked == False:
  Choosingseat = input("Please enter the seat number you want to book: ")
  for k in range (0, len(Seats)):
    if Seats[k][0] == Choosingseat:
      Found = True
      if Seats[k][1] == "Booked":
        print("Sorry, This seat is already booked,choose another one please.")
      else:
        print(f"Seat{Seats[k][0]} Booking successfull!!!")
        Ticket = "DCMB-B12" + Seats[k][0]
        NewBooking = [Seats[k][0] , PassengerName, Ticket]
        Booked = True
        Passengers.append(NewBooking)
        Seats[k][1] = "Booked"
  if Found == False:
      print("This seat isn't available, thank you")