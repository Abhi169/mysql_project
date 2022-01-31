'''Project For Managing The Organisation Records In Multiple Databases/Tables From One Program'''

#Import mysql-connector module
import mysql.connector as m

def dbcreate():
    #Establishing connection between MySql database
    db = m.connect(host="localhost",user="root",passwd="root")
    #creating cursor instance
    c = db.cursor()

    userdb = input("\nEnter the name of database which you wants to create: ")
    # %/{} is a parameterised queries
    query = "create database if not exists %s ;"%(userdb)
    c.execute(query)  #executing SQL Query
    print("\nDatabse is created successfully!\n")
    input(">>>PRESS ENTER TO CONTINUE<<<")
    return


def tablecreatecumchecker():
    db = m.connect(host="localhost",user="root",passwd="root")  #connecting to database
    c = db.cursor() 
    c.execute("show databases;")  
    print("\nAvailable Databases are: \n")
    for data in c:   #printing database
        data = list(data)
        print(data[0])
    

    #validating the database if it exists or not before creating the table
    name = input("\nEnter the database name which you want to use: ")
    check = m.connect(host="localhost",user="root",passwd="root")
    cur = check.cursor()
    cur.execute("Show databases;")
    #fetching all records from cursor
    data = cur.fetchall()
    l=[]  #to store resultset
    for i in data:
        i = list(i)
        l.append(i[0])  #ignoring the datatypes,constraints
    
    if name in l:  #checking if dbname provided by user exists
        createtable(name) #if exist calling create table function
    else:
        print("\nDatabase don't exist!\n")
    
    input(">>>PRESS ENTER TO CONTINUE<<<")
    return

def createtable(dbname):

    db = m.connect(host="localhost",user="root",passwd="root",database="{}".format(dbname))
    c = db.cursor()
    #Taking Input Of Table Name
    tname = input("\nNOTE: Don't use any whitespace in name\nEnter the table name: ")
    c.execute("create table if not exists {}(Name varchar(20) NOT NULL,Roll_no int(6) NOT NULL UNIQUE);".format(tname))
    #Alerting The user that rollno and name column already exists
    print("\nNOTE: Roll_no and Name columns are created in newly generated table!")
    print("NOTE: Name & Roll_no are Neccesarily Required(cant't be Null)\n")
    #If user want to add more columns
    print("If you want to add more columns enter 1 or else enter 0")
    ch=int(input("Enter 0/1: "))
    if ch==1:
        columns = int(input("\nEnter how many columns you want to add: "))
        while(columns>0):
            columns-=1
            cname = input("Enter the column name: ")
            dtype = input("Enter column's datatype: ")
            size = input("Enter the size: ")
            cn = input("Enter constraint if any: ")
            c.execute("alter table {} add({} {}({}) {});".format(tname,cname,dtype,size,cn))
            print("Column Added Successfully!\n")
    if ch==0:
        print("Table created successfully!\n")
    
    input(">>>PRESS ENTER TO CONTINUE<<<")
    return


def add_record():
    conn = m.connect(host="localhost",user="root",passwd="root")
    cur = conn.cursor()
    cur.execute("show databases;")
    l=[]
    print("\nAvailable Databases are: \n")
    for i in cur:
        i = list(i)
        print(i[0])
        l.append(i[0])

    dname = input("\nEnter the name of database: ")
    #validating input if not it will result into an error
    if dname in l:
        db = m.connect(host="localhost",user="root",passwd="root",database="{}".format(dname))
        c = db.cursor()
        c.execute("show tables;")
        print("\nTables Present in Database are: ")
        s = []
        for data in c:
            data = list(data)  #typecasting bec data was of tuple type
            print(data[0])
            s.append(data[0])
            
        if len(s)==0:
            print("\nDatabase do not contain any Table!")
            print("Create A Table First\n")
        else:
            tname = input("\nEnter the table name in which you want to add records: ")
            #validating table name
            if tname in s:
                c.execute("desc {};".format(tname))
                a=1
                print("\nThe Columns Present in Table Are: ")
                for data in c:
                    data = list(data)
                    print("{} Column:".format(a),data[0])
                    a+=1
                
                ch = 'y'
                while(ch.lower()=='y'):   #if wants to add multiple records
                    
                    count = 3
                    name = input("Enter Name: ")
                    roll = input("Roll No. is Unique Can't be duplicate\nEnter Roll No: ")
                    c.execute("insert into {}(Name,Roll_no)values('{}',{});".format(tname,name,roll))
                    db.commit()
                    
                    while(count<a): 
                        
                        count+=1
                        cname = input("Always Enter Column Name: ")
                        if cname.isspace():
                            while (cname.isspace()==True):
                                print("***Column name is required!***")
                                cname = input("Always Enter Column Name: ")
                
                        value = input("Enter The Input/Data if any: ")
                        
                        if value.isnumeric:
                            c.execute("update {} set {} = '{}' where Roll_no  = {} ;".format(tname,cname,value,roll))
                            db.commit()
                        
                        elif value.isdigit:
                            c.execute("update {} set {} = {} where Roll_no = {} ;".format(tname,cname,value,roll))
                            db.commit()

                
                    print("Data Added Successfully!\n")
                    ch = input("\nWant to Enter Data y/n: ")
                    

            else:
                print("Table doesn't exist!\n")

    else:
        print("Database doesn't exist!\n")

    
    input(">>>PRESS ENTER TO CONTINUE<<<")
    return

