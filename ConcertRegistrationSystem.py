registration_data = {
    "Name": [],
    "KTP": [],
    "Gender": [],
    "Age": [],
    "Ticket Type": []
}

def validate_name():
    while True:
        name = input("Enter name: ").strip()
        if len(name) == 0:
            print("❌ Name cannot be empty. Please try again.")
        else:
            return name.title()
        
def validate_ktp():
    KTP_LENGTH = 5
    while True:
        ktp = input(f"Enter KTP ({KTP_LENGTH} digits): ").strip()
        if len(ktp)==0:
            print("❌ KTP cannot be empty. Please try again.")
        elif len(ktp) != KTP_LENGTH:
            print(f"❌ KTP must be exactly {KTP_LENGTH} characters. You entered {len(ktp)}.")
        elif not ktp.isdigit():
            print(f"❌ KTP must contain only numbers. Please try again.")
        elif ktp in registration_data["KTP"]:
            print(f"❌ This KTP is already registered. Please enter a unique KTP.")
        else:
            return ktp

def validate_gender():
    VALID_GENDERS = ["male", "female"]
    while True:
        gender = input("Enter gender (Male/Female): ").strip().lower()
        if len(gender) == 0:
            print("❌ Gender cannot be empty. Please try again.")
        elif gender in VALID_GENDERS:
            return gender.capitalize()
        else:
            print("❌ Gender must be 'Male' or 'Female'. Please try again.")

def validate_age():
    while True:
        age_input = input("Enter age: ").strip()
        if len(age_input) == 0:
            print("❌ Age cannot be empty. Please try again.")
            continue

        try:
            age = int (age_input)
            if age <= 10:
                print("❌ Attendee must be older than 10. Please try again.")
            else:
                return age
        except ValueError:
            print("Please enter a valid number for age!")

def validate_ticket_type():
    VALID_TICKETS = ["vip", "regular", "student"]
    while True:
        ticket_type = input("Enter ticket type (VIP/Regular/Student): ").strip().lower()
        if len(ticket_type) == 0:
            print("❌ Ticket type cannot be empty. Please try again.")
        elif ticket_type in VALID_TICKETS:
            return ticket_type
        else:
            print("❌ Invalid ticket type. Please choose from VIP, Regular, or Student.")

def create_attendee():
    print("\n--- Register New Attendee ---")
    print("Please provide the following information:")
    name = validate_name()
    ktp = validate_ktp()
    gender = validate_gender()
    age = validate_age()
    ticket_type = validate_ticket_type()

    print("\nPlease Review the information:")
    print(f"    Name: {name}")
    print(f"    KTP: {ktp}")
    print(f"    Gender: {gender}")
    print(f"    Age: {age}")
    print(f"    Ticket Type: {ticket_type}")

    confirm = input("\nIs this information correct? (yes/no): ").strip().lower()
    if confirm == "yes":
        registration_data["Name"].append(name)
        registration_data["KTP"].append(ktp)
        registration_data["Gender"].append(gender)
        registration_data["Age"].append(age)
        registration_data["Ticket Type"].append(ticket_type)
        print(f"\n✅ SUCCESS! {name} has been registered for the concert!")
    else:
        print("\n ❌ Registration cancelled. Returning to main menu.")

def display_attendee_details(index):
    if 0 <= index < len(registration_data["Name"]):
        print(f"\n Registrant #{index + 1}:")
        print(f"    Name: {registration_data['Name'][index]}")
        print(f"    KTP: {registration_data['KTP'][index]}")
        print(f"    Gender: {registration_data['Gender'][index]}")
        print(f"    Age: {registration_data['Age'][index]}")
        print(f"    Ticket Type: {registration_data['Ticket Type'][index]}")
    else:
        print("Invalid index.")

def find_attendee_by_ktp(ktp_to_find):
    try:
        index = registration_data["KTP"].index(ktp_to_find)
        return index
    except ValueError:
        return None

