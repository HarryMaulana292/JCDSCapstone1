main_data = {
    "ABC123" : {
        "Patient Number" : "ABC123",
        "Name" : "Hermoine Granger",
        "Sex" : "Female",
        "Age" : 28,
        "Disease" : "Hepatitis"},
    "DEF456" : {
        "Patient Number" : "DEF456",
        "Name" : "Ron Weasley",
        "Sex" : "Male",
        "Age" : 36,
        "Disease" : "Typus"},
    "GHI789" : {
        "Patient Number" : "GHI789",
        "Name" : "Harry Potter",
        "Sex" : "Male",
        "Age" : 33,
        "Disease" : "Hypertension"},
    "JKL012" : {
        "Patient Number" : "JKL012",
        "Name" : "Tom Riddle",
        "Sex" : "Male",
        "Age" : 40,
        "Disease" : "Diabetes"},
    "MNO345" : {
        "Patient Number" : "MNO345",
        "Name" : "Luna Lovegood",
        "Sex" : "Female",
        "Age" : 32,
        "Disease" : "Hyperosmia"}
    }

line = "----------------------------------------------------------------------------"
def main_table():
    print (f"{'Patient Number':<16}| {'Name':<32}| {'Sex':<8}| {'Age':<5}| Disease")
    for key, val in main_data.items():
        print (f"{main_data[key]['Patient Number']:<16}| {main_data[key]['Name']:<32}| {main_data[key]['Sex']:<8}| {main_data[key]['Age']:<5}| {main_data[key]['Disease']}")

def main_menu():
    print (line)
    print ("                        Welcome to Racoon Hospital                          ")
    print (line)
    print ("~ MAIN MENU ~")
    print ("1. Read Data")
    print ("2. Create Data")
    print ("3. Update Data")
    print ("4. Delete Data")
    print ("5. Exit Program")
    main_menu_input = input("Input : ")
    if main_menu_input.isdigit():
        if int(main_menu_input) == 1:
            read_data()
        elif int(main_menu_input) == 2:
            create_data()
        elif int(main_menu_input) == 3:
            update_data()
        elif int(main_menu_input) == 4:
            delete_data()
        elif int(main_menu_input) == 5:
            exit_program()
    else :
        print ("Your choice is not exist")
        main_menu()

def read_data():
    print(line)
    print ("~ MAIN MENU | READ DATA ~")
    print ("1. Show all data")
    print ("2. Find data")
    print ("3. Back to Main Menu")
    read_data_input = input("Input : ")
    if read_data_input.isdigit():
        if int(read_data_input) == 1:
            print(line)
            print ("~ MAIN MENU | READ DATA | SHOW ALL DATA ~")
            show_data()
        elif int(read_data_input) == 2:
            print(line)
            print ("~ MAIN MENU | READ DATA | FIND DATA ~")
            find_data()
        elif int(read_data_input) == 3:
            main_menu()
        else:
            read_data()
    else :
        read_data()

def show_data():
    if len(main_data) == 0:
        print ("Data is not exist")
    else :
        main_table()
    read_data()
    
def find_data():
    if len(main_data) == 0:
        print ("Data is not exist")
    else :
        prim_key = input("Input Patient Number : ").upper()
        if prim_key in main_data:
            print (f"{'Patient Number':<16}| {'Name':<32}| {'Sex':<8}| {'Age':<5}| Disease")
            print (f"{main_data[prim_key]['Patient Number']:<16}| {main_data[prim_key]['Name']:<32}| {main_data[prim_key]['Sex']:<8}| {main_data[prim_key]['Age']:<5}| {main_data[prim_key]['Disease']}")
        else :
            print ("Data is not exist")
    read_data()
    
def create_data():
    print(line)
    print ("~ CREATE DATA ~")
    print ("1. Add data")
    print ("2. Back to Main Menu")
    create_data_input = input("Input : ")
    if create_data_input.isdigit():
        if int(create_data_input) == 1:
            print(line)
            print ("~ CREATE DATA | ADD DATA ~")
            add_data()
        elif int(create_data_input) == 2:
            main_menu()
        else :
            create_data()
    else :
        create_data()

