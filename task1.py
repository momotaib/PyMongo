from pymongo import MongoClient
import pprint

client = MongoClient(host = "localhost", port = 27017)
Tes_Go = client["Store"]
items_collection = Tes_Go["Items"]
staff_collection = Tes_Go["Employees"]

# items class
class Items(object):

    # add item function
    def AddItem():
        name = input("Please Enter Item Name: ")
        cost = input("Please Enter Cost Of Item: ")
        quantity = input("Please Enter Quantity: ")
        myquery = {"Item": name, "Price": cost, "Quantity": quantity}
        new_id = items_collection.insert_one(myquery)

        print("Inserted Item with id %s" % new_id.inserted_id)


    # find one item function
    def FindOneItem():

        name = input("Please Enter Item Name: ")
        myquery = {"Item": name}
        itm = items_collection.find_one(myquery)
        if itm is not None:
            print(itm)
        else: 
            print ("Sorry, Item Not Found")
    
    # find all item function
    def FindAllItems():

        item_data = items_collection.find()
        for itm in item_data:
            print(itm)

            
    # remove item function
    def RemoveItem():

        name = input("Please Enter Name of The Item Being Deleted: ")
        results = items_collection.delete_many({"Quantity": name})
        print("\nDeleted %d Items" %(results.deleted_count))

    # update item function
    def UpdateItem():

        First = input("Would you like to update an stock or cost?: ")
        Second = input("What item do you want to update?: ")
        itemname = {"Item": Second}

        if First == "Stock" or First == "stock":
            addstock = input("How much stock is left for this item: ")
            newvalue = {"$set": {"Quantity" : addstock}}
            result1 = items_collection.update_one(itemname, newvalue)
            print("%d Items matched, %d Item prices updated"%(result1.matched_count, result1.modified_count))

        else:
            if First == "Cost" or First == "cost":
                cost = input("What would you like the cost to be? ")
                costvalue = {"$set": {"Price": cost}}
                result = items_collection.update_one(itemname, costvalue)
                print("%d Items matched, %d Item prices updated"%(result.matched_count, result.modified_count))


    # first command line for understanding employee needs
    while True:
        Position = input("Hi, could you please enter in your position: ")
        if Position == 'Till Operator' or Position == 'till operator':
            Read = input("Hi, Till Operator, would you like to search All items or search for One?: ")
            if Read == 'All' or Read == 'all':
                FindAllItems()
                break
            else:
                if Read == 'One' or Read == 'one':
                    FindOneItem()
                    break
        else:
            if Position == 'Stock Controller' or Position == 'stock controller':
                print("Hi, Stock Controller! ")
                UpdateItem()
                break
            elif Position == 'Financial Consultant' or Position == 'financial consultant':
                print("Hi, Financial Consultant! ")
                UpdateItem()
                break
            elif Position == 'Store Manager' or Position == 'store manager':
                Read = input("Hi, Store Manager, would you like to Add or Remove items from stock list? ")
                if Read == 'Add' or Read == 'add':
                    AddItem()
                    break
                else:
                    if Read == 'Remove' or Read == 'add':
                        RemoveItem()
                break
            else:
                print("Im sorry, seems like you have not entered your position..")

# staff class
class staff(object):

    def addStaff():

        lastname = input("Please Enter Last Name: ")
        firstname = input("Please Enter First Name: ")
        staffroles = input("Please Enter Current Role: ")
        staffsalary = int(input("Please Enter Salary: "))
        myquery = {"LastName": lastname, "FirstName": firstname, "Role": staffroles, "Salary": staffsalary}
        new_id = staff_collection.insert_one(myquery)
        print("Inserted Staff with id %s" % new_id.inserted_id)

    def findstaff():

        staff_data = staff_collection.find()
        for stff in staff_data:
            print(stff)

    def RemoveStaff():

        lastname = input("Please Enter Last Name of The Employee Being Deleted: ")
        firstname = input("Please Enter First Name of The Employee Being Deleted: ")
        results = staff_collection.delete_many({"LastName": lastname, "FirstName": firstname})
        print("\nDeleted %d Staff" %(results.deleted_count))

    def UpdateStaff():

        First = input("Would You Like To Update A Role Or Salary?: ")
        Second = input("What Is The Last Name Of The Employee?: ")
        Third = input("What Is The First Name Of The Employee?: ")
        staffname = {"LastName": Second, "FirstName": Third}

        if First == "Role" or First == "role":
            addrole = input("What Is The New Role?: ")
            newvalue = {"$set": {"Role" : addrole}}
            result1 = staff_collection.update_one(staffname, newvalue)
            print("%d Role matched, %d Role updated"%(result1.matched_count, result1.modified_count))

        else:
            if First == "Salary" or First == "salary":
                cost = int(input("What Is The New Salary?: "))
                salaryvalue = {"$set": {"Salary": cost}}
                result = staff_collection.update_one(staffname, salaryvalue)
                print("%d Salary matched, %d Staff Salary updated"%(result.matched_count, result.modified_count))
    
    def Update_Staff():
        
        StaffInput = input("Would You Like to Update Your Last Name? Yes or No:  ")
        Second = input("What Is Your Last Name?: ")
        Third = input("What Is Your First Name?: ")
        staffname = {"LastName": Second, "FirstName": Third}

        if StaffInput == "Yes" or StaffInput == "yes":
            lastname1 = input("What Is Your New LastName?: ")
            newvalue = {"$set": {"LastName" : lastname1}}
            result1 = staff_collection.update_one(staffname, newvalue)
            print("%d Last Name matched, %d Last Name updated"%(result1.matched_count, result1.modified_count))

        else:
            if First == "No" or First == "no":
                firstname1 = int(input("What Is Is Your New FirstName?: "))
                salaryvalue = {"$set": {"FirstName": firstname1}}
                result = staff_collection.update_one(staffname, salaryvalue)
                print("%d First Name matched, %d First Name updated"%(result.matched_count, result.modified_count))

    while True:
        Position = int(input("Hi, Could You Please Enter In Your Login code: "))
        if Position == 45678: 
            print("Hello Store Manager!")
            Read = input("Would You Like To Add, Remove, View or Update Staff From System? ")
            if Read == 'Add' or Read == 'add':
                addStaff()
                break
            elif Read == 'Remove' or Read == 'remove':
                RemoveStaff()
                break
            elif Read == 'View' or Read == 'view':
                findstaff()
                break
            else:
                if Read == 'Update' or Read == 'update':
                    UpdateStaff()
                    break
        elif Position == 123:
            print("Hello Customer Assistant!")
            Update_Staff()
            break
        else:
            print("Im Sorry, Seems Like You Have Entered An Incorrect Code...")
    

