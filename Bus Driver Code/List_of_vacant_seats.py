Passengers = [['A1', 'Messi','DCMB- B12A1'], ['A2', 'Neymar', 'DCMB- B12A2'], ['A3', 'Rooney', 'DCMB- B12A3'], ['B2', 'Beckham', 'DCMB- B12B2'], ['B4', 'Eriksen', 'DCMB- B12B4'], ['C2', 'Kaka', 'DCMB- B12C2'], ['C3', 'Drogba', 'DCMB- B12C3'], ['C4','Sancho', 'DCMB- B12C4'], ['D1', 'Xavi', 'DCMB- B12D1'], ['D3', 'Iniesta', 'DCMB- B12D3']]
Seats = [['A1','Vacant'], ['A2', 'Vacant'],['A3','Vacant'],['A4','Vacant'],['B1','Vacant'],['B2', 'Vacant'], ['B3', 'Vacant'], ['B4','Vacant'], ['C1', 'Vacant'], ['C2','Vacant'], ['C3','Vacant'], ['C4', 'Vacant'], ['D1', 'Vacant'], ['D2', "Vacant"],['D3','Vacant'],['D4','Vacant']]
for i in range (0, len(Passengers)):
 for j in range (0, len(Seats)):
    if Passengers [i][0] == Seats[j][0]:
      Seats[j][1] = 'Booked'
print("List of vacant seats: ")
for k in range (0,len(Seats)):
  if Seats[k][1] == "Vacant" :
      print(f"Seat Number {Seats[k][0]}")