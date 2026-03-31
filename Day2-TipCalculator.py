print('Welcome to tips calculator!')
Final_Bill = input('Enter your final bill\n')
Tip = input('How much do you want to tip?\n')
People = input('How many people to split the bill? \n')

tip_percent = int(Tip)/100
final_cal_tip = tip_percent * float(Final_Bill)

Total_bill =  final_cal_tip + float(Final_Bill)

Splitting = Total_bill/int(People)

Each_to_Pay = round(Splitting,2)


message = f" \n The total bill was: {Final_Bill} \n and a tip of {Tip}% making {Total_bill} split amongst {People} people\n Each person pays GHC: {Each_to_Pay}"
print(message)