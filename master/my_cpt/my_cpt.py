from Tkinter import *

root = Tk()
root.geometry("450x600")
root.resizable(width=False, height=False)
root.configure(background='snow')

def login_page(create_account):
    def login_label():
        labelfont = ('helvetica', 50, 'bold')
        login = Label(root, text="LOGIN")
        login.config(font=labelfont, relief=SUNKEN)
        login.place(x=225, y=100, anchor=N)


    def user_label():
        labelfont = ('helvetica', 20)
        user = Label(root, text="Username: ")
        user.config(font=labelfont)
        user.place(x=125, y=250, anchor=N)
        user_entry = Entry(root)
        user_entry.place(x=280, y=252, anchor=N)


    def pass_label():
        labelfont = ('helvetica', 20)
        password = Label(root, text="Password: ")
        password.config(font=labelfont)
        password.place(x=125, y=290, anchor=N)
        password_entry = Entry(root)
        password_entry.place(x=280, y=292, anchor=N)


    def buttons(create_account):
        check = Checkbutton(root, text="Keep me logged in")
        check.place(x=225, y=350, anchor=N)

        button = Button(root, text="Create an account", command=create_account)
        button.place(x=225, y=400, anchor=N)


    def main(create_account):
        login_label()
        user_label()
        pass_label()
        buttons(create_account)


    main(create_account)

def create_account():
    def create_label():
        labelfont = ('helvetica', 30, 'bold')
        login_1 = Label(root, text="CREATE AN")
        login_1.config(font=labelfont, relief=SUNKEN)
        login_1.place(x=225, y=100, anchor=N)
        login_2 = Label(root, text="ACCOUNT")
        login_2.config(font=labelfont, relief=SUNKEN)
        login_2.place(x=225, y=141, anchor=N)


    def user_label():
        labelfont = ('helvetica', 20)
        user = Label(root, text="Username: ")
        user.config(font=labelfont)
        user.place(x=125, y=250, anchor=N)
        user_entry = Entry(root)
        user_entry.place(x=280, y=252, anchor=N)


    def pass_label():
        labelfont = ('helvetica', 20)
        password = Label(root, text="Password: ")
        password.config(font=labelfont)
        password.place(x=125, y=290, anchor=N)
        password_entry = Entry(root)
        password_entry.place(x=280, y=292, anchor=N)


    def create_button():
        button = Button(root, text="Create")
        button.place(x=225, y=350, anchor=N)


    def main():
        create_label()
        user_label()
        pass_label()
        create_button()

    main()

login_page(create_account)
root.mainloop()
