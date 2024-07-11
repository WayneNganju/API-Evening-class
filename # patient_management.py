# patient_management.py

def add_patient(patients):
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    illness = input("Enter patient's illness: ")
    patients.append({'name': name, 'age': age, 'illness': illness})

def display_patients(patients):
    if not patients:
        print("No patients in the system.")
    for patient in patients:
        print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")

def search_patient(patients, name):
    for patient in patients:
        if patient['name'] == name:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
            return
    print("Patient not found.")

def remove_patient(patients, name):
    for patient in patients:
        if patient['name'] == name:
            patients.remove(patient)
            print("Patient removed.")
            return
    print("Patient not found.")

def main():
    patients = []
    while True:
        print("\n1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_patient(patients)
        elif choice == '2':
            display_patients(patients)
        elif choice == '3':
            name = input("Enter patient's name to search: ")
            search_patient(patients, name)
        elif choice == '4':
            name = input("Enter patient's name to remove: ")
            remove_patient(patients, name)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
