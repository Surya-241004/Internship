from CRUD import SafetyRecordManager

class StadiumSafetyConsole:
    def __init__(self):
        self.manager = SafetyRecordManager()

    def run(self):
        while True:
            print("\n--- Stadium Safety Inspection Tool ---")
            print("1. Create Safety Record")
            print("2. View Safety Records")
            print("3. Update Safety Record")
            print("4. Delete Safety Record")
            print("5. Conduct Safety Audit")
            print("6. Manage Safety Improvements")
            print("7. View Safety Improvements")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                stadium_id = int(input("Enter Stadium ID: "))
                hazard = input("Enter Hazard Description: ")
                severity = input("Enter Severity (Low/Medium/High): ")
                print(self.manager.create_safety_record(stadium_id, {'hazard': hazard, 'severity': severity}))

            elif choice == "2":
                stadium_id = int(input("Enter Stadium ID to view records: "))
                records = self.manager.read_safety_records(stadium_id)
                print(records)

            elif choice == "3":
                stadium_id = int(input("Enter Stadium ID: "))
                records = self.manager.read_safety_records(stadium_id)
                print(records)
                record_id = int(input("Enter Record ID to update: "))
                hazard = input("Enter Updated Hazard: ")
                severity = input("Enter Updated Severity (Low/Medium/High): ")
                print(self.manager.update_safety_record(stadium_id, record_id, {'hazard': hazard, 'severity': severity}))

            elif choice == "4":
                stadium_id = int(input("Enter Stadium ID: "))
                records = self.manager.read_safety_records(stadium_id)
                print(records)
                record_id = int(input("Enter Record ID to delete: "))
                print(self.manager.delete_safety_record(stadium_id, record_id))

            elif choice == "5":
                stadium_id = int(input("Enter Stadium ID for audit: "))
                print(self.manager.conduct_safety_audit(stadium_id))

            elif choice == "6":
                stadium_id = int(input("Enter Stadium ID: "))
                improvement = input("Enter Improvement Needed: ")
                status = input("Enter Status (Planned/In Progress/Completed): ")
                print(self.manager.manage_safety_improvements({'stadium_id': stadium_id, 'improvement': improvement, 'status': status}))

            elif choice == "7":
                print(self.manager.get_safety_improvements())

            elif choice == "8":
                print("Exiting the Stadium Safety Inspection Tool.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

