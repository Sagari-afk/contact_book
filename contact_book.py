def add_contact(name, phone_number, email, job):
    my_dict = {"name": name, "phone_number": phone_number, "email": email, "job": job}
    contact_list.append(my_dict)
    print(my_dict)

def delete_contact():
    index =  input(f"what do you want to delete?(write number of dict)   {contact_list}")
    try:
        del contact_list[int(index)-1]
        print(f"final list - {contact_list}")
        
    except Exception as e:
        print(f"Exception: {e}")

def find_contact(how_find, what_find):
    try:
        for i in contact_list:
            for key, value in i.items():
                if key == how_find and value == what_find:
                    print(i)

                else:
                    continue

    except Exception as e:
        print(f"Exception: {e}")

def save_contact_list():
    how_save = input("would you like to save as table - 1 or txt - 2 file?")
    try:
        if how_save == "1":
            import csv
            row = contact_list
            with open("your contact book.csv", "w", encoding="utf-8", newline="") as csv_file:
                columns = ["name", "phone_number", "email", "job"]
                writer = csv.DictWriter(csv_file, fieldnames=columns, delimiter=';')
                writer.writeheader()
                writer.writerows(row)

        elif how_save == "2":
            with open("your contact book.txt", "w", encoding="utf-8") as f:
                for i in contact_list:
                    for key, value in i.items():
                        f.write(f"{key} - {value}\n")

    except Exception as e:
        print(f"Exception: {e}")

def create_database(contact_list):
    print('. . .')
    try:
        from pymongo import MongoClient

        mongo = MongoClient('localhost', port=27017)
        my_db = mongo['Contacts']
        users_coll = my_db['Contacts']

        for contact in contact_list:
            res = users_coll.insert_one(contact)

        print('Success!')

    except Exception as e:
        print(f"Exception: {e}")

if __name__ == '__main__':
    contact_list = []
    while True:
        want = input("What do you want to do?\n(add contact - 1\nfind contact - 2\ndelete contact - 3\nsave - 4\ncreate database - 5)")
        if want == "1":
            add_contact(name=input("name"), phone_number=input("phone number"), email=input("email"), job=input("job"))

        elif want == "2":
            find_contact(how_find=input("how to find?"), what_find=input("what to find"))

        elif want == "3":
            delete_contact()

        elif want == "4":
            save_contact_list()

        elif want == "5":
            create_database(contact_list)

        else:
            print("Error")

        want_and = input("Do you want to end program?(yes/no)")
        if want_and == "yes":
            break
        else:
            continue