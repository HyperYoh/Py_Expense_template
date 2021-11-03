# Python Group Expense tracker

## Abstract

Ever wondered why Tricount and Splitwise never made a CLI version of their respectives applications ? Don't keep on waiting, do it yourself ! Today we'll be creating a CLI application allowing to track your expenses and their repartition within your friends or your family. 

## Pre-requisites
- Have Python (>=3.7) installed on your computer
- Install the PyInquirer library using pip (`pip install pyinquirer`)

## Useful References
- PyInquirer github repository : https://github.com/CITGuru/PyInquirer
- Python Package Manager Documentation : https://pypi.org/project/pip/
- CSV Read/Write standard lib documentation : https://docs.python.org/fr/3/library/csv.html
- Unittest standard lib documentation : https://docs.python.org/3/library/unittest.html

## Advices
Code quality and lisibility as well as documentation on how you solved problems will be greatly appreciated/rewarded
Cheating is allowed, but getting catched isn't
Creation of new files is recommended. Clean architectures will be rewarded
A `tests` folder has been created along with a test example. Look at noted documentation in order to learn more about unit testing
## Todo-list

- [X] A new expense can be added (Mandatory expense information : Amount, label, Spender)
- [X] Expense registry is stored in an external file on an appropriate format for persistency (CSV is fine, any other relevant format would be cool)
- [ ] A new user can be created (Mandatory user information : Name)
- [ ] Users are stored in an external file for persistency
- [ ] When adding a new expense, Spender should be chosen among existing users
- [ ] An expense can be divided between several existing users. By default, total amount of the expense will be evenly split between all involved users and spender should automatically be checked as involved in the expense
- [ ] New mandatory expense information : People involved in the expense
- [ ] A status report can be accessed from the main menu, synthesizing who owes who. Every user must appear only once in the report, so you must synthesize reimbursements. 
Exemple: 3 Users :
- User1 owes 34,56€ to User2
- User2 owes nothing
- User3 owes 14,72€ to User2
- [ ] Add the possibility to mark a debt as payed from the status report 
- [ ] Think of new ways of spliting the expense (Percentage / person, Amount / person, anything that makes sense)
- [ ] User Input Validation : Throw an error if an expense amount is not a number, and so on ..
- [ ] All implemented features should have relevant test cases
    - If I just have to run your test suite to check project quality and features : Automatic bonus
- [ ] Bonus : Improve your app in any way you want : More features, fancy report, any good idea will be rewarded

