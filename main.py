contact_list = []

def add_contact(name, phone_number, email, job):
    my_dict = {"name": name, "phone_number": phone_number, "email": email, "job": job}
    contact_list.append(my_dict)
    print(my_dict)

def delete_contact(my_list):
    for i in my_list:
        print(f"\n---> {i}")
    index = input(f"what do you want to delete?(write the number of the dict)")
    try:
        del contact_list[int(index)-1]
        print(f"final list - {my_list}")
        
    except Exception as e:
        print(f"Exception: {e}")

def find_contact(my_list):
    a = input("how find?")
    b = input("what find?")
    try:
        for i in my_list:
            for key, value in i.items():
                if key == a and value == b:
                    print(i)

                else:
                    continue

    except Exception as e:
        print(f"Exception: {e}")

def save_contact_list(my_list):
    print(". . .")
    try:
        import csv
        row = my_list
        with open("your contact book.csv", "w", encoding="utf-8", newline="") as csv_file:
            columns = ["name", "phone_number", "email", "job"]
            writer = csv.DictWriter(csv_file, fieldnames=columns, delimiter=';')
            writer.writeheader()
            writer.writerows(row)
        print("Success!")

    except Exception as e:
        print(f"Exception: {e}")

def create_database(my_list):
    print(". . .")
    try:
        from pymongo import MongoClient

        mongo = MongoClient('localhost', port=27017)
        my_db = mongo['Contacts']
        users_coll = my_db['Contacts']

        for contact in my_list:
            res = users_coll.insert_one(contact)

        print("Success!")

    except Exception as e:
        print(f"Exception: {e}")

if __name__ == '__main__':
    import sys
    from PyQt5 import QtCore, QtGui, QtWidgets
    from design import Ui_MainWindow

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    print("ok")
    MainWindow.show()
    sys.exit(app.exec_())
