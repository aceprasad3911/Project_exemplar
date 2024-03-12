import time
from datahandler import data
# user interface


def ui():
    option = int(input("""Welcome to the Nurse Attrition database.
    What would you like to do?:
         Load Data      [1]
         Process Data   [2]
         Visualise Data [3]
         Export Data    [4]
         Exit           [5]
    Enter an option:   """))
    return option


# main body for instructions
def run():
    while True:
        option = ui()
        if option == 1:
            load_data()
            print(f"Successfully loaded {len(data) - 1} profiles.")
            print("Returning to main menu...")
            time.sleep(3)
        elif option == 2:
            from Process_ui import process
            process()
            time.sleep(2)
            print("Returning to main menu...")
            time.sleep(3)
        elif option == 3:
            from Visualise_ui import visualise
            visualise()
            time.sleep(2)
            print("Returning to main menu...")
            time.sleep(3)
        elif option == 4:
            from jsonexport import export
            departid = input("Enter Department:  ")
            export(departid)
            print("Exiting programme to save your .json file")
            exit()
        elif option == 5:
            exit()
        else:
            print("Invalid option, please try again!")


# option 1
def load_data():
    with open("nurse_attrition.csv") as csv_file:
        for record in csv_file:
            data.append(record)


run()
