from PyInquirer import prompt
import csv
import copy


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
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

def fun_choose_user():
    dico = copy.deepcopy(choose_user)
    with open("users.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=["Name"])
        dico["choices"] += [row["Name"] for row in reader]
    return dico


def new_expense(*args):
    infos = prompt(expense_questions)
    user=prompt(fun_choose_user())["choose_user"]
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with  open("expense_report.csv", newline="") as csvfile:
        reader=csv.DictReader(csvfile)
        fieldnames = reader.fieldnames
    if not fieldnames:
            with open("expense_report.csv", "w", newline="") as csvfile:
                fieldnames = ["Amount", "Label", "Spender"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
    with open("expense_report.csv", "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"Amount": infos['amount'], "Label": infos['label'], "Spender": user})
    print("Expense Added !")
    return True