#__________________Agrasth_Naman_____________________________________________________
from tkinter import*
import random
import time;

root=Tk()
root.geometry("1600x800+0+0")
root['bg']="dark slate gray"
root.title("Restaurant Management")

text_input=StringVar()
operator=" "

Tops=Frame(root, width=1600, height=50, bg='lavender')
Tops.pack(side=TOP)

f1=Frame(root, width=800, height=700, bg='lavender')
f1.pack(side=LEFT)

f2=Frame(root, width=300, height=700, bg='lavender')
f2.pack(side=RIGHT)
#=================================TIME====================================================
localtime=time.asctime(time.localtime(time.time()))
#=================================INFO====================================================
lblInfo=Label(Tops, font=('stalemate', 50, 'bold'), text="Cafe", fg="black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
lblInfo=Label(Tops, font=('google sans medium', 10, 'bold'), text=localtime, fg="black", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)
#===============================CALCULATOR================================================
def btnclick(numbers):
      global operator
      operator =operator + str(numbers)
      text_input.set (operator)

def btnClearDisplay():
      global operator
      operator=" "
      text_input.set("")

def btnEqualsInput():
      global operator
      sumup=str(eval(operator))
      text_input.set(sumup)
      operator=" "

def ref():
      #x=random.randit(1, 999999)
      #randomref=str(x)
      #rand.set(randomref)

      cosandwich=float(Sandwich.get())
      cofries=float(Fries.get())
      cocoffee=float(Coffee.get())
      cocola=float(Cola.get())
      coburger=float(Burger.get())

      CostOffries=cofries*49
      CostOfsanwich=cosandwich*99
      CostOfcola=cocola*39
      CostOfburger=coburger*79
      CostOfcoffee=cocoffee*69

      COST=CostOffries+CostOfsanwich+CostOfcola+CostOfburger+CostOfcoffee
      costD=("₹", str(CostOffries+CostOfsanwich+CostOfcola+CostOfburger+CostOfcoffee))
      CGSTD=("(0.25%)", (0.25*(float(COST)))+(float(COST)))
      SGSTD=("(0.25%)", (0.25*(float(COST)))+(float(COST)))
      TotalD=("(0.5%)",( 0.5*(COST))+(COST))

      Cost.set(costD)
      CGST.set(CGSTD)
      SGST.set(SGSTD)
      Total.set(TotalD)

def qExit():
      root.destroy()

def New():
      Sandwich.set(" ")
      Fries.set(" ")
      Coffee.set(" ")
      Cola.set(" ")
      Burger.set(" ")
      EmailID.set(" ")
      Cost.set(" ")
      CGST.set(" ")
      SGST.set(" ")
      Total.set(" ")
      

txtDisplay = Entry(f2, font=('google sans medium', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4,
                    bg="lavender", justify= 'right' )
txtDisplay.grid(columnspan=4)

#----------------------------------LINE 1-------------------------------------------------
btn7=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium', 20, 'bold'),
            text="7", bg="salmon", command=lambda: btnclick(7)).grid (row=2, column=0)
btn8=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium', 20, 'bold'),
            text="8", bg="salmon", command=lambda: btnclick(8)).grid (row=2, column=1)
btn9=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium',20, 'bold'),
            text="9", bg="salmon", command=lambda: btnclick(9)).grid (row=2, column=2)

Addition=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium', 20, 'bold'),
          text="+", bg='cadet blue', command=lambda: btnclick("+")).grid (row=2, column=3)
#----------------------------------LINE 2-------------------------------------------------
btn4=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium', 20, 'bold'),
            text="4", bg="salmon", command=lambda: btnclick(4)).grid (row=3, column=0)
btn5=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium', 20, 'bold'),
            text="5", bg="salmon", command=lambda: btnclick(5)).grid (row=3, column=1)
btn6=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium',20, 'bold'),
            text="6", bg="salmon", command=lambda: btnclick(6)).grid (row=3, column=2)

Substraction=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium', 20, 'bold'),
          text="-", bg='cadet blue', command=lambda: btnclick("-")).grid (row=3, column=3)
#----------------------------------LINE 3-------------------------------------------------
btn1=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium', 20, 'bold'),
            text="1", bg="salmon", command=lambda: btnclick(1)).grid (row=4, column=0)
btn2=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium', 20, 'bold'),
            text="2", bg="salmon", command=lambda: btnclick(2)).grid (row=4, column=1)
btn3=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium',20, 'bold'),
            text="3", bg="salmon", command=lambda: btnclick(3)).grid (row=4, column=2)

Division=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium', 20, 'bold'),
          text="/", bg='cadet blue', command=lambda: btnclick("/")).grid (row=4, column=3)
#----------------------------------LINE 4-------------------------------------------------
btn0=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium', 20, 'bold'),
            text="0", bg="salmon", command=lambda: btnclick(0)).grid (row=5, column=0)
btnClear=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium', 20, 'bold'),
            text="C", bg="salmon", command=btnClearDisplay).grid (row=5, column=1)
btnEqauls=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium',20, 'bold'),
            text="=", bg="salmon", command=btnEqualsInput).grid (row=5, column=2)

Multiply=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('google sans medium', 20, 'bold'),
          text="*", bg='cadet blue', command=lambda: btnclick("*")).grid (row=5, column=3)
#--------------------------------CONTENT INFO---------------------------------------------
Sandwich=StringVar()
Fries=StringVar()
Coffee=StringVar()
Cola=StringVar()
Burger=StringVar()
EmailID=StringVar()
Cost=StringVar()
CGST=StringVar()
SGST=StringVar()
Total=StringVar()

lblSandwich=Label(f1, font=('google sans medium', 16, 'bold'), text="Sandwich", bd=16, anchor='w')
lblSandwich.grid(row=0, column=0)
txtSandwich=Entry(f1, font=('google sans medium', 16, 'bold'), textvariable=Sandwich, bd=10, insertwidth=4,
                   bg='salmon',  justify='right')
txtSandwich.grid(row=0, column=1)

lblFries=Label(f1, font=('google sans medium', 16, 'bold'), text="Fries", bd=16, anchor='w')
lblFries.grid(row=1, column=0)
txtFries=Entry(f1, font=('google sans medium', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4,
                   bg='salmon', justify='right')
txtFries.grid(row=1, column=1)

lblCoffee=Label(f1, font=('google sans medium', 16, 'bold'), text="Coffee", bd=16, anchor='w')
lblCoffee.grid(row=2, column=0)
txtCoffee=Entry(f1, font=('google sans medium', 16, 'bold'), textvariable=Coffee, bd=10, insertwidth=4,
                   bg='salmon', justify='right')
txtCoffee.grid(row=2, column=1)

lblCola=Label(f1, font=('google sans medium',16, 'bold'), text="Cola", bd=16, anchor='w')
lblCola.grid(row=3, column=0)
txtCola=Entry(f1, font=('google sans medium', 16, 'bold'), textvariable=Cola, bd=10, insertwidth=4,
                   bg='salmon', justify='right')
txtCola.grid(row=3, column=1)

lblBurger=Label(f1, font=('google sans medium', 16, 'bold'), text="Burger", bd=16, anchor='w')
lblBurger.grid(row=4, column=0)
txtBurger=Entry(f1, font=('google sans medium', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4,
                   bg='salmon', justify='right')
txtBurger.grid(row=4, column=1)
#--------------------------------------BILL-----------------------------------------------
lblEmailID=Label(f1, font=('google sans medium', 16, 'bold'), text="Email ID", bd=16, anchor='w')
lblEmailID.grid(row=0, column=2)
txtEmailID=Entry(f1, font=('google sans medium', 16, 'bold'), textvariable=EmailID, bd=10, insertwidth=4,
                   bg='salmon', justify='right')
txtEmailID.grid(row=0, column=3)

lblCost=Label(f1, font=('google sans medium', 16, 'bold'), text="Cost", bd=16, anchor='w')
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('google sans medium', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4,
                   bg='salmon', justify='right')
txtCost.grid(row=1, column=3)

lblCGST=Label(f1, font=('google sans medium', 16, 'bold'), text="CGST", bd=16, anchor='w')
lblCGST.grid(row=2, column=2)
txtCGST=Entry(f1, font=('google sans medium', 16, 'bold'), textvariable=CGST, bd=10, insertwidth=4,
                   bg='salmon', justify='right')
txtCGST.grid(row=2, column=3)

lblSGST=Label(f1, font=('google sans medium', 16, 'bold'), text="SGST", bd=16, anchor='w')
lblSGST.grid(row=3, column=2)
txtSGST=Entry(f1, font=('google sans medium', 16, 'bold'), textvariable=SGST, bd=10, insertwidth=4,
                   bg='salmon', justify='right')
txtSGST.grid(row=3, column=3)

lblTotal=Label(f1, font=('google sans medium', 16, 'bold'), text="Total", bd=16, anchor='w')
lblTotal.grid(row=4, column=2)
txtTotal=Entry(f1, font=('google sans medium', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4,
                   bg='salmon', justify='right')
txtTotal.grid(row=4, column=3)
#============================================BUTTONS======================================
btnTotal=Button(f1, padx=16, pady=8, bd=16, fg="black", font=('google sans medium', 16, 'bold'),
            text="Total", bg="cadet blue", command=ref).grid (row=7, column=0)
btnNew=Button(f1, padx=16, pady=8, bd=16, fg="black", font=('google sans medium', 16, 'bold'),
            text="New", bg="cadet blue", command=New).grid (row=7, column=1)
btnExit=Button(f1, padx=16, pady=8, bd=16, fg="black", font=('google sans medium', 16, 'bold'),
            text="Exit", bg="cadet blue", command=qExit).grid (row=7, column=2)

root.mainloop()
