import tkinter
from PIL import ImageTk, Image
#import sqlite3
#import time
import random
#conn=sqlite3.connect("TaxiDB.db")

'''#conn.execute("DROP TABLE IF EXISTS Reservation")
conn.execute("DROP TABLE IF EXISTS USER")
conn.execute("DROP TABLE IF EXISTS RESERVATION")

#conn.execute("DROP TABLE IF EXISTS Car")

conn.execute("Create table USER (name varchar(20), mob varchar(15) PRIMARY KEY,  pass varchar(15));")
conn.execute("INSERT INTO USER (mob, pass) VALUES(?,?)", ("9818028023", "password"))
conn.execute("Create table RESERVATION (rid int, name varchar(20), mob varchar(15) PRIMARY KEY, point varchar(20), pt varchar(30),  dt varchar(30));")
#conn.execute("Create table ArtWork (Title varchar(20) PRIMARY KEY, AName varchar(15), Year int, Type varchar(15), Price real);")
#conn.execute("Create table Customer (CName varchar(15) PRIMARY KEY, Address varchar(40) DEFAULT None, Pno int DEFAULT None, Amount real DEFAULT 0 );")
#conn.execute("Create table Purchase (Cname varchar(15), Title varchar(20), Price real, Date varchar(10));")
'''

Customers=[]
customers_dict={"Name":"Sejal", "Mobile":"9650061224", "Pw":"sejal"}
Customers.append(customers_dict)
customers_dict={"Name":"Aanchal", "Mobile":"9818028023", "Pw":"aanchal"}
Customers.append(customers_dict)
customers_dict={"Name":"Abhishek", "Mobile":"9818826362", "Pw":"abhi"}
Customers.append(customers_dict)

Reservations=[]
reservations_dict={"RID":'4536',"Name":"Karan", "Point":"Dwarka", "ts":"09:00-12:00", "Car":"WagonR","Rent":'2500', "Security":'25000'}
Reservations.append(reservations_dict)
#reservations_dict={"RID":'6736',"Name":"Priya", "Mobile":"8857488339", "pt":datetime.date(2017, 11, 20), "dt":datetime.date(2017, 12, 05)}
#Reservations.append(reservations_dict)
#reservations_dict={"RID":'7744',"Name":"Sneha", "Mobile":"9212647583", "pt":datetime.date(2017, 11, 20), "dt":datetime.date(2017, 12, 04)}
#Reservations.append(reservations_dict)

choice=[""]

mini=[]
WagonR=['WagonR',2500, 25000,1,4,7]
Ritz=['Ritz',2500, 25000,1,5,8]
i10=['i10',2500, 25000,2,5]
i20=['i20',2500, 25000,3,6]
Swift=['Swift',2500, 25000,3]
mini.append(WagonR)
mini.append(Ritz)
mini.append(i10)
mini.append(i20)
mini.append(Swift)

sedan=[]
Verna=['Verna',3500, 35000,1,4,7]
Dzire=['Dzire',3500, 35000,1,5,8]
Ciaz=['Ciaz',3500, 35000,2,5]
Amaze=['Amaze',3500, 35000,3,6]
Accent=['Accent',3500, 35000,3]
sedan.append(Verna)
sedan.append(Dzire)
sedan.append(Ciaz)
sedan.append(Amaze)
sedan.append(Accent)

suv=[]
Creta=['Creta',4500, 45000, 1,4,7]
Innova=['Innova',4500, 45000,1,5,8]
Scorpio=['Scorpio',4500, 45000,2,5]
Nexon=['Nexon',4500, 45000,3,6]
Brezza=['Brezza',4500, 45000,3]
suv.append(Creta)
suv.append(Innova)
suv.append(Scorpio)
suv.append(Nexon)
suv.append(Brezza)

TIMESLOTS=[]
a=9
b=12
for i in range(0,10):
    TIMESLOTS.append(str(a)+":00-"+str(b)+":00")
    a=a+1
    b=b+1 
     

global root,f1
root = tkinter.Tk()
root.attributes('-fullscreen', True)

#User= {'Names':["Sejal", "Aanchal", "Abhishek"],'Mobile':['9650061224', '9818028023', '9818826362'],'Address':['Dwarka', 'Dwarka', 'Gurgaon']}
#userdata= pd.Dataframe

