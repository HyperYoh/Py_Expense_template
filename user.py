from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    }
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    fieldnames=["Name"]
    with open("users.csv", newline="") as csvfile:
        reader=csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            if row["Name"] == infos["name"]:
                print(f"Error: User \"{infos['name']}\" already in database " )
                return False
    with open("users.csv", "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"Name": infos["name"]})
        print("User Added !")
    return True