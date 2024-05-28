# !/bin/pyhton3

#   price = (rate/1000)*gram
#   gram  = (price*1000)/rate

from tkinter import Tk,Label,Entry,Button,END

# To check that price & rate are integers 
def inputchecker(price,rate):
    try:
        price= int(price)
        rate= int(rate)
        return True,price,rate
    except:
        return False,0,0

def calculate_data():
    price = priceEntry.get()
    rate = rateEntry.get()
    # Show MSG if input is BLANK

    value,priceint,rateint = inputchecker(price=price,rate=rate)

    if price =="" or rate=="":
        noteLabel = Label(text="Please FILL the CREDENTIALS")
        noteLabel.place(x=20,y=290)
    elif value:
        gram=(priceint*1000)/rateint
        # Clear GRAMENTRY and then Insert grams
        gramEntry.delete(0,END)
        gramEntry.insert(0,gram)
    else:
        # Show MSG if price OR RATE is not integers
        noteLabel = Label(text="Please Enter only INTEGERS")
        noteLabel.place(x=20,y=290)


def main():
    root = Tk()

    # To keep window TOP on all other softwares
    root.wm_attributes("-topmost", True)

    root.title("Gram teller")
    root.resizable(False,False)
    root.geometry("200x350")

    # Print PRICE on window
    priceLabel : Label = Label(root, text="Price : ", font=("Arial",15,"bold"))
    priceLabel.place(x=20,y=20)

    # To take PRICE from USER
    global priceEntry
    priceEntry = Entry(root)
    priceEntry.place(x=20,y=50 , width=150,height=35)

    
    # Print RATE on window
    rateLabel : Label = Label(root, text="Rate : ", font=("Arial",15,"bold"))
    rateLabel.place(x=20,y=90)

    # To take RATE from USER
    global rateEntry
    rateEntry = Entry(root)
    rateEntry.place(x=20,y=130 , width=150,height=35)

    button : Button = Button(root, text="Calculate",command=calculate_data)
    button.place(x=30,y=175)

    # Print GRAM on window
    gramLabel : Label = Label(root, text="Gram : ", font=("Arial",15,"bold"))
    gramLabel.place(x=20,y=220)

    # To show GRAMS on SCREEN
    global gramEntry
    gramEntry = Entry(root)
    gramEntry.place(x=20,y=250 , width=150,height=35)


    root.mainloop()

if __name__ == "__main__":
    main()