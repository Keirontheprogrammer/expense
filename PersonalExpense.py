#Tracking expenses

def option():
    print("MAIN MENU")
    
    services =["Record Expenses", "View Expenses", "Monthly Summary", "Spending Alert"]
    for i, service in enumerate(services):
        print(f"{i+1}. {service}")
    choice = int(input("Choose the preferred service :"))

    def expense():
        while True:
                
                paid = (input("Amount spent : MKW "))

                try:
                    amount =float(paid)
                    if amount<0:
                         print("amount finna be a positive nummber")
                         continue
                except ValueError:
                     print("Please enter the amount in digits")
                     continue 
                allowed_categories=["food", "alcohol", "shopping", "traveling", "others"]

                while True:
                    category = input("whatchu spend it on ?(Food/Alcohol/Shopping/Traveling/ Others) : ").lower()

                    if category in allowed_categories:
                         break
                    print(f"Invalid category!!, Must one of these :{', '.join(allowed_categories)}")
                    
                                    
                print(f"MKW {amount} was spent on {category}")

                break
        
        new_record=input("Wanna log a new record? 'y/n :"   )

        if new_record == 'n':
             print("You logged out")
             return 
        else:
             expense()
        

    def view_records():
         #READING FROM SOME FILE#
         return
    
    
    match choice:
        case 1: 
               expense()            
        case 2:
            return
        case 3:
            return
        case 4:
            return
option()