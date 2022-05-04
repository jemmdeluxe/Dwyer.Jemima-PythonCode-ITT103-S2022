# Author: Jemima Dwyer
#- Date Created: 4/8/2022
#- Course: ITT103
#- Purpose: <To calculate the commission received by employees. To avoid tedious calculates by users.>

salepId = int(input("Enter your Sales Person ID number: " ))
while salepId < 10000:
    print(input("Please enter valid a valid Sales Person ID."))
    break
if salepId >= 10000 and salepId <= 11501:
    salepId == True
else:
    salepId == False
    print("ERROR!! Invalid Sales Person ID. Try again or contact your supervisor. Thank you.")
salepId = ("JEx"+str(salepId))

sales_amnt = int(input("Enter the amount of sales : "))
classTp = int(input("Enter Class Type : "))

"To calcultate the emplyee's commission who are under the Class number 1."

while classTp == 1:
    if sales_amnt <= 1000:
        comAmount = int(.06 * sales_amnt)
        print("For",str(saleNo)+ " your commission is", + int(comAmount))
        break
    elif sales_amnt > 1000 and sales_amnt < 2000:
        comAmount =   int(.07 * sales_amnt)
        print("For",str(saleNo)+ " your commission is", + int(comAmount))
        break
    else: 
        sales_amnt >= 2000
        comAmount =  int(.1 * sales_amnt)
        print("For",str(salepId)+ " your commission is", + int(comAmount))
        break
        pass

"To calcultate the emplyee's commission who are under the Class number 2."

while classTp == 2:
    if sales_amnt < 1000:
        comAmount = int(.04 * sales_amnt)
        print("For",str(salepId)+ " your commission is", + int(comAmount))
        break
    else:
        sales_amnt <= 1000
        comAmount = int(.06 * sales_amnt)
        print("For",str(salepId)+ " your commission is", + int(comAmount))
        break
    
"To calcultate the emplyee's commission who are under the Class number 3."

while classTp == 3:
    comAmount = int(.06 * sales_amnt)
    print("For",str(salepId)+ " your commission is", + int(comAmount))
    break

"Error message for class the do Not exsist in the programme."

if classTp >= 4:
    print("Error invalid Class. Please Try again.")
