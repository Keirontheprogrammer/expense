import datetime
#Tracking expenses

def option():
    print("="*20,"MAIN MENU", "="*20)
    
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

                try :
                 with open("expenses.txt", "a") as file:
                    time =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    file.write(f"{time}, {amount}, {category}\n")
                    print(f"\nRecorded: MKW {amount:.2f} on {category.capitalize()}")
                except ValueError:
                        print("Error writing to file")      
               

                break
        
        new_record=input("Wanna log a new record? 'y/n :"   )

        if new_record == 'n':
             print("You logged out")
             return 
        else:
             expense()
    

        

    def view_records():
        try:
            with open("expenses.txt", "r") as file:
                records=file.readlines()
                if not records :
                    print("No recorded data found")
                    return
            print("Your records are :")
            print("-"*3,"DATE","-"*3 ," ","-"*2, "TIME","-"*2, " ", "| AMOUNT (MKW) | CATEGORY |")
           
            for record in records:
                print(record.strip())
        except FileNotFoundError:
            print("No records found-File does not exist")

        while True:
         manage_records =["Delete records", "Exit"]
         for i, manage in enumerate(manage_records):
          print(f"{i+1}. {manage}")
         try:
          action = int(input("Choose an action :"))
         except ValueError:
          print("Please enter a valid number")

          match action:
           case 1:
                confirm = input("Are you sure you want to delete all records? (y/n): ").lower()
                if confirm == 'y':
                  open("expenses.txt","w").close()   
                  print("Records deleted successfully :)")
                else:
                    print("Failed to delete records")         
           case 2:
                  print("You logged out")
                  break
           case _:
                  print("Invalid choice, please choose a valid option")
                  continue
         break

    def monthly_summary():
         print("Monthly summary coming right up")
    def spending_alert():
        print("Spending alerts coming right up")
    
    
    match choice:
        case 1: 
               expense()            
        case 2:
            view_records()
        case 3:
            monthly_summary()
        case 4:
             spending_alert()
option()