import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letter = [(random.choice(letters)) for item in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for j in range(nr_numbers)]
    password_list = pass_letter + pass_numbers + pass_symbols

    random.shuffle(password_list)
    pass_code = "".join(password_list)
    password_entry.insert(0, pass_code)
    pyperclip.copy(pass_code)



def save_data():
    website = box_label.get()
    password = password_entry.get()
    e_mail = mail_entry.get()
    new_data = {
        website: {
            "Email": e_mail,
            "password": password,
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(message="Sorry there as to be an entry.")
    else:
        try:
            with open("data.json", "r") as data:
                data_file = json.load(data)

        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            data_file.update(new_data)
            with open('data.json', 'w') as data:
                json.dump(data_file, data, indent=4)
        finally:
            box_label.delete(0, 'end')
            password_entry.delete(0, 'end')


def search_entry():
    website = box_label.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(file="Error", message="No data file Found.")
    else:
        if website in data:
            email = data[website]['Email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    finally:
        box_label.delete(0, 'end')



window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=200, width=200, bg="white", highlightthickness=20)
i_mage = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=i_mage)
canvas.grid(column=1, row=0)

web_label = tkinter.Label(text="Website:")
web_label.grid(column=0, row=1)
box_label = tkinter.Entry(width=21)
box_label.focus()
box_label.grid(row=1, column=1)

search_button = tkinter.Button(text="Search", command=search_entry, width=13)
search_button.grid(row=1, column=2)

web_label2 = tkinter.Label(text="Email/Username:")
web_label2.grid(column=0, row=2)
mail_entry = tkinter.Entry(width=35)
mail_entry.insert(0, "Billionaire@gmail.com")
mail_entry.grid(row=2, column=1, columnspan=2)

password_label = tkinter.Label(text="Password")
password_label.grid(column=0, row=3)
password_entry = tkinter.Entry(width=21)

password_entry.grid(column=1, row=3)

password_button = tkinter.Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()