import psycopg
from database.user_dao import UserDao
import tkinter as tk
from tkinter import scrolledtext

def list_users(text_area):
    conn = psycopg.connect(
        dbname='postgres',
        user='postgres',
        password="sua_senha",
        host="localhost",
        port="5432"
    )

    # initialize DAOs

    userDao = UserDao(conn)
    #... TowelDaos, etc

    # Code logic

    users = userDao.getAllUsers()

    for user in users:
        text_area.insert(tk.END, f'user: {user.toString()}\n')
    conn.close()

# Create main window
root = tk.Tk()
root.title("User List")

# Create text area to display users
text_area = scrolledtext.ScrolledText(root, width=40, height=10)
text_area.pack()

action_function = lambda: list_users(text_area)

# Button to list users
list_button = tk.Button(root, text="List Users", command=action_function)
list_button.pack()

# Run the main event loop
root.mainloop()