def update():
    conn = m.connect(host="localhost",user="root",passwd="root")
    cur = conn.cursor()
    cur.execute("show databases;")
    l=[]
    print("\nAvailable Databases are: \n")
    for i in cur:
        i = list(i)
        print(i[0])
        l.append(i[0])

    dname = input("\nEnter the name of database: ")
    if dname in l:
        db = m.connect(host="localhost",user="root",passwd="root",database="{}".format(dname))
        c = db.cursor()
        c.execute("show tables;")
        s=[]
        print("\nTables Present in Database are: ")
        for data in c:
            data = list(data)
            print(data[0])
            s.append(data[0])
            
            
        tname = input("\nEnter the table name in which you want to update the records: ")
        if tname in s:
            a = 1
            l =[]
            c.execute("desc {};".format(tname))
            print("\nThe Columns present in table are:")
            for data in c:
                data = list(data)
                print("{} Column:".format(a),data[0])
                l.append(data[0])
                a+=1
                
            print("\nThe following data is in format of {}".format(l))
            print()
            c.execute("select*from {};".format(tname))
            for data in c:
                data = list(data)
                print(data)
                
            ch = 'y'
            while(ch.lower()=='y'):
                
                roll = input("Enter the Roll_no Whose Record You Want to Update: ")
                cname = input("Enter Column Name: ")
                if cname.isspace():
                    print("***Column name is required!***")
                    cname = input("Enter Column Name: ")
                value = input("Enter The Data/Value: ")
                if value.isnumeric:
                    c.execute("update {} set {} = '{}' where Roll_no = {} ;".format(tname,cname,value,roll))
                    db.commit()
                elif value.isdigit:
                    c.execute("update {} set {} = {} where Roll_no = {} ;".format(tname,cname,value,roll))
                    db.commit()
                
                ch = input("Want to Update More Columns y/n: ")
            
        else:
            print("Table do not exist!\n")

    else:
        print("Database do not exist!\n")

    input(">>>PRESS ENTER TO CONTINUE<<<")
    return

def rec_deletion():
    conn = m.connect(host="localhost",user="root",passwd="root")
    cur = conn.cursor()
    cur.execute("show databases;")
    q=[]
    print("Available Databases are: ")
    for i in cur:
        i = list(i)
        print(i[0])
        q.append(i[0])

    dname = input("\nEnter the name of database: ")
    if dname in q:
        db = m.connect(host="localhost",user="root",passwd="root",database="{}".format(dname))
        c = db.cursor()
        x=[]
        print("\nThe Tables Present in Database are:")
        c.execute("show tables;")
        for data in c:
            data = list(data)
            print(data[0])
            x.append(data[0])
            
        tname = input("\nEnter Table Name: ")
        if tname in x:
            l=[]
            c.execute("desc {};".format(tname))
            for data in c:
                data = list(data)
                l.append(data[0])
                
            c.execute("select*from {};".format(tname))
            print("\nData Inside Table is: ")
            print("\nData is in format of {} respectively\n".format(l))
            for data in c:
                data  = list(data)
                print(data)
                
            roll = input("\nEnter Roll_no whose record you want to delete: ")
            c.execute("delete from {} where roll_no = {};".format(tname,roll))
            db.commit()
            print("Record deleted successfully!\n")
        else:
            print("Table do not exist!\n")

    else:
        print("Database do not exist!\n")

    input(">>>PRESS ENTER TO CONTINUE<<<")
    return


