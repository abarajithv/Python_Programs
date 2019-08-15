def Function_Get_User_input_Insert():
    InputCount=int(input("How many entries That you want to update? : "))
    for i in range(InputCount):
                   name=input("Enter the student name : ")
                   age=int(input("Enter the student age : "))
                   gender=input("Enter the Gender of the student. Format is M/F : ")
                   Function_Dbinsert([name,age,gender])
        


def Function_Dbinsert(Insert_List):
    from tinydb import TinyDB,Query
    global db
    db=TinyDB('Save_List.jon')
    Query_Element=Query()
    Row_Check_Count=db.count((Query_Element.name==Insert_List[0]) & (Query_Element.age==Insert_List[1])&(Query_Element.gender==Insert_List[2]))
    if Row_Check_Count > 0:
        print ("The entry is existing already")
    else:
        db.insert ({'name':Insert_List[0],'age':Insert_List[1],'gender':Insert_List[2]})
        print ("The Following Row has been added")
        print (db.search((Query_Element.name==Insert_List[0]) & (Query_Element.age==Insert_List[1])&(Query_Element.gender==Insert_List[2])))



def Function_DB_Lookup(name):
    import re
    from tinydb import Query
    qe=Query()
    print("\n\n\n I found these entries for ",name)
    print(db.search(qe.name.matches(name, flags=re.IGNORECASE)))
    print ("\n\n\n")
    

def Function_DB_Remove ():
    print ("Need to develop \n \n \n")

def Function_DB_Update ():
    print ("Need to develop \n \n \n")

def Function_DB_Add ():
    print ("Need to develop \n \n \n")

def Function_DB_Showall():
    print ("\n \n \n \n")
    for i in db:
        print (i)
    #print(db.all())
    print ("\n \n \n \n")
    
def Function_Initial_Screen():
    Home_Screen_Selection=int(input ("Select one of these options by entering their number \n 1. I Want to lookup someone \n 2. I want to delete some one \n 3. I want to update some one \n 4. I want to add some one \n 5. I want to list the entire list \n 6. Exit the program\n :"))
    if  Home_Screen_Selection == 1:
        LookupName=input("Enter the name that you want to lookup :")
        Function_DB_Lookup(LookupName)

    elif Home_Screen_Selection == 2:
        Function_DB_Remove()

    elif Home_Screen_Selection == 3:
        Function_DB_Update()

    elif Home_Screen_Selection == 4:
        Function_Get_User_input_Insert()
        
    elif  Home_Screen_Selection == 5:
        Function_DB_Showall()

    elif Home_Screen_Selection == 6:
        print ("Bye I am exiting")
        global DontExit
        DontExit=False
        

    else :
        print ("Enter a valid input ")
        
############# It starts from here #############################################
DontExit=True
from tinydb import TinyDB,Query
global db
db=TinyDB('Save_List.jon')
while DontExit:
    Function_Initial_Screen()

#HIHIHI#
        