def add_data():
    new_prime_key = input("Input Patient Number : ")
    while True:
        if len(new_prime_key) <= 7 and len(new_prime_key) > 0:
            new_prime_key = new_prime_key.upper()
            break
        else:
            print ("Patient number cannot be more than 7 character")
            new_prime_key = input("Input Patient Number : ")
    if new_prime_key in main_data:
        print ("Data already exist")
    else :
        new_name = input ("Input Name : ")
        while True:
            for word in new_name.split():
                if word.isalpha():
                    status = True
                else :
                    status = False
                    break
            if len(new_name) == 0 or status == False:
                print ("Data must not be empty and must be alphabet")
                new_name = input ("Input Name : ")
            elif status == True:
                break

        new_name_splitted = new_name.split()
        cap_new_name = []
        if len(new_name) > 30:
            for idx,val in enumerate (new_name_splitted):
                if idx == 0 or idx == 1 or idx == 2:
                    cap_new_name.append((new_name_splitted[idx]).capitalize())
                else :
                    cap_new_name.append((new_name_splitted[idx][0]).capitalize())
            new_name = " ".join(cap_new_name)    
        else :
            new_name = new_name.title()
        
        new_sex = input ("Input Sex (Male/Female) : ").capitalize()
        while True:
            if new_sex == "Male" or new_sex == "Female":
                break
            else :
                new_sex = input ("Input Sex (Male/Female) : ").capitalize()            
        
        new_age = input ("Input Age : ")
        while not new_age.isdigit():
            new_age = input ("Input Age (must be number): ")
        new_age = int(new_age)
        
        new_disease = input ("Input Disease : ")
        while True:
            if len(new_disease) > 0:
                new_disease = new_disease.title()
                break
            else :
                print ("Data must not be empty")
                new_disease = input ("Input Disease : ").split()
                
        print ("\n")
        print (f"{'Patient Number':<16}| {'Name':<32}| {'Sex':<8}| {'Age':<5}| Disease")
        print (f"{new_prime_key:<16}| {new_name:<32}| {new_sex:<8}| {new_age:<5}| {new_disease}")
        
        save = input ("Save data (yes/no) ? ").lower()
        while True:
            if save == "yes":
                new_data = {}
                new_data["Patient Number"] = new_prime_key
                new_data["Name"] = new_name
                new_data["Sex"] = new_sex
                new_data["Age"] = new_age
                new_data["Disease"] = new_disease
                main_data[new_prime_key] = new_data
                print ("New data has been saved")
                break
            elif save == "no":
                break
            else :
                save = input ("Save data (yes/no) ? ").lower()
    create_data()
            
def update_data():
    print(line)
    print ("~ UPDATE DATA ~")
    print ("1. Change data")
    print ("2. Back to Main Menu")
    update_data_input = input("Input : ")
    if update_data_input.isdigit():
        if int(update_data_input) == 1:
            print(line)
            print ("~ UPDATE DATA | CHANGE DATA ~")
            change_data()
        elif int(update_data_input) == 2:
            main_menu()
        else :
            update_data()
    else :
        update_data()
                 
