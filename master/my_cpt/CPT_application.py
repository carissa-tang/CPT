from Tkinter import *


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        MainMenu(self)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, CreateAccount, CategoryPage, AddPage, ReportPage):
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

        labelfont = ('helvetica', 50, 'bold')
        login = Label(self, text="LOGIN")
        login.config(font=labelfont, relief=SUNKEN)
        login.grid(columnspan=2, pady=100, ipadx=10)

        labelfont = ('helvetica', 20)
        user = Label(self, text="Username: ", bg='snow')
        user.config(font=labelfont)
        user.grid(row=1, column=0, padx=(80, 10))
        user_entry = Entry(self)
        user_entry.grid(row=1, column=1, padx=(10, 60))

        password = Label(self, text="Password: ", bg='snow')
        password.config(font=labelfont)
        password.grid(row=2, column=0, padx=(80, 10), pady=10)
        password_entry = Entry(self)
        password_entry.grid(row=2, column=1, padx=(10, 60), pady=10)

        check = Checkbutton(self, text="Keep me logged in", bg='snow')
        check.grid(row=3, columnspan=2, pady=10)

        create_account = Button(self, text="Create a new account", command=lambda: controller.show_frame(CreateAccount))
        create_account.grid(row=4, columnspan=2)

        category_page = Button(self, text="Login", command=lambda: controller.show_frame(CategoryPage))
        category_page.grid(row=5, columnspan=2, pady=(1, 160))


class CreateAccount(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        labelfont = ('helvetica', 40, 'bold')
        title = Label(self, text="CREATE ACCOUNT")
        title.config(font=labelfont, relief=SUNKEN)
        title.grid(columnspan=2, padx=20, pady=100, ipadx=10)

        labelfont = ('helvetica', 20)
        user = Label(self, text="Username: ", bg='snow')
        user.config(font=labelfont)
        user.grid(row=1, column=0, padx=(80, 10))
        user_entry = Entry(self)
        user_entry.grid(row=1, column=1, padx=(10, 60))

        password = Label(self, text="Password: ", bg='snow')
        password.config(font=labelfont)
        password.grid(row=2, column=0, padx=(80, 10), pady=10)
        password_entry = Entry(self)
        password_entry.grid(row=2, column=1, padx=(10, 60), pady=10)

        category_page = Button(self, text="Create account", command=lambda: controller.show_frame(CategoryPage))
        category_page.grid(row=3, columnspan=2, pady=10)


class CategoryPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        labelfont = ('helvetica', 50, 'bold')
        title = Label(self, text="Category Page")
        title.config(font=labelfont, relief=SUNKEN)
        title.grid(columnspan=2, padx=10, pady=20, ipadx=10)

        login_page = Button(self, text="Report", command=lambda: controller.show_frame(ReportPage))
        login_page.grid(columnspan=2, row=7, pady=(20, 1))

        labelfont = ('helvetica', 20)
        technology = Button(self, text="technology", width=12, command=lambda: controller.show_frame(AddPage))
        technology.config(font=labelfont)
        technology.grid(pady=10, row=1, column=0)

        clothing = Button(self, text="clothing", width=12, command=lambda: controller.show_frame(AddPage))
        clothing.config(font=labelfont)
        clothing.grid(pady=10, row=2, column=0)

        shoes = Button(self, text="shoes", width=12, command=lambda: controller.show_frame(AddPage))
        shoes.config(font=labelfont)
        shoes.grid(pady=10, row=3, column=0)

        public_transport = Button(self, text="public transport", width=12, command=lambda: controller.show_frame(AddPage))
        public_transport.config(font=labelfont)
        public_transport.grid(pady=10, row=4, column=0)

        travel = Button(self, text="travel", width=12, command=lambda: controller.show_frame(AddPage))
        travel.config(font=labelfont)
        travel.grid(pady=10, row=5, column=0)

        vehicle = Button(self, text="vehicle", width=12, command=lambda: controller.show_frame(AddPage))
        vehicle.config(font=labelfont)
        vehicle.grid(pady=10, row=6, column=0)

        pet = Button(self, text="pet", width=12, command=lambda: controller.show_frame(AddPage))
        pet.config(font=labelfont)
        pet.grid(pady=10, row=1, column=1)

        books = Button(self, text="books", width=12, command=lambda: controller.show_frame(AddPage))
        books.config(font=labelfont)
        books.grid(pady=10, row=2, column=1)

        cosmetics = Button(self, text="cosmetics", width=12, command=lambda: controller.show_frame(AddPage))
        cosmetics.config(font=labelfont)
        cosmetics.grid(pady=10, row=3, column=1)

        stationary = Button(self, text="stationary", width=12, command=lambda: controller.show_frame(AddPage))
        stationary.config(font=labelfont)
        stationary.grid(pady=10, row=4, column=1)

        restaurant = Button(self, text="restaurant", width=12, command=lambda: controller.show_frame(AddPage))
        restaurant.config(font=labelfont)
        restaurant.grid(pady=10, row=5, column=1)

        gifts = Button(self, text="gifts", width=12, command=lambda: controller.show_frame(AddPage))
        gifts.config(font=labelfont)
        gifts.grid(pady=10, row=6, column=1)


class AddPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        labelfont = ('helvetica', 50, 'bold')
        title = Label(self, text="'Category'")
        title.config(font=labelfont, relief=SUNKEN)
        title.pack(padx=10, pady=10)

        labelfont = ('helvetica', 20)
        amount = Label(self, text="Amount: ")
        amount.config(font=labelfont)
        amount.pack(padx=10, pady=10)
        amount_entry = Entry(self)
        amount_entry.pack()

        add = Button(self, text="add", command=lambda: controller.show_frame(CategoryPage))
        add.pack()


class ReportPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        labelfont = ('helvetica', 50, 'bold')
        title = Label(self, text="Report")
        title.config(font=labelfont, relief=SUNKEN)
        title.pack(padx=10, pady=10)

        add = Button(self, text="back", command=lambda: controller.show_frame(CategoryPage))
        add.pack()



class MainMenu:
    def __init__(self, master):
        menu_bar = Menu(master)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=master.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        master.config(menu=menu_bar)


app = App()
app.mainloop()