def read_attendees():
    while True:
        print("\n--- View Registered Attendees ---")
        if not registration_data["Name"]:
            print("ℹ️ No attendees have been registered yet")
            input("Press Enter to return to the main menu:")
            break
        
        print("1. Show All Attendees")
        print("2. Find Attendee by KTP")
        print("3. Press Enter to return to the main menu...")
        sub_choice = input("Enter your choice (1-3): ").strip()

        if sub_choice == '1':
            print("\n--- All registered Attendees ---")
            for i in range(len(registration_data["Name"])):
                display_attendee_details(i)
            print("\n" + "-"*30)
            input("Press Enter to continue...")

        elif sub_choice == '2':
            ktp_to_find = input("Enter the KTP of the attendee: ").strip()
            index = find_attendee_by_ktp(ktp_to_find)
            if index is not None:
                display_attendee_details(index)
            else:
                print(f"❌ Attendee with KTP '{ktp_to_find}' not found")
                input("\nPress Enter to continue...")

        elif sub_choice == "3":
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 3.")

def get_ktp_for_search():
    KTP_LENGTH = 5
    while True:
        ktp_input = input(f"Enter the KTP of the attendee ({KTP_LENGTH}) digits: ").strip()
        if len(ktp_input) != KTP_LENGTH or not ktp_input.isdigit():
            print(f"❌ Invalid format. KTP must be {KTP_LENGTH} digits and contain only numbers.")
            retry = input("Would you like to try again? (yes/no): ").strip().lower()
            if retry != "yes":
                return None
        else:
            return ktp_input

def update_attendee():
    print("\n--- Update Attendee Information ---")
    if not registration_data["Name"]:
        print("ℹ️ No attendees to update.")
        return
    
    ktp_to_update = get_ktp_for_search()
    if ktp_to_update is None:
        print("Returning to main menu.")
        return
    
    index = find_attendee_by_ktp(ktp_to_update)
    if index is None:
        print(f"❌ Attendee with KTP '{ktp_to_update}' not found.")

    display_attendee_details(index)
    while True:
        print("\nWhich information would you like to update?")
        print("1. Name")
        print("2. Gender")
        print("3. Age")
        print("4. Ticket Type")
        print("5. Finish Updating")

        update_choice = input("Enter your choice (1-5): ").strip()
        if update_choice == "1":
            new_name = validate_name()
            registration_data["Name"][index] = new_name
            print("✅ Name updated successfully.")
        elif update_choice == "2":
            new_gender = validate_gender()
            registration_data["Gender"][index] = new_gender
            print("✅ Gender updated successfully.")
        elif update_choice == "3":
            new_age = validate_age()
            registration_data["Age"][index] = new_age
            print("✅ Age updated sucessfully.")
        elif update_choice == "4":
            new_ticket_type = validate_ticket_type()
            registration_data["Ticket Type"][index] = new_ticket_type
            print("✅ Ticket Type updated successfully.")   
        elif update_choice == "5":
            print("Returning to main menu.")
            break
        else:
            print("❌ Invalid choice.")   
        display_attendee_details(index)  

def delete_attendee():
    print("\n--- Delete Attendee Registration ---")
    if not registration_data["Name"]:
        print("ℹ️ No attendees to delete")
        return
    
    ktp_to_delete = get_ktp_for_search()
    if ktp_to_delete is None:
        print("Returning to main menu.")
        return
    
    index = find_attendee_by_ktp(ktp_to_delete)
    if index is None:
        print(f"❌ Attendee with KTP '{ktp_to_delete}' not found.")
        return

    display_attendee_details(index)
    confirm = input("\n⚠️ Are you sure you want to delete this record? This action cannot be undone. (yes/no): ").strip().lower()

    if confirm == "yes":
        name = registration_data["Name"].pop(index)
        registration_data["KTP"].pop(index)
        registration_data["Gender"].pop(index)
        registration_data["Age"].pop(index)
        registration_data["Ticket Type"].pop(index)
        print(f"✅ Registration for {name} has been deleted.")
    else:
        print("❌ Deletion cancelled.")

def main_menu():
    while True:
        print("\n" + "="*40)
        print(" 🎶 Concert Registration System 🎶")
        print("1. Register New Attendee (Create)")
        print("2. View Registered Attendees (Read)")
        print("3. Update Attendee Information (Update)")
        print("4. Delete Attendee Registration (Delete)")
        print("5. Exit")
        print("-"*40)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            create_attendee()
        elif choice == "2":
            read_attendees()
        elif choice == "3":
            update_attendee()
        elif choice == "4":
            delete_attendee()
        elif choice == "5":
            print("\n👋 Thank you for using the system. Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 5.")


main_menu()