from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

CREAM = "#FFF7D4"
YELLOW = "#FFD95A"
BROWN = "#C07F00"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_enter.delete(0, END)
    password_enter.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_file():
    website = website_enter.get()
    email = email_enter.get()
    password = password_enter.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}"
                                                              f"\nPassword:{password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a", encoding="UTF-8") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_enter.delete(0, END)
                password_enter.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg=YELLOW)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg=YELLOW)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg=YELLOW)
password_label.grid(column=0, row=3)

website_enter = Entry(width=51)
website_enter.grid(row=1, column=1, columnspan=2)
website_enter.focus()

email_enter = Entry(width=51)
email_enter.grid(row=2, column=1, columnspan=2)
email_enter.insert(0, "0riq4mi@gmail.com")

password_enter = Entry(width=33)
password_enter.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=save_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
