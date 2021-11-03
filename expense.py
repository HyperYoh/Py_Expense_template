from PyInquirer import prompt
import csv
import copy
import re



expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
        #"validate": lambda  _, x: re.fullmatch("^\d+$", x)
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
]

choose_user={
        "type":"list",
        "name":"choose_user",
        "message":"New Expense - Spender: ",
        "choices": []
}

choose_involved_user={
        "type":"list",
        "name":"choose_involved_user",
        "message":"New Expense - Involved User: ",
        "choices": []
}

def fun_choose_user():
    dico = copy.deepcopy(choose_user)
    with open("users.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=["Name"])
        dico["choices"] += [row["Name"] for row in reader]
    return dico

def fun_choose_involved_user(involved_user):
    dico = copy.deepcopy(choose_involved_user)
    with open("users.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=["Name"])
        dico["choices"] += [row["Name"] for row in reader if row["Name"] not in involved_user] + ["None"]
    return dico

def new_expense(*args):
    infos = prompt(expense_questions)
    spender=prompt(fun_choose_user())["choose_user"]
    involved_user= [spender]
    IUser = prompt(fun_choose_involved_user(involved_user))["choose_involved_user"]
    while IUser != "None":
        involved_user += [IUser]
        IUser = prompt(fun_choose_involved_user(involved_user))["choose_involved_user"]

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with  open("expense_report.csv", newline="") as csvfile:
        reader=csv.DictReader(csvfile)
        fieldnames = reader.fieldnames
    if not fieldnames:
            with open("expense_report.csv", "w", newline="") as csvfile:
                fieldnames = ["Amount", "Label", "Spender", "Involved Users"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
    with open("expense_report.csv", "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"Amount": infos['amount'], "Label": infos['label'], "Spender": spender, "Involved Users":involved_user})
    print("Expense Added !")
    return True