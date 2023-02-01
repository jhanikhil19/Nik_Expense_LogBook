#this is an expense calculator which I made for myself.
# logs expense with time stamp
# one function to enter all the data
# one function to retrieve all the date
# f.write("\n"+a+"\t"+b)

#For reading whole file.
# f = open("nik.txt","rt")
# for line  in f:
#     print(line)
# f.close()


def getdate():
    import datetime
    return datetime.datetime.now()
date_time=str(getdate())

def enter_data_expense():
        print("Enter the your expense for today")
        expense_today = input()
        print("What's that expense for ?")
        expense_for = input()
        with open("Feb_Expense_Nikhil.txt","a+") as f:
            f.write("\n"+date_time+"\t\t"+expense_today+"\tEuro \t"+expense_for)


def retrieve_data():
        with open("Feb_Expense_Nikhil.txt","rt") as f:
            for line in f:
                print(line)

def main1():

    print("Enter 1 for Logging EXPENSE Data in the file")
    print("Enter 2 for Looking at EXPENSES DONE TILL NOW")
    action_num = int(input())

    if (action_num==1):
        enter_data_expense()
    elif (action_num==2):
        retrieve_data()
    else:
        print("Enter proper request")

    choice=input("Want to continue Y for YES and any other key to exit")
    if(choice in ["Y","y"]):
        main1()
    else:
        print("----- THANK YOU FOR USING NIK's EXPENSE TRACKING SYSTEM ------")


main1()







