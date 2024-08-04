from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password():
    global password_input
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for x in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list += [random.choice(symbols) for i in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list += [random.choice(numbers) for x in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""

    for char in password_list:
        password += char
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH DATA ------------------------------- #
def search():
    user = ""
    password = ""
    user_search = web_site_input.get()
    dic = {}
    try:
        with open("data.json", "r") as data:
            data_file = json.load(data)
    except:
        messagebox.showerror(title="Error", message="No data file found")

    else:
        if user_search in data_file:
            dic = data_file[user_search]
            user = dic["user"]
            password = dic["password"]
            messagebox.showinfo(title=f"{user_search}", message=f"User: {user}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {user_search} exist")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_value = web_site_input.get()
    user_value = user_name_input.get()
    password_value = password_input.get()
    dic_web_site = {web_value: {
        "user": user_value,
        "password": password_value,
    }
    }

    if web_value == "" or user_value == "" or password_value == "":
        messagebox.showinfo(title="Opss", message="Please don't leave any field empty")
    else:
        try:
            with open("data.json", "r") as data:
                # Reding the data
                data_file = json.load(data)
                # Update the data
                data_file.update(dic_web_site)
        except:
            with open("data.json", "w") as ex_data:
                json.dump(dic_web_site, ex_data, indent=4)
        else:
            with open("data.json", "w") as data_file2:
                # Writing the data
                json.dump(data_file, data_file2, indent=4)

                web_site_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Canvas image
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
web_site_label = Label(text="Website")
web_site_label.grid(row=1, column=0)

user_name_label = Label(text="Email/Username")
user_name_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Inputs
web_site_input = Entry(width=19)
web_site_input.grid(row=1, column=1)
web_site_input.focus()

user_name_input = Entry(width=36)
user_name_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=19)
password_input.grid(row=3, column=1)

# Buttons
generate_password_b = Button(text="Generate Password", highlightthickness=0, command=random_password)
generate_password_b.grid(row=3, column=2)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=12, command=search)
search_button.grid(row=1, column=2)

window.mainloop()