'''def final():
    row=list(conn.execute("Select rid from RESERVATION where rid=?", (myrid,)))
    for r in row:
        print(r)
        
    row=list(conn.execute("Select pt,dt from RESERVATION"))
    for x in row:
        x[0]=datetime.date(2006, 12, 25)
  '''      
  
def final():
    
    img= Image.open("sejal1.jpg")
    img = img.resize((1362,763))
    img1 = ImageTk.PhotoImage(img)
    myimage1 = tkinter.Label(root, image = img1)
    myimage1.place(x=0, y=0)
    
    frame = tkinter.Frame(root, bg='#F7DC6F')
    frame.place(x=120, y=230, height=380, width=360)
    
    myrid=str(random.randint(1, 10000))
    
    reservations_dict={"RID":myrid,"Name":cname, "Point":point_entry.get(), "ts":var.get(), "Car":car, "Rent":rent, "Security":security}
    Reservations.append(reservations_dict)
    
    head = tkinter.Label(root, text="And you're done!",fg='maroon', font=("Arial", 30, "bold italic"), bg='#F7DC6F')
    head.place(x=450, y=100)
            
    back = tkinter.Button(root, text="Back", command=booking, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    back.place(x=60, y=20)
    
    about = tkinter.Button(root, text="About Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    about.place(x=900, y=20)
        
    contact = tkinter.Button(root, text="Contact Us", command = main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    contact.place(x=1050, y=20)
    
    signout = tkinter.Button(root, text="Sign Out", command = main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    signout.place(x=1220, y=20)
    
    lname = tkinter.Message(root, text="Congrats "+cname+"! Your car has been booked for tomorrow!\n\nPlease note the details:",fg='navy', font=("Arial", 16, "bold italic"), bg='#F7DC6F', width=290)
    lname.place(x=140, y=260)  
    
    one = tkinter.Label(root, text="REGN ID:", fg='dark green', font=("Arial", 13, "bold italic"), bg='#F7DC6F')
    one.place(x=140, y=410)
    
    two = tkinter.Label(root, text="STARTING POINT:", fg='dark green', font=("Arial", 13, "bold italic"), bg='#F7DC6F')
    two.place(x=140, y=440)
    
    three = tkinter.Label(root, text="TIME SLOT:", fg='dark green', font=("Arial", 13, "bold italic"), bg='#F7DC6F')
    three.place(x=140, y=470)
    
    four = tkinter.Label(root, text="CAR:", fg='dark green', font=("Arial", 13, "bold italic"), bg='#F7DC6F')
    four.place(x=140, y=500)
    
    five = tkinter.Label(root, text="RENT:", fg='dark green', font=("Arial", 13, "bold italic"), bg='#F7DC6F')
    five.place(x=140, y=530)
    
    six = tkinter.Label(root, text="SECURITY:", fg='dark green', font=("Arial", 13, "bold italic"), bg='#F7DC6F')
    six.place(x=140, y=560)
    #data = tkinter.Message(root, text="REGN ID:        "+myrid+"\nCAR:           "+car+"\nSTARTING POINT: "+point_entry.get()+"\nTIME SLOT:    "+var.get(),fg='maroon', font=("Arial", 12, "bold italic"), bg='#F7DC6F', width=200)
    #data.place(x=140, y=320)
    i=410
    for r in reservations_dict.keys():
        a = reservations_dict[r]
        
        if r!='Name':
            data = tkinter.Label(root, text=a, fg='maroon', font=("Arial", 13, "bold italic"), bg='#F7DC6F')
            data.place(x=300, y=i)
            i += 30
    
    root.mainloop()
    
    
def activity_selection():
    
    global cname, mylist,car, rent, security
    car=""
    for row in Customers:
        if row["Pw"]==confirm.get():
            #print("YAYYYY")
            cname=row["Name"]
            num=TIMESLOTS.index(var.get()) 
            num=num+1
            
            if choice[0]=='mini':
                mylist=mini
            if choice[0]=='sedan':
                mylist=sedan
            if choice[0]=='suv':
                mylist=suv
                print (mylist)
            
            if num not in mylist[0] and num>mylist[0][-1] and (mylist[0][-1]!=num+1 or mylist[0][-1]!=num+2) :
                mylist[0].append(num)
                print(mylist[0])
                car=(mylist[0][0])
                rent=(mylist[0][1])
                security=(mylist[0][2])
                print(car)
                final()
                        
            elif num not in mylist[1] and num>mylist[1][-1] and (mylist[1][-1]!=num+1 or mylist[1][-1]!=num+2):
                mylist[1].append(num)
                print(mylist[1])
                car=(mylist[1][0])
                rent=(mylist[1][1])
                security=(mylist[1][2])
                final()
                      
            elif num not in mylist[2] and num>mylist[2][-1] and (mylist[2][-1]!=num+1 or mylist[0][-1]!=num+2) :
                mylist[2].append(num)
                print(mylist[2])
                car=(mylist[2][0])
                rent=(mylist[1][1])
                security=(mylist[1][2])
                final()
                
            elif num not in mylist[3] and num>mylist[3][-1] and (mylist[3][-1]!=num+1 or mylist[0][-1]!=num+2) :
                mylist[3].append(num)
                print(mylist[3])
                car=(mylist[3][0])
                rent=(mylist[3][1])
                security=(mylist[3][2])
                final()
                
            elif num not in mylist[4] and num>mylist[4][-1] and (mylist[4][-1]!=num+1 or mylist[0][-1]!=num+2) :
                mylist[4].append(num)
                print(mylist[4])
                car=(mylist[4][0])
                rent=(mylist[3][1])
                security=(mylist[3][2])
                final()
            else:
                lname = tkinter.Message(root, text="Sorry "+row["Name"]+"!\n\nNo cars available!\nTry a different slot.",fg='maroon', font=("Arial", 15, "bold italic"), bg='#F7DC6F', width=200)
                lname.place(x=530, y=320) 
                 
        
            
            
    
    print("done")
    #print(Reservations)
    root.mainloop()
    
def update_reservation():
    global confirm
    
    img= Image.open("sejal1.jpg")
    img = img.resize((1362,763))
    img1 = ImageTk.PhotoImage(img)
    myimage1 = tkinter.Label(root, image = img1)
    myimage1.place(x=0, y=0)
    
    
    head = tkinter.Label(root, text="Confirm your password, please!",fg='maroon', font=("Arial", 20, "bold italic"), bg='#F7DC6F')
    head.place(x=430, y=100)
    
    confirm = tkinter.Entry(root,show="*", font=("Arial", 15, "bold italic"), width=17)
    confirm.place(x=530, y=150)
    
    go = tkinter.Button(root, text="Go >", command=activity_selection, fg='white', font=("Arial", 13, "bold italic"), bg='maroon', bd=0, width=4)
    go.place(x=730, y=150)
    
    back = tkinter.Button(root, text="Back", command=booking, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    back.place(x=60, y=20)
    
    about = tkinter.Button(root, text="About Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    about.place(x=900, y=20)
        
    contact = tkinter.Button(root, text="Contact Us", command = main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    contact.place(x=1050, y=20)
    
    signout = tkinter.Button(root, text="Sign Out", command = main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    signout.place(x=1220, y=20)

    root.mainloop()
    
def booking():
    global point_entry, var
    
    imgs= Image.open("sejal2.jpg")
    imgs = imgs.resize((1362,763))
    imgs1 = ImageTk.PhotoImage(imgs)
    myimages1 = tkinter.Label(root, image = imgs1)
    myimages1.place(x=0, y=0)
    
    head = tkinter.Label(root, text="OWN IT FOR 3 HOURS!",fg='maroon', font=("Arial", 30, "bold italic"), bg='#F7DC6F')
    head.place(x=390, y=100)
    
    frame = tkinter.Frame(root, bg='#F7DC6F')
    frame.place(x=120, y=230, height=360, width=250)
    
    back = tkinter.Button(root, text="Back", command=citypage, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    back.place(x=60, y=20)
    
    about = tkinter.Button(root, text="About Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    about.place(x=900, y=20)
        
    contact = tkinter.Button(root, text="Contact Us", command = main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    contact.place(x=1050, y=20)
    
    signout = tkinter.Button(root, text="Sign Out", command = main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    signout.place(x=1220, y=20)
    
    point = tkinter.Label(root, text="Starting point:",fg='maroon', font=("Arial", 15, "bold italic"), bg='#F7DC6F')
    point.place(x=140, y=280)

    point_entry = tkinter.Entry(root, font=("Arial", 12, "bold italic"), width=19)
    point_entry.place(x=140, y=310)
    point_entry.insert(0,"Enter nearby location")

    pt = tkinter.Label(root, text="Time Slots:",fg='maroon', font=("Arial", 15, "bold italic"), bg='#F7DC6F')
    pt.place(x=140, y=360)
    
    #pt_entry = tkinter.Entry(root, font=("Arial", 12, "bold italic"), width=19)
    #pt_entry.insert(0,time.strftime("%c"))
    #pt_entry.insert(0,time.strftime("%x")+" "+time.strftime("%I")+":"+time.strftime("%M")+" "+time.strftime("%p"))
    #pt_entry.insert(0,"dd/mm/yyyy")
    #pt_entry.place(x=140, y=390)
    
    var = tkinter.StringVar(root)
    var.set(TIMESLOTS[0])
    
    pt_dd = tkinter.OptionMenu(root, var, *TIMESLOTS)
    pt_dd.config(font=("Arial", 12, "bold italic"), width=15, bg="white")
    pt_dd.place(x=140,y=390)
    
    '''dt = tkinter.Label(root, text="Drop off time:",fg='maroon', font=("Arial", 15, "bold italic"), bg='#F7DC6F')
    dt.place(x=140, y=440)
    
    dt_entry = tkinter.Entry(root, font=("Arial", 12, "bold italic"), width=19)
    #dt_entry.insert(0,time.strftime("%x")+" "+time.strftime("%I")+":"+time.strftime("%M")+" "+time.strftime("%p"))
    dt_entry.insert(0,"dd/mm/yyyy")
    dt_entry.place(x=140, y=470)
    #dt_entry.insert(time.strftime("%c"))
    '''
    sub = tkinter.Button(root, text="Start \nyour journey >", command=update_reservation, fg='white', font=("Arial", 15, "bold italic"), bg='maroon', bd=0, width=12, height=2)
    sub.place(x=160, y=470)
    
    root.mainloop()
    
    
def minicar():
    choice[0]='mini'
    booking()
def sedancar():
    choice[0]='sedan'
    booking()
def suvcar():
    choice[0]='suv'
    booking()

def citypage():
    
    #f1 = tkinter.Frame(root, bg="#FFA07A")
    #f1.place(height=2000, width=2000)
    
    img= Image.open("road.jpg")
    img = img.resize((1362,763))
    img1 = ImageTk.PhotoImage(img)
    myimage1 = tkinter.Label(root, image = img1)
    myimage1.place(x=0, y=0)
    
    back = tkinter.Button(root, text="Back", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    back.place(x=60, y=20)
    
    about = tkinter.Button(root, text="About Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    about.place(x=900, y=20)
        
    contact = tkinter.Button(root, text="Contact Us", command = main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    contact.place(x=1050, y=20)
    
    signout = tkinter.Button(root, text="Sign Out", command = main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    signout.place(x=1220, y=20)
    
    delhi = tkinter.Button(root, command=minicar)
    button1 = Image.open("mini.jpg")
    button1 = button1.resize((320, 400), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(button1)
    delhi.config(image=image1, bd=0)
    delhi.image = image1
    delhi.grid(row=1, column=1, padx=100, pady=120)
    
    mumbai = tkinter.Button(root, command=sedancar)
    button2 = Image.open("sedan.jpg")
    button2 = button2.resize((320, 400), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(button2)
    mumbai.config(image=image2)
    mumbai.image = image2
    mumbai.grid(row=1, column=2, pady=120)
     
    bangalore = tkinter.Button(root, command=suvcar)
    button3 = Image.open("suv.jpg")
    button3 = button3.resize((320, 400), Image.ANTIALIAS)
    image3 = ImageTk.PhotoImage(button3)
    bangalore.config(image=image3)
    bangalore.image = image3
    bangalore.grid(row=1, column=3, padx=100, pady=120)
    
    head = tkinter.Label(root, text="Make your choice and ride your way",fg='white', font=("Arial", 35, "bold italic"), bg='#ce2d5c', width=50)
    head.place(x=0, y=590)
        
    root.mainloop()
    
def signup():
    global name, mob
    name=name_textbox.get()
    mob=mobile_textbox.get()
    pw=pass_textbox.get()
    if name=='' or mob=='' or pw=='':
        error = tkinter.Label(root, text="Empty fields",fg='red', font=("Arial", 11, "bold italic"), bg='#F7DC6F')
        error.place(x=820 , y=475)
        #citypage()
    else:
        customers_dict={"Name":name, "Mobile":mob, "Pw":pw}
        Customers.append(customers_dict)
        print (Customers)
        #reservations_dict={"RID":'',"Name":name, "Mobile":mob, "Point":"", "ts":'', "Car":''}
        #Reservations.append(reservations_dict)
        citypage()
    
def login():
    #global mob
    #mob = mob_textbox.get()
    #pw = pw_textbox.get()
    
    #for row in conn.execute("Select mob, pass from USER"):
    for row in Customers:
        if ( row["Mobile"]== mob_textbox.get() and row["Pw"]== pw_textbox.get()):
            citypage()
        else:
            error = tkinter.Label(root, text="Wrong ID / Password",fg='red', font=("Arial", 11, "bold italic"), bg='#F7DC6F')
            error.place(x=1095 , y=470)

    
def fun():
    
    #root.withdraw()
    #root1 = tkinter.Tk()
    #root1.attributes('-fullscreen', True)
    
    f1 = tkinter.Frame(root, bg="#F7DC6F")
    f1.place(height=2000, width=2000)
        
    bi = tkinter.Button(f1, command=main_fun)
    cat = Image.open("taxibg.jpg")
    cat = cat.resize((100,100), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(cat)
    bi.config(image=image)
    bi.image = image
    bi.place(x=1200, y=600)
    
    root.mainloop()

    
def main_fun():
    
    global mob_textbox, pw_textbox, name_textbox, mobile_textbox, pass_textbox
    img= Image.open("sejal3.jpg")
    img = img.resize((1362,763))
    img1 = ImageTk.PhotoImage(img)
    myimage1 = tkinter.Label(root, image = img1)
    myimage1.place(x=0, y=0)
    
    about = tkinter.Button(root, text="About Us", command=main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    about.place(x=900, y=20)
        
    contact = tkinter.Button(root, text="Contact Us", command = main_fun, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    contact.place(x=1050, y=20)
    
    signout = tkinter.Button(root, text="Sign Out", command = root.destroy, fg='maroon', font=("Arial", 17, "bold italic"), bg='#F7DC6F', bd=0)
    signout.place(x=1220, y=20)
 
    
    #SIGN UP
    sframe = tkinter.Frame(root, bg="#F7DC6F")
    sframe.place(x=750, y=250, height=370, width=250)
    
    name_label = tkinter.Label(root, text="Name:",fg='maroon', font=("Arial", 15, "bold italic"), bg='#F7DC6F')
    name_label.place(x=780, y=270)

    name_textbox = tkinter.Entry(root, font=("Arial", 15, "bold italic"), width=17)
    name_textbox.place(x=780, y=300)
    
    mobile_label = tkinter.Label(root, text="Mobile:",fg='maroon', font=("Arial", 15, "bold italic"), bg='#F7DC6F')
    mobile_label.place(x=780, y=340)

    mobile_textbox = tkinter.Entry(root, font=("Arial", 15, "bold italic"), width=17)
    mobile_textbox.place(x=780, y=370)

    pass_label = tkinter.Label(root, text="Create Password:",fg='maroon', font=("Arial", 15, "bold italic"), bg='#F7DC6F')
    pass_label.place(x=780, y=410)

    pass_textbox = tkinter.Entry(root, show="*", font=("Arial", 15, "bold italic"), width=17)
    pass_textbox.place(x=780, y=440)

    b1 = tkinter.Button(root, command=signup)
    button1 = Image.open("signup.jpg")
    button1 = button1.resize((80,80), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(button1)
    b1.config(image=image1)
    b1.image = image1
    b1.place(x=830, y=510)
    
    #LOGIN
    lframe = tkinter.Frame(root, bg='#F7DC6F')
    lframe.place(x=1050, y=250, height=370, width=250)
    
    mob_label = tkinter.Label(root, text="Mobile:",fg='maroon', font=("Arial", 15, "bold italic"), bg='#F7DC6F')
    mob_label.place(x=1080, y=300)

    mob_textbox = tkinter.Entry(root, font=("Arial", 15, "bold italic"), width=17)
    mob_textbox.place(x=1080, y=340)

    pw_label = tkinter.Label(root, text="Password:",fg='maroon', font=("Arial", 15, "bold italic"), bg='#F7DC6F')
    pw_label.place(x=1080, y=380)

    pw_textbox = tkinter.Entry(root, show="*", font=("Arial", 15, "bold italic"), width=17)
    pw_textbox.place(x=1080, y=420)

    b2 = tkinter.Button(root, command=login)
    button2 = Image.open("login.jpg")
    button2 = button2.resize((80,80), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(button2)
    b2.config(image=image2)
    b2.image = image2
    b2.place(x=1130, y=510)
        
    root.mainloop()
    
main_fun()

