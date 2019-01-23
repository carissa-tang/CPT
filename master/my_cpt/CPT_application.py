from Tkinter import *

users = []
passwords = []

# categories and list containing its values#
dictionary = {
    "technology": [],
    "clothing": [],
    "shoes": [],
    "public transport": [],
    "travel": [],
    "vehicle": [],
    "pet": [],
    "books": [],
    "cosmetics": [],
    "stationary": [],
    "restaurant": [],
    "gifts": []
}

# variables for total_sums of values in each category
tech_sum = 0
cloth_sum = 0
shoes_sum = 0
transport_sum = 0
travel_sum = 0
vehicle_sum = 0
pet_sum = 0
books_sum = 0
cos_sum = 0
stat_sum = 0
rest_sum = 0
gifts_sum = 0

label_font = ('helvetica', 20)


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        MainMenu(self)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # navigate between different pages
        for F in (LoginPage, CreateAccount, CategoryPage, TechnologyPage,
                  ClothingPage, ShoesPage, PublicTransportPage, TravelPage,
                  VehiclePage, PetPage, BooksPage, CosmeticsPage,
                  StationaryPage, RestaurantPage, GiftsPage):
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
            title_font = ('helvetica', 50, 'bold')
            login_title = Label(self, text="LOGIN")
            login_title.config(font=title_font, relief=SUNKEN)
            login_title.grid(columnspan=2, pady=100, ipadx=10)

        def labels(text, row, y):
            global label_font
            label = Label(self, text=text, bg='snow')
            label.config(font=label_font)
            label.grid(row=row, column=0, padx=(80, 10), pady=y)

        # Checks if username and password exist
        def login():
            global users, passwords
            username = user_entry2.get()
            password = password_entry2.get()
            if username in users:
                i_user = [i for i, s in enumerate(users) if username in s]
                i_pass = [i for i, s in enumerate(passwords) if password in s]
                if i_user == i_pass:
                    controller.show_frame(CategoryPage)
            else:
                text = Label(self, text="Invalid username/password",
                             bg='snow', fg='red')
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

            create_account = Button(self, text="Create a new account",
                                    command=lambda:
                                    controller.show_frame(CreateAccount))
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
            title_font = ('helvetica', 40, 'bold')
            create_title = Label(self, text="CREATE ACCOUNT")
            create_title.config(font=title_font, relief=SUNKEN)
            create_title.grid(columnspan=2, padx=20, pady=100, ipadx=10)

        def labels(text, row, y):
            global label_font
            label = Label(self, text=text, bg='snow')
            label.config(font=label_font)
            label.grid(row=row, column=0, padx=(80, 10), pady=y)

        # Stores new username and password
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
            create_button = Button(self, text="Create account",
                                   command=create_account)
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
            title_font = ('helvetica', 50, 'bold')
            category_title = Label(self, text="Category Page")
            category_title.config(font=title_font, relief=SUNKEN)
            category_title.grid(columnspan=2, padx=(40, 10), pady=20, ipadx=10)

        # Takes categories and its values to make a pie chart
        def pie_chart():
            global tech_sum, cloth_sum, shoes_sum, transport_sum
            global travel_sum, vehicle_sum, pet_sum, books_sum
            global cos_sum, stat_sum, rest_sum, gifts_sum
            import matplotlib
            matplotlib.use('TkAgg')
            import matplotlib.pyplot as plt

            category_names = ["technology", "clothing", "shoes",
                              "public transport", "travel", "vehicle",
                              "pet", "books", "cosmetics",
                              "stationary", "restaurant", "gifts"]
            slices = [tech_sum, cloth_sum, shoes_sum, transport_sum,
                      travel_sum, vehicle_sum, pet_sum, books_sum,
                      cos_sum, stat_sum, rest_sum, gifts_sum]

            plt.pie(slices, labels=category_names, autopct='%1.1f%%',
                    shadow=True, startangle=140)
            plt.axis('equal')
            plt.title('Monthly Expenses')
            plt.show()

        def button():
            login_page = Button(self, text="Report", command=pie_chart)
            login_page.grid(columnspan=2, row=7, pady=(20, 1), padx=(20, 1))

        def categories(text, row, column, page):
            global label_font
            category = Button(self, text=text, width=12,
                              command=lambda: controller.show_frame(page))
            category.config(font=label_font)
            category.grid(pady=10, row=row, column=column, padx=(25, 1))

        def main():
            title()
            button()
            categories("technology", 1, 0, TechnologyPage)
            categories("clothing", 2, 0, ClothingPage)
            categories("shoes", 3, 0, ShoesPage)
            categories("public transport", 4, 0, PublicTransportPage)
            categories("travel", 5, 0, TravelPage)
            categories("vehicle", 6, 0, VehiclePage)
            categories("pet", 1, 1, PetPage)
            categories("books", 2, 1, BooksPage)
            categories("cosmetics", 3, 1, CosmeticsPage)
            categories("stationary", 4, 1, StationaryPage)
            categories("restaurant", 5, 1, RestaurantPage)
            categories("gifts", 6, 1, GiftsPage)

        main()