def del_table():
    conn = m.connect(host="localhost",user="root",passwd="root")
    cur = conn.cursor()
    cur.execute("show databases;")
    s=[]
    print("Available Databases are: ")
    for i in cur:
        i = list(i)
        print(i[0])
        s.append(i[0])

    dname = input("\nEnter the name of database: ")
    if dname in s:
        db = m.connect(host="localhost",user="root",passwd="root",database="{}".format(dname))
        c = db.cursor()
        print("\nThe Tables Present in Database are:")
        c.execute("show tables;")
        l=[]
        for data in c:
            data = list(data)
            print(data[0])
            l.append(data[0])
            
        ch='y'
        while ch.lower()=='y':
            tname = input("\nEnter Table Name Which will be deleted: ")
            if tname in l:
                c.execute("drop table {};".format(tname))
                print("Table Deleted Successfully!")
                db.commit()
                
                print("\nUpdated Tables Are: \n")
                c.execute("show tables;")
                l.clear()
                for data in c:
                    data= list(data)
                    print(data[0])
                    l.append(data[0])
                    
                ch=input("\nWant to Delete other Table y/n: ")

            else:
                print("\nTable do not exist!\n")

    else:
        print("Database do not exist!\n")
    
    input(">>>PRESS ENTER TO CONTINUE<<<")
    return


def dbcheck():
    db = m.connect(host="localhost",user="root",passwd="root")
    c = db.cursor()
    c.execute("show databases;")
    print("\nAvailable Databases are: \n")
    for data in c:
        data = list(data)
        print(data[0])

    print()
    input(">>>PRESS ENTER<<<")
    return

def check_rec():
    
    db = m.connect(host="localhost",user="root",passwd="root")
    c = db.cursor()
    c.execute("show databases;")
    l=[]
    print("\nAvailable Databases Are: \n")
    for data in c:
        data = list(data)
        print(data[0])
        l.append(data[0])
    
    dname = input("\nEnter the name of database: ")
    if dname in l:
        c.execute("use {};".format(dname))
        print("\nThe Tables Present in Database are:")
        c.execute("show tables;")
        s=[]
        for data in c:
            data = list(data)
            print(data[0])
            s.append(data[0])
            
        if len(s)==0:
            print("\nDatabase do not contain any table\n")
        else:
            tname = input("\nEnter Table Name Whose Record You Want To see: ")
            if tname in s:
                l=[]
                c.execute("desc {};".format(tname))
                for data in c:
                    data = list(data)
                    l.append(data[0])
                    
                c.execute("select*from {};".format(tname))
                print("Records available in Table Are:")
                print("Records are in following Order respectively:- \n")
                print(l)
                print()
                for data in c:
                    data = list(data)
                    print(data)
                
                print()

            else:
                print("\nTable doesn't exist\n")

    else:
        print("\nDatabase do not exist!\n")

    input(">>>PRESS ENTER TO CONTINUE<<<")
    return

def db_drop():
    
    db = m.connect(host="localhost",user="root",passwd="root")
    c = db.cursor()
    c.execute("show databases;")
    print("\nAvailable Databases Are: \n")
    s=[]
    for data in c:
        data = list(data)
        print(data[0])
        s.append(data[0])
    
    ch = 'y'
    while (ch.lower())=='y':
        dname = input("\nEnter the name of database which will be deleted: ")
        if dname in s:
            c.execute("drop database {};".format(dname))
            print("Database Deleted Successfully!")
            db.commit()
            c.execute("show databases;")
            print("\nNow Available databases are: \n")
            for data in c:
                data = list(data)
                print(data[0])

            ch=input("\nWant to delete another database y/n: ")
                
        else:
            print("\nDatabase do not exist")
    
    print()
    input(">>>PRESS ENTER TO CONTINUE<<<")
    return

def column():
    print("\n1. To Add Column to existing Table\n2. To Delete Column of existing Table")
    ch=int(input("Enter your choice 1/2: "))
    while((ch!=1)and(ch!=2)):
        ch=int(input("Enter valid choice 1/2: "))

    if ch==1:
        db = m.connect(host="localhost",user="root",passwd="root")
        c = db.cursor()
        c.execute("show databases;")
        print("\nAvailable Databases Are: \n")
        s=[]
        for data in c:
           data = list(data)
           print(data[0])
           s.append(data[0])
        
        dname = input("\nEnter database name: ")
        if dname in s:
            c.execute("use {};".format(dname))
            c.execute("Show tables;")
            j=[]
            print("\nAvailable Tables are: ")
            for i in c:
                i = list(i)
                print(i[0])
                j.append(i[0])

            tname = input("\nEnter Table Name: ")
            if tname in j:
                a=1
                c.execute("desc {};".format(tname))
                print("\nThe availabe columns are: ")
                t=[]
                while a<=len(j):
                  for i in c:
                      i = list(i)
                      t.append(i[0])
                      print("{} Column: ".format(a),i[0])
                      a+=1

                cname = input("\nEnter Column Name To Add: ")
                if cname in t:
                    print("Column Already Exists!\n")

                else:
                    dtype = input("Enter datatype: ")
                    size = input("Enter Size: ")
                    cn = input("Enter Constraint if any: ")
                    c.execute("alter table {} add({} {}({}) {});".format(tname,cname,dtype,size,cn))
                    db.commit()
                    print("Column created successfully!")
                    w = input("Want to See Updated Columns? y/n: ")
                    if w.lower()=='y':
                        c.execute("desc {};".format(tname))
                        print("\nUpdated columns are: \n")
                        for data in c:
                            data = list(data)
                            print(data[0])

                    else:
                        return
            else:
                print("Table do not exist!\n")

        else:
            print("Database do not exist!\n")

    elif ch==2:
        db = m.connect(host="localhost",user="root",passwd="root")
        c = db.cursor()
        c.execute("show databases;")
        print("\nAvailable Databases Are: \n")
        s=[]
        for data in c:
           data = list(data)
           print(data[0])
           s.append(data[0])

        dname = input("\nEnter database name: ")
        if dname in s:
            c.execute("use {};".format(dname))
            c.execute("Show tables;")
            j=[]
            print("\nAvailable Tables are: ")
            for i in c:
                i = list(i)
                print(i[0])
                j.append(i[0])

            tname = input("\nEnter Table Name: ")
            if tname in j:
                a=1
                c.execute("desc {};".format(tname))
                print("The availabe columns are: ")
                t=[]
                while a<=len(j):
                  for i in c:
                      i = list(i)
                      t.append(i[0])
                      print("{} Column: ".format(a),i[0])
                      a+=1

                cname = input("\nEnter Column Name To Drop/Delete: ")
                if cname in t:
                    c.execute(" alter table {} drop column {};".format(tname,cname))
                    db.commit()
                    print("Column Deleted Successfully!")
                    w = input("Want to See Updated Columns? y/n: ")
                    if w.lower()=='y':
                        c.execute("desc {};".format(tname))
                        print("\nUpdated columns are: \n")
                        for data in c:
                            data = list(data)
                            print(data[0])

                    else:
                        return

                else:
                    print("Column do not exist!\n")
            else:
                print("Table do not exist!\n")

        else:
            print("Database do not exist!\n")       


    print()
    input(">>>ENTER SPACE<<<")
    return

f = True
while f is True:
    print('''
    \n  >>>PROJECT FOR MANAGING THE ORGANISATION RECORDS<<<
                           
                           CHOICES                   
    1. To create a new separate database for office,teachers,etc.

    2. To create a new table in any database

    3. To add details of student in database

    4. To check the Databases/Records in Table

    5. To delete student's record

    6. To update student's record

    7. To drop a database

    8. To delete a table from any database

    9. To Add/Delete a column

    10. To Exit
    
    ''')
    choice = int(input("Enter Your Choice 1/2/3/4/5/6/7/8/9/10: "))

    while((choice!=1)and(choice!=2)and(choice!=3)and(choice!=4)and(choice!=5)and(choice!=6)and(choice!=7)and(choice!=8)and(choice!=9)and(choice!=10)):
        choice = int(input("Enter a Valid Choice 1/2/3/4/5/6/7/8/9/10: "))

        
    if choice==1:
        dbcreate()

    elif choice==2:
        tablecreatecumchecker()

    elif choice==3:
        add_record()

    elif choice==4:
        print("\n1. To check list of Databases\n2. To check Data Inside Table")
        ch = int(input("Enter your choice 1/2: "))
        while(ch!=1 and ch!=2):
            ch = int(input("Enter Valid Choice 1/2: "))
        if ch==1:
            dbcheck()

        elif ch==2:
            check_rec()

    elif choice==5:
        rec_deletion()

    elif choice==6:
        update()

    elif choice==7:
        db_drop()

    elif choice==8:
        del_table()

    elif choice==9:
        column()


    elif choice==10:
        print("\nTHANK YOU FOR USING THE PROGRAM!\n")
        input("<<<PRESS ENTER>>>")
        f = False
