from PyInquirer import prompt
import csv

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
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)
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
        writer.writerow({"Amount": infos['amount'], "Label": infos['label'], "Spender": infos['spender']})
    print("Expense Added !")
    return True