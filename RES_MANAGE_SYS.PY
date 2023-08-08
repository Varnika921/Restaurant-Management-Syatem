from tkinter import*        #import tkinter
import random                    #imports random module to generates a random number
import time               #handle various opearations regarding time,its conversion,representation

root = Tk()  #initialise tkinter
root.geometry("1400x700+0+0")           #decides the size,position of the screen layout we are going to create
root.title("Restaurant Management System")

Tops = Frame(root,bg="grey",width = 1400,height=50,relief=GROOVE)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=GROOVE)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=GROOVE)
f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))                  #gives the local time of the computer
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="GetTogether Cafe",fg="black",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)                                                              #grid organises the data in table_like structure
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="black",anchor=W)
lblinfo.grid(row=1,column=0)

text_Input=StringVar()
operator =""





def Ref():
    x=random.randint(100, 100000)      #generates a random value between 100 to 100000       
    randomRef = str(x)
    rand.set(randomRef)         

#to get  the values of no. of each dishes
    cof =float(Fries.get())
    colpasta= float(Pasta.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

#to calculate the cost of each items
    costoffries = cof*25
    costofpasta = colpasta*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35

#to calculate various costs
    costofmeal = "Rs.",str('%.2f'% (costoffries +  costofpasta + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costofpasta + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.10)
    Totalcost=(costoffries +  costofpasta + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costofpasta + costofburger + costoffilet + costofcheeseburger + costofdrinks)/100)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str('%.2f'%( PayTax + Totalcost + Ser_Charge))
    PaidTax="Rs.",str('%.2f'% PayTax)
    subtot="Rs.",str('%.2f'%(PayTax + Ser_Charge))
    
    
#to set the various costs
    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(subtot)
    Total.set(OverAllCost)


def qexit():            #function to exit the window
    root.destroy()

def reset():             #function to reset the values
    rand.set("")
    Fries.set("")
    Pasta.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")


status = Label(f2,font=('aria', 15, 'bold'),width = 19, text="-By Varnika Chhavi",bd=2,relief=SUNKEN)
status.grid(row=15,column=0,columnspan=3)

#---------------------------------------------------------------------------------------
#initialising variables
rand = StringVar()
Fries = StringVar()
Pasta = StringVar()
Burger = StringVar()
Filet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()

#creating labels and entry boxes in frame 1 
lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="red",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtreference.grid(row=0,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="French Fries",fg="red",bd=10,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtfries.grid(row=1,column=1)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Italian Pasta",fg="red",bd=10,anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Pasta , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtLargefries.grid(row=2,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal",fg="red",bd=10,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtburger.grid(row=3,column=1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="red",bd=10,anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtFilet.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="red",bd=10,anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtCheese_burger.grid(row=5,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="red",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtDrinks.grid(row=0,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Net Cost",fg="red",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="red",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax@10%",fg="red",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="red",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="red",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="grey" ,justify='right')
txtTotal.grid(row=5,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="black",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="black",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="black",command=qexit)
btnexit.grid(row=7, column=3)

#function to create the menu list
def price():
    roo = Tk()
    roo.geometry("400x400+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="steel blue", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="French Fries", fg="black", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Italian Pasta", fg="black", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="black", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="black", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="black", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="black", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()           #mainloop is a method to run the application

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="black",command=price)
btnprice.grid(row=7, column=0)

root.mainloop()