def change_data():
    main_table()
    prime_key = input("Input Patient Number : ").upper()
    if prime_key in main_data:
        print (f"{'Patient Number':<16}| {'Name':<32}| {'Sex':<8}| {'Age':<5}| Disease")
        print (f"{main_data[prime_key]['Patient Number']:<16}| {main_data[prime_key]['Name']:<32}| {main_data[prime_key]['Sex']:<8}| {main_data[prime_key]['Age']:<5}| {main_data[prime_key]['Disease']}")
        update1 = input("Continue to update (yes/no) ? ").lower()
        while True:
            if update1 == "yes":
                column_update = input ("Choose column to update : ").split()
                cap_column_update = []
                for word in column_update :
                    cap_column_update.append (word.capitalize())
                column_update = " ".join(cap_column_update)
                while not column_update in main_data [prime_key]:
                    print ("Column is not exist")
                    column_update = input ("Choose column to update : ").split()
                    cap_column_update = []
                    for word in column_update :
                        cap_column_update.append (word.capitalize())
                    column_update = " ".join(cap_column_update)

                while True :
                    new_data = input("Input new data : ")
                    if len(new_data) == 0:
                        print ("Data must not be empty")
                    elif column_update == "Age":
                        while not new_data.isdigit():
                            new_data = input("Input new data (must be number): ")
                        new_data = int(new_data)
                        break
                    elif column_update == "Name":
                        while True:
                            for word in new_data.split():
                                if word.isalpha():
                                    status = True
                                else :
                                    status = False
                                    break
                            if len(new_data) == 0 or status == False:
                                print ("Data must not be empty and must be alphabet")
                                new_data = input ("Input Name : ")
                            elif status == True:
                                break
                        new_data_splitted = new_data.split()
                        cap_new_data = []
                        if len(new_data) > 30:
                            for idx,val in enumerate (new_data_splitted):
                                if idx == 0 or idx == 1 or idx == 2:
                                    cap_new_data.append((new_data_splitted[idx]).capitalize())
                                else :
                                    cap_new_data.append((new_data_splitted[idx][0]).capitalize())
                            new_data = " ".join(cap_new_data)    
                        else :
                            new_data = new_data.title()
                        break
                    elif column_update == "Disease":
                        new_data = new_data.title()
                        break
                    elif column_update == "Sex":
                        while True:
                            new_data = new_data.capitalize() 
                            if new_data == "Male" or new_data == "Female":
                                break
                            else :
                                new_data = input ("Input Sex (Male/Female) : ").capitalize()
                        break
                    elif column_update == "Patient Number":
                        while True:
                            while True:
                                if len(new_data) <= 7 and len(new_data) > 0:
                                    new_data = new_data.upper()
                                    break
                                else:
                                    print ("Patient number cannot be more than 7 character")
                                    new_data = input("Input Patient Number : ")
                            if new_data in main_data:
                                print ("Data already exist")
                                new_data = input("Input Patient Number : ")
                            else :
                                break
                        break
                update2 = input ("Save update data (yes/no) ? ").lower()
                while True:
                    if update2 == "yes":
                        if column_update == "Patient Number":
                            main_data[new_data] = {
                                "Patient Number" : new_data, 
                                "Name" : main_data[prime_key]["Name"], 
                                "Sex" : main_data[prime_key]["Sex"], 
                                "Age" : main_data[prime_key]["Age"], 
                                "Disease" : main_data[prime_key]["Disease"]}
                            del main_data [prime_key]
                        else:
                            main_data[prime_key][column_update] = new_data
                        print ("Data has been updated")
                        break
                    elif update2 == "no":
                        break
                    else :
                        update2 = input ("Save data (yes/no) ? ").lower()
                break
            elif update1 == "no":
                break
            else :
                update1 = input ("Continue to update (yes/no) ? ").lower()
    else :
        print ("Data is not exist")
    update_data()

def delete_data():
    print(line)
    print ("~ DELETE DATA ~")
    print ("1. Remove data")
    print ("2. Back to Main Menu")
    delete_data_input = input("Input : ")
    if delete_data_input.isdigit():
        if int(delete_data_input) == 1:
            print(line)
            print ("~ DELETE DATA | REMOVE DATA ~")
            remove_data()
        elif int(delete_data_input) == 2:
            main_menu()
        else :
            delete_data()
    else :
        delete_data()

def remove_data():
    main_table()
    prime_key = input("Input Patient Number : ").upper()
    if prime_key in main_data:
        print (f"{'Patient Number':<16}| {'Name':<32}| {'Sex':<8}| {'Age':<5}| Disease")
        print (f"{main_data[prime_key]['Patient Number']:<16}| {main_data[prime_key]['Name']:<32}| {main_data[prime_key]['Sex']:<8}| {main_data[prime_key]['Age']:<8}| {main_data[prime_key]['Disease']}")
        delete = input ("Delete this data (yes/no) ? ").lower()
        while True:
            if delete == "yes":
                del main_data[prime_key]
                print ("Data has been deleted")
                break
            elif delete == "no":
                break
            else :
                delete = input ("Save data (yes/no) ? ").lower()
    else :
        print("Data is not exist")
    delete_data()

def exit_program():
    global x
    x = 0    

x = 1
while x == 1 :
    main_menu()