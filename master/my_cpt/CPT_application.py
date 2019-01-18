from Tkinter import *
users = []
passwords = []


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        MainMenu(self)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, CreateAccount, CategoryPage, AddPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.config(background='snow')

        self.show_frame(LoginPage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()


class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def title():
            labelfont = ('helvetica', 50, 'bold')
            login = Label(self, text="LOGIN")
            login.config(font=labelfont, relief=SUNKEN)
            login.grid(columnspan=2, pady=100, ipadx=10)

        def labels(text, row, y):
            labelfont = ('helvetica', 20)
            label = Label(self, text=text, bg='snow')
            label.config(font=labelfont)
            label.grid(row=row, column=0, padx=(80, 10), pady=y)

        def login():
            global users, passwords
            username = user_entry2.get()
            password = password_entry2.get()
            if username in users:
                i_user = [i for i, s in enumerate(users) if username in s]
                i_pass = [i for i, s in enumerate(passwords) if password in s]
                if indice_user == indice_pass:
                    controller.show_frame(CategoryPage)
            else:
                text = Label(self, text="Invalid username/password", bg='snow', fg='red')
                text.grid(row=5, columnspan=2)

        def entries():
            global user_entry2, password_entry2
            user_entry2 = Entry(self)
            user_entry2.grid(row=1, column=1, padx=(10, 60))

            password_entry2 = Entry(self, show="*")
            password_entry2.grid(row=2, column=1, padx=(10, 60), pady=10)

        def buttons():
            check = Checkbutton(self, text="Keep me logged in", bg='snow')
            check.grid(row=3, columnspan=2, pady=10)

            create_account = Button(self, text="Create a new account", command=lambda: controller.show_frame(CreateAccount))
            create_account.grid(row=4, columnspan=2)

            category_page = Button(self, text="Login", command=login)
            category_page.grid(row=5, columnspan=2, pady=(1, 160))

        def main():
            title()
            labels("Username: ", 1, 0)
            labels("Password: ", 2, 10)
            entries()
            buttons()

        main()


class CreateAccount(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def title():
            labelfont = ('helvetica', 40, 'bold')
            title = Label(self, text="CREATE ACCOUNT")
            title.config(font=labelfont, relief=SUNKEN)
            title.grid(columnspan=2, padx=20, pady=100, ipadx=10)

        def labels(text, row, y):
            labelfont = ('helvetica', 20)
            label = Label(self, text=text, bg='snow')
            label.config(font=labelfont)
            label.grid(row=row, column=0, padx=(80, 10), pady=y)

        def create_account():
            global users, passwords
            username = user_entry1.get()
            password = pass_entry1.get()
            users.append(username)
            passwords.append(password)
            controller.show_frame(LoginPage)

        def entries():
            global user_entry1, pass_entry1
            user_entry1 = Entry(self)
            user_entry1.grid(row=1, column=1, padx=(10, 60))
            pass_entry1 = Entry(self, show="*")
            pass_entry1.grid(row=2, column=1, padx=(10, 60))

        def button():
            create_button = Button(self, text="Create account", command=create_account)
            create_button.grid(row=3, columnspan=2, pady=10)

        def main():
            title()
            labels("Username: ", 1, 0)
            labels("Password: ", 2, 10)
            entries()
            button()

        main()


class CategoryPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def title():
            labelfont = ('helvetica', 50, 'bold')
            title = Label(self, text="Category Page")
            title.config(font=labelfont, relief=SUNKEN)
            title.grid(columnspan=2, padx=(40, 10), pady=20, ipadx=10)

        def pie_chart():
            import matplotlib
            matplotlib.use('TkAgg')
            import matplotlib.pyplot as plt

            categories = ['vehicle', 'shoes', 'gifts', 'travel']
            slices = [15, 45, 24, 10]

            plt.pie(slices, labels=categories, autopct='%1.1f%%', shadow=True, startangle=140)
            plt.axis('equal')
            plt.title('Monthly Expenses')
            plt.show()

        def button():
            login_page = Button(self, text="Report", command=pie_chart)
            login_page.grid(columnspan=2, row=7, pady=(20, 1), padx=(20, 1))

        def categories(text, row, column):
            labelfont = ('helvetica', 20)
            category = Button(self, text=text, width=12, command=lambda: controller.show_frame(AddPage))
            category.config(font=labelfont)
            category.grid(pady=10, row=row, column=column, padx=(25, 1))

        def main():
            title()
            button()
            categories("technology", 1, 0)
            categories("clothing", 2, 0)
            categories("shoes", 3, 0)
            categories("public transport", 4, 0)
            categories("travel", 5, 0)
            categories("vehicle", 6, 0)
            categories("pet", 1, 1)
            categories("books", 2, 1)
            categories("cosmetics", 3, 1)
            categories("stationary", 4, 1)
            categories("restaurant", 5, 1)
            categories("gifts", 6, 1)

        main()


class AddPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def labels():
            labelfont = ('helvetica', 50, 'bold')
            title = Label(self, text="'Category'")
            title.config(font=labelfont, relief=SUNKEN)
            title.pack(padx=10, pady=10, ipadx=10)

            labelfont = ('helvetica', 20)
            amount = Label(self, text="Amount: ")
            amount.config(font=labelfont)
            amount.pack(padx=10, pady=10)

        def entry():
            amount_entry = Entry(self)
            amount_entry.pack()

        def button():
            add = Button(self, text="add", command=lambda: controller.show_frame(CategoryPage))
            add.pack()

        def main():
            labels()
            entry()
            button()

        main()


class ReportPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def label():
            labelfont = ('helvetica', 50, 'bold')
            title = Label(self, text="Report")
            title.config(font=labelfont, relief=SUNKEN)
            title.pack(padx=10, pady=10, ipadx=10)

        def button():
            add = Button(self, text="back", command=lambda: controller.show_frame(CategoryPage))
            add.pack()

        def main():
            label()
            button()

        main()


class MainMenu:
    def __init__(self, master):
        menu_bar = Menu(master)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=master.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        master.config(menu=menu_bar)


app = App()
app.mainloop()