def category_labels(self, title):
    global label_font
    title_font = ('helvetica', 40, 'bold')
    title = Label(self, text=title)
    title.config(font=title_font, relief=SUNKEN)
    title.pack(padx=10, pady=10, ipadx=10)

    amount = Label(self, text="Amount: ")
    amount.config(font=label_font)
    amount.pack(padx=10, pady=10)


class TechnologyPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        category_labels(self, "Technology")

        def add_button():
            global dictionary, tech_sum
            new_amount = amount_entry.get()
            try:
                dictionary["technology"].append(int(new_amount))
            except:
                text = Label(self, text="Please enter a number.",
                             bg='snow', fg='red')
                text.pack()
            else:
                controller.show_frame(CategoryPage)
            total_sum = 0
            for number in dictionary["technology"]:
                total_sum += number
            tech_sum = total_sum

        amount_entry = Entry(self)
        amount_entry.pack()

        add = Button(self, text="add", command=add_button)
        add.pack()


class ClothingPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        category_labels(self, "Clothing")

        def add_button():
            global dictionary, cloth_sum
            new_amount = amount_entry.get()
            try:
                dictionary["clothing"].append(int(new_amount))
            except:
                text = Label(self, text="Please enter a number.",
                             bg='snow', fg='red')
                text.pack()
            else:
                controller.show_frame(CategoryPage)
            total_sum = 0
            for number in dictionary["clothing"]:
                total_sum += number
            cloth_sum = total_sum

        amount_entry = Entry(self)
        amount_entry.pack()

        add = Button(self, text="add", command=add_button)
        add.pack()


class ShoesPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        category_labels(self, "Shoes")

        def add_button():
            global dictionary, shoes_sum
            new_amount = amount_entry.get()
            try:
                dictionary["shoes"].append(int(new_amount))
            except:
                text = Label(self, text="Please enter a number.",
                             bg='snow', fg='red')
                text.pack()
            else:
                controller.show_frame(CategoryPage)
            total_sum = 0
            for number in dictionary["shoes"]:
                total_sum += number
            shoes_sum = total_sum

        amount_entry = Entry(self)
        amount_entry.pack()

        add = Button(self, text="add", command=add_button)
        add.pack()


class PublicTransportPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        category_labels(self, "Public Transport")

        def add_button():
            global dictionary, transport_sum
            new_amount = amount_entry.get()
            try:
                dictionary["shoes"].append(int(new_amount))
            except:
                text = Label(self, text="Please enter a number.",
                             bg='snow', fg='red')
                text.pack()
            else:
                controller.show_frame(CategoryPage)
            total_sum = 0
            for number in dictionary["shoes"]:
                total_sum += number
            transport_sum = total_sum

        amount_entry = Entry(self)
        amount_entry.pack()

        add = Button(self, text="add", command=add_button)
        add.pack()


class TravelPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        category_labels(self, "Travel")

        def add_button():
            global dictionary, travel_sum
            new_amount = amount_entry.get()
            try:
                dictionary["travel"].append(int(new_amount))
            except:
                text = Label(self, text="Please enter a number.",
                             bg='snow', fg='red')
                text.pack()
            else:
                controller.show_frame(CategoryPage)
            total_sum = 0
            for number in dictionary["travel"]:
                total_sum += number
            travel_sum = total_sum

        amount_entry = Entry(self)
        amount_entry.pack()

        add = Button(self, text="add", command=add_button)
        add.pack()


class VehiclePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        category_labels(self, "Vehicle")

        def add_button():
            global dictionary, vehicle_sum
            new_amount = amount_entry.get()
            try:
                dictionary["vehicle"].append(int(new_amount))
            except:
                text = Label(self, text="Please enter a number.",
                             bg='snow', fg='red')
                text.pack()
            else:
                controller.show_frame(CategoryPage)
            total_sum = 0
            for number in dictionary["vehicle"]:
                total_sum += number
            vehicle_sum = total_sum

        amount_entry = Entry(self)
        amount_entry.pack()

        add = Button(self, text="add", command=add_button)
        add.pack()


class PetPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        category_labels(self, "Pet")

        def add_button():
            global dictionary, pet_sum
            new_amount = amount_entry.get()
            try:
                dictionary["pet"].append(int(new_amount))
            except:
                text = Label(self, text="Please enter a number.",
                             bg='snow', fg='red')
                text.pack()
            else:
                controller.show_frame(CategoryPage)
            total_sum = 0
            for number in dictionary["pet"]:
                total_sum += number
            pet_sum = total_sum

        amount_entry = Entry(self)
        amount_entry.pack()

        add = Button(self, text="add", command=add_button)
        add.pack()


class BooksPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        category_labels(self, "Books")

        def add_button():
            global dictionary, books_sum
            new_amount = amount_entry.get()
            try:
                dictionary["books"].append(int(new_amount))
            except:
                text = Label(self, text="Please enter a number.",
                             bg='snow', fg='red')
                text.pack()
            else:
                controller.show_frame(CategoryPage)
            total_sum = 0
            for number in dictionary["books"]:
                total_sum += number
            books_sum = total_sum

        amount_entry = Entry(self)
        amount_entry.pack()

        add = Button(self, text="add", command=add_button)
        add.pack()


class CosmeticsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        category_labels(self, "Cosmetics")

        def add_button():
            global dictionary, cos_sum
            new_amount = amount_entry.get()
            try:
                dictionary["cosmetics"].append(int(new_amount))
            except:
                text = Label(self, text="Please enter a number.",
                             bg='snow', fg='red')
                text.pack()
            else:
                controller.show_frame(CategoryPage)
            total_sum = 0
            for number in dictionary["cosmetics"]:
                total_sum += number
            cos_sum = total_sum

        amount_entry = Entry(self)
        amount_entry.pack()

        add = Button(self, text="add", command=add_button)
        add.pack()


class StationaryPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        category_labels(self, "Stationary")

        def add_button():
            global dictionary, stat_sum
            new_amount = amount_entry.get()
            try:
                dictionary["stationary"].append(int(new_amount))
            except:
                text = Label(self, text="Please enter a number.",
                             bg='snow', fg='red')
                text.pack()
            else:
                controller.show_frame(CategoryPage)
            total_sum = 0
            for number in dictionary["stationary"]:
                total_sum += number
            stat_sum = total_sum

        amount_entry = Entry(self)
        amount_entry.pack()

        add = Button(self, text="add", command=add_button)
        add.pack()


class RestaurantPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        category_labels(self, "Restaurant")

        def add_button():
            global dictionary, rest_sum
            new_amount = amount_entry.get()
            try:
                dictionary["restaurant"].append(int(new_amount))
            except:
                text = Label(self, text="Please enter a number.",
                             bg='snow', fg='red')
                text.pack()
            else:
                controller.show_frame(CategoryPage)
            total_sum = 0
            for number in dictionary["restaurant"]:
                total_sum += number
            rest_sum = total_sum

        amount_entry = Entry(self)
        amount_entry.pack()

        add = Button(self, text="add", command=add_button)
        add.pack()


class GiftsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        category_labels(self, "Gifts")

        def add_button():
            global dictionary, gifts_sum
            new_amount = amount_entry.get()
            try:
                dictionary["gifts"].append(int(new_amount))
            except:
                text = Label(self, text="Please enter a number.",
                             bg='snow', fg='red')
                text.pack()
            else:
                controller.show_frame(CategoryPage)
            total_sum = 0
            for number in dictionary["gifts"]:
                total_sum += number
            gifts_sum = total_sum

        amount_entry = Entry(self)
        amount_entry.pack()

        add = Button(self, text="add", command=add_button)
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
