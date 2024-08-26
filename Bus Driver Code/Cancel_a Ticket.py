Passengers = [['A1', 'Messi','DCMB- B12A1'], ['A2', 'Neymar', 'DCMB- B12A2'], ['A3', 'Rooney', 'DCMB- B12A3'], ['B2', 'Beckham', 'DCMB- B12B2'], ['B4', 'Eriksen', 'DCMB- B12B4'], ['C2', 'Kaka', 'DCMB- B12C2'], ['C3', 'Drogba', 'DCMB- B12C3'], ['C4','Sancho', 'DCMB- B12C4'], ['D1', 'Xavi', 'DCMB- B12D1'], ['D3', 'Iniesta', 'DCMB- B12D3']]
Seats = [['A1','Vacant'], ['A2', 'Vacant'],['A3','Vacant'],['A4','Vacant'],['B1','Vacant'],['B2', 'Vacant'], ['B3', 'Vacant'], ['B4','Vacant'], ['C1', 'Vacant'], ['C2','Vacant'], ['C3','Vacant'], ['C4', 'Vacant'], ['D1', 'Vacant'], ['D2', "Vacant"],['D3','Vacant'],['D4','Vacant']]
for i in range (0, len(Passengers)):
 for j in range (0, len(Seats)):
    if Passengers [i][0] == Seats[j][0]:
      Seats[j][1] = 'Booked'
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
Removed = Passengers.pop(Remove)
print(Removed)