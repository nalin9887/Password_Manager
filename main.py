from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entr.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def savedata():
    user_website = web_inp.get()
    user_mail = mail_entry.get()
    user_password = pass_entr.get()

    new_data = {
        user_website : {
            "email": user_mail,
            "password": user_password,
        }
    }

    if len(user_password)==0 or len(user_mail)==0:
        print("sdsadsa")
        messagebox.askokcancel(title="WARNING!!!",message="You Have Not Filled Infor Correctyly!!")
    is_ok= messagebox.askyesnocancel(title=user_website,message=f"Email:   {user_mail}\nPassword:   {user_password}")

    #text=f"\n{user_website} || {user_mail} || {user_password}"
    try:
        with open("data.json","r") as data:
            datas=json.load(data)
            datas.update(new_data)
    except:
        print("No previous data found")
        datas=new_data
        pass

    else:
        with open("data.json", "w") as data:
                    json.dump(datas, data, indent=4)
        #passfile.write(text)
    finally:
        web_inp.delete(0,END)
        mail_entry.delete(0,END)
        pass_entr.delete(0,END)
        web_inp.focus()
# ------------------- Find password and mail  ----------------------- #
def findpass():
    website=web_inp.get()
    with open("data.json") as datas:
            data=json.load(datas)

            if website in data:
                print("dfsad")
                email=data[website]['email']
                password=data[website]["password"]
                messagebox.showinfo(title="Data",message=f"email:{email} password: {password}")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
Img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=Img)
canvas.grid(row=0,column=1)

website=Label(text="Website")
website.grid(row=1,column=0)

web_inp=Entry(width=35)
web_inp.focus()
web_inp.grid(row=1,column=1,columnspan=2)
user_website=web_inp.get()

mail=Label(text="Email/Username")
mail.grid(row=2,column=0)

mail_entry=Entry(width=35)
mail_entry.grid(row=2,column=1,columnspan=2)
user_mail=mail_entry.get()

password=Label(text="Password")
password.grid(row=3,column=0)

pass_entr=Entry(width=35)
pass_entr.grid(row=3,column=1,columnspan=3)
user_password=pass_entr.get()
print(user_password)
pass_button=Button(text="Genarate Password",command=generate_password,borderwidth=0)
pass_button.grid(row=3, column=2,columnspan=1)

add=Button(text="Add",width=35,command=savedata)
add.grid(row=4,column=1,columnspan=2)

search=Button(width=14,text="Search",command=findpass,borderwidth=0)
search.grid(row=1, column=2,columnspan=1)
window.mainloop()
