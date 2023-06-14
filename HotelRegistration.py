#-------------------------------------------------------------------------------
# Name:        HotelManagementSystem.py
# Purpose:     A system for a booking system with a database for a hotel
#
# Author:      Dylan Porter
#
# Created:     11/12/2021
# Copyright:   (c) Dylan 2021-2022
# Licence:     notareallicence.com
#-------------------------------------------------------------------------------

# Importing tkinter, random, and os modules for later usage
import tkinter.ttk, random, os

# Defines the menu subprogram where the user starts
def menu():
    # Globalises the database variable for usage outside of the subprogram
    global database

    # Generates the GUI for the menu screen and removes the GUI for other screens that call it
    menu_screen.pack(expand=True)
    login_screen.pack_forget()
    register_screen.pack_forget()
    dashboard_screen.pack_forget()
    confirmation_screen.pack_forget()
    transaction_screen.pack_forget()
    manager_screen.pack_forget()

    # Assigns a title and a pixel size for the menu screen
    root.title("The ICS3U Hotel | Menu")
    root.geometry("350x300")

    # https://stackoverflow.com/questions/3925614/how-do-you-read-a-file-into-a-list-in-python
    # Reading lines from a file to place it into a list
    database = open("RoomKeys/database.txt").read().splitlines()

    # Declares the Tkinter variables
    menu_text = tkinter.Label(menu_screen, text="Welcome to the ICS3U Hotel!")
    # The button calls the login subprogram when pressed
    login_button = tkinter.ttk.Button(menu_screen, text="Login", width=2, command=login)
    # The button calls the register subprogram when pressed
    register_button = tkinter.ttk.Button(menu_screen, text="Register", width=2, command=register)

    # Places the Tkinter variables onto the screen
    menu_text.grid(column=0, row=0, columnspan=2)
    login_button.grid(column=0, row=1, pady=10, sticky="ew")
    register_button.grid(column=1, row=1, pady=10, sticky="ew")

# Defines the login subprogram where the users verify their identities
def login():

    # Generates the login GUI and removes all other GUIs that call it
    login_screen.pack(expand=True)
    menu_screen.pack_forget()
    confirmation_screen.pack_forget()

    # Changes its title and size
    root.title("The ICS3U Hotel | Login")
    root.geometry("350x300")

    # Declares the Tkinter variables for the GUI
    login_text = tkinter.Label(login_screen, text="Welcome Back!")
    id_text = tkinter.Label(login_screen, text="Login ID: ")
    id_entry = tkinter.ttk.Entry(login_screen)
    # https://www.delftstack.com/howto/python-tkinter/how-to-bind-multiple-commands-to-tkinter-button/
    # Using lambda to pass more than one command on tkinter button
    menu_button = tkinter.ttk.Button(login_screen, text="Back", command=lambda:[menu(), invalid_id.grid_forget()])
    # https://www.delftstack.com/howto/python-tkinter/how-to-pass-arguments-to-tkinter-button-command/
    # Using lambda to pass arguments in a tkinter button
    login_button = tkinter.ttk.Button(login_screen, text="Submit", command=lambda:login_submit(id_entry, invalid_id))
    invalid_id = tkinter.Label(login_screen, text="Invalid ID. Please try again.")

    # Adds the declared Tkinter variables to the screen
    login_text.grid(column=0, row=0, columnspan=2)
    id_text.grid(column=0, row=1, sticky="e")
    id_entry.grid(column=1, row=1, sticky="ew")
    menu_button.grid(column=0, row=2, sticky="ew")
    login_button.grid(column=1, row=2, sticky="ew")
    id_entry.focus_set()

# Defines the register subprogram where users create their accounts
def register():

    # Initialises the login screen information and removes all other screens that call it
    register_screen.pack(expand=True)
    menu_screen.pack_forget()
    root.title("The ICS3U Hotel | Register")
    root.geometry("350x300")


    # https://stackoverflow.com/questions/20453488/how-do-you-replace-a-label-in-tkinter-python
    # Replacing labels with StringVar() to allow for labels to change
    name_variable, credit_variable, email_variable, hkid_variable, agree_variable = tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar(), tkinter.IntVar()

    # Declares all of the variables for the GUI
    register_text = tkinter.Label(register_screen, text="Please enter your details below:")
    name_text = tkinter.Label(register_screen, text="Full name: ")
    credit_text = tkinter.Label(register_screen, text="Credit card number: ")
    email_text = tkinter.Label(register_screen, text="Email address: ")
    hkid_text = tkinter.Label(register_screen, text="HKID: ")
    name_entry = tkinter.ttk.Entry(register_screen, textvariable=name_variable)
    credit_entry = tkinter.ttk.Entry(register_screen, textvariable=credit_variable)
    email_entry = tkinter.ttk.Entry(register_screen, textvariable=email_variable)
    hkid_entry = tkinter.ttk.Entry(register_screen, textvariable=hkid_variable)
    menu_button = tkinter.ttk.Button(register_screen, text="Back", width=21, command=lambda: [menu(), invalid_details.grid_forget()])
    register_button = tkinter.ttk.Button(register_screen, text="Submit", width=21, command=lambda: register_submit(name_variable, credit_variable, email_variable, hkid_variable, invalid_details, detail_type), state="disabled")
    # https://www.tutorialspoint.com/python/tk_checkbutton.htm
    # Checkbuttons
    agree = tkinter.Checkbutton(register_screen, text="I agree to the terms & conditions", variable=agree_variable)
    agree.deselect()
    detail_type = tkinter.StringVar()
    invalid_details = tkinter.Label(register_screen, textvariable=detail_type)

    # Outputs the variables onto the GUI
    register_text.grid(column=0, row=0, sticky="s", columnspan=2)
    name_text.grid(column=0, row=1, sticky="e")
    credit_text.grid(column=0, row=2, sticky="e")
    email_text.grid(column=0, row=3, sticky="e")
    hkid_text.grid(column=0, row=4, sticky="e")
    name_entry.grid(column=1, row=1, sticky="ew")
    credit_entry.grid(column=1, row=2, sticky="ew")
    email_entry.grid(column=1, row=3, sticky="ew")
    hkid_entry.grid(column=1, row=4, sticky="ew")
    agree.grid(column=0, row=5, sticky="n", columnspan=2)
    menu_button.grid(column=0, row=6, sticky="e")
    register_button.grid(column=1, row=6, sticky="w")
    name_entry.focus_set()

    # https://python.hotexamples.com/site/file?hash=0xb2ce841fc6d5933a60d8727b6d18a2160c790d41383278790db0906a201516c5
    # Uses trace with lambda to call a subprogram every time the variable is updated
    name_variable.trace("w", lambda a, b, c, d=name_variable: change_state("register", register_button, name_variable.get(), credit_variable.get(), email_variable.get(), hkid_variable.get(), agree_variable.get()))
    credit_variable.trace("w", lambda a, b, c, d=credit_variable: change_state("register", register_button, name_variable.get(), credit_variable.get(), email_variable.get(), hkid_variable.get(), agree_variable.get()))
    email_variable.trace("w", lambda a, b, c, d=email_variable: change_state("register", register_button, name_variable.get(), credit_variable.get(), email_variable.get(), hkid_variable.get(), agree_variable.get()))
    hkid_variable.trace("w", lambda a, b, c, d=hkid_variable: change_state("register", register_button, name_variable.get(), credit_variable.get(), email_variable.get(), hkid_variable.get(), agree_variable.get()))
    agree_variable.trace("w", lambda a, b, c, d=agree_variable: change_state("register", register_button, name_variable.get(), credit_variable.get(), email_variable.get(), hkid_variable.get(), agree_variable.get()))

# Defines the login submission subprogram where the processing for logging in is done
def login_submit(id_entry, invalid_id):
    global user_entry, file

    # Takes the input from the entry box
    user_entry = id_entry.get()
    id_entry.delete(0, 'end')

    # Checks if the user's input is the manager ID or not
    if user_entry != manager_id:
        # Finds an existing file named with the user ID using file access if it isn't
        # Uses error handling to give an error message if the file does not exist
        #try:
            # https://www.w3schools.com/python/python_ref_file.asp
            # Python file access
            # https://www.w3schools.com/python/python_strings_slicing.asp
            # Python string slice syntax
        file = "UserIDs/%s.txt" % (user_entry)
        open(file)
        # Calls the dashboard subprogram
        dashboard()
        #except:
        invalid_id.grid(column=0, row=3, columnspan=3)
    else:
        # Calls the manager_dashboard subprogram if it is
        manager_dashboard()

# Defines the register submission subprogram where the register input is processed
def register_submit(name, credit, email, hkid, invalid_details, detail_type):
    # Creates a for loop to check if the name has no numbers
    for i in range(len(name.get())):
        try:
            int(name.get()[i])
            # Changes the detail_type variable to update the label
            detail_type.set("Invalid name entered (Letters only).")
            break
        except ValueError:
            continue
    else:
        # https://www.w3schools.com/python/ref_string_isnumeric.asp
        # Check if a variable is numerical
        # Checks if the credit card information has 11 digits
        if credit.get().isnumeric() and len(credit.get()) == 11:
            # Calls the confirmation subprogram
            confirmation(name, credit, email, hkid)
        else:
            detail_type.set("Invalid credit card number entered (11 digits only).")

    invalid_details.grid(column=0, row=7, columnspan=2)

# Defines the confirmation subprogram that shows a GUI after a successful registration
def confirmation(name_entry, credit_entry, email_entry, hkid_entry):
    confirmation_screen.pack(expand=True)
    register_screen.pack_forget()
    root.geometry("350x300")

    # Adds the information to a lsit and creates a list with random unique numbers between 1 and 800
    registration = [name_entry.get(), credit_entry.get(), email_entry.get(), hkid_entry.get()]
    user_id = random.sample(range(1,801),800)

    # Creates a for loop to add the ID to a file and output the information
    for n in range(len(user_id)):
        try:
            new_file = open("UserIDs/%s.txt" % (user_id[n]), "w")
            registration.append(user_id[n])
            for y in range(len(registration)):
                new_file.write("%s\n" % (registration[y]))
            thanks_message = tkinter.Label(confirmation_screen, text="Thank you for joining us, %s." % name_entry.get())
            assigned_id = tkinter.Label(confirmation_screen, text="Your login ID is %s." % user_id[n])
            continue_button = tkinter.ttk.Button(confirmation_screen, text="Login", command=login)
            thanks_message.grid(column=0, row=0, columnspan=2)
            continue_button.grid(column=0, row=2, columnspan=2)
            break
        except:
            continue
    else:
        # Outputs an error message if no IDs are available
        assigned_id = tkinter.Label(confirmation_screen, text="There were no available IDs.")
        menu_button = tkinter.ttk.Button(confirmation_screen, text="Menu", command=menu)
        menu_button.grid(column=0, row=2)

    assigned_id.grid(column=0, row=1, columnspan=2)

# Defines the dashboard subprogram where the purchases are selected
def dashboard():
    dashboard_screen.pack(expand=True)
    login_screen.pack_forget()
    invoice_screen.pack_forget()

    root.title("The ICS3U Hotel | Dashboard")
    root.geometry("350x300")

    # Declares StringVar() variables to update labels
    single_variable, double_variable, executive_variable, suite_variable, coupon_variable, date1_variable, date2_variable = tkinter.IntVar(), tkinter.IntVar(), tkinter.IntVar(), tkinter.IntVar(), tkinter.IntVar(), tkinter.StringVar(), tkinter.StringVar()

    # Initialises Tkinter variables to output onto the screen
    welcome_text = tkinter.Label(dashboard_screen, text="Welcome, %s." % open(file).readline()[:-1])
    booking_text = tkinter.Label(dashboard_screen, text="What room(s) would you like to book?")
    single_check = tkinter.Checkbutton(dashboard_screen, text="Single Bedroom", command=lambda: toggle_state(single_quantity, "customer"))
    double_check = tkinter.Checkbutton(dashboard_screen, text="Double Bedroom", command=lambda: toggle_state(double_quantity, "customer"))
    executive_check = tkinter.Checkbutton(dashboard_screen, text="Executive Room", command=lambda: toggle_state(executive_quantity, "customer"))
    suite_check = tkinter.Checkbutton(dashboard_screen, text="President Suite", command=lambda: toggle_state(suite_quantity, "customer"))
    single_check.deselect()
    double_check.deselect()
    executive_check.deselect()
    suite_check.deselect()
    # https://www.tutorialspoint.com/python/tk_spinbox.htm
    # Spinbox (number quantifier)
    single_quantity = tkinter.ttk.Spinbox(dashboard_screen, values=list(range(0,int(database[0])+1)), textvariable=single_variable, state="disabled", width=3)
    double_quantity = tkinter.ttk.Spinbox(dashboard_screen, values=list(range(0,int(database[1])+1)), textvariable=double_variable, state="disabled", width=3)
    executive_quantity = tkinter.ttk.Spinbox(dashboard_screen, values=list(range(0,int(database[2])+1)), textvariable=executive_variable, state="disabled", width=3)
    suite_quantity = tkinter.ttk.Spinbox(dashboard_screen, values=list(range(0,int(database[3])+1)), textvariable=suite_variable, state="disabled", width=3)
    coupons_check = tkinter.Checkbutton(dashboard_screen, text="Breakfast Coupons", variable=coupon_variable)
    # https://tkdocs.com/tutorial/widgets.html#combobox
    # Tkinter Combobox
    # https://stackoverflow.com/questions/134934/display-number-with-leading-zeros
    # Leading zeroes with string formatting
    # https://blog.finxter.com/python-one-line-for-loop-a-simple-tutorial/
    # One-line for loops
    date1 = tkinter.ttk.Combobox(dashboard_screen, values=[("%02d%s" % (x, "/01/21")) for x in range(1,32)], textvariable=date1_variable, state="readonly", width=10)
    date2 = tkinter.ttk.Combobox(dashboard_screen, values=[("%02d%s" % (x, "/01/21")) for x in range(1,32)], textvariable=date2_variable, state="readonly", width=10)
    checkin_text = tkinter.Label(dashboard_screen, text="Check-In Date")
    checkout_text = tkinter.Label(dashboard_screen, text="Check-Out Date")
    purchase_button = tkinter.ttk.Button(dashboard_screen, text="Purchase", command=lambda: purchase(single_quantity, double_quantity, executive_quantity, suite_quantity, coupon_variable, date1, date2, invalid_selections, selection), state="disabled")
    logout_button = tkinter.ttk.Button(dashboard_screen, text="Logout", command=lambda: [menu(), welcome_text.grid_forget(), invalid_selections.grid_forget()])

    # Initialises variables for error messages
    selection = tkinter.StringVar()
    invalid_selections = tkinter.Label(dashboard_screen, textvariable=selection)

    # Outputs the GUI variables onto the screen
    welcome_text.grid(column=0, row=0, columnspan=2)
    booking_text.grid(column=0, row=1, columnspan=2)
    single_check.grid(column=0, row=2)
    double_check.grid(column=0, row=3)
    executive_check.grid(column=0, row=4)
    suite_check.grid(column=0, row=5)
    single_quantity.grid(column=1, row=2)
    double_quantity.grid(column=1, row=3)
    executive_quantity.grid(column=1, row=4)
    suite_quantity.grid(column=1, row=5)
    coupons_check.grid(column=0, row=6, columnspan=2)
    date1.grid(column=0, row=7)
    date2.grid(column=1, row=7, sticky="w")
    checkin_text.grid(column=0, row=8)
    checkout_text.grid(column=1, row=8)
    purchase_button.grid(column=0, row=9, columnspan=2)
    logout_button.grid(column=0, row=10, columnspan=2)

    # Calls the change_state() subprogram every time one of the variables are updated
    single_variable.trace("w", lambda a, b, c, d=single_variable: change_state("dashboard", purchase_button, single_variable.get(), double_variable.get(), executive_variable.get(), suite_variable.get(), date1_variable.get(), date2_variable.get()))
    double_variable.trace("w", lambda a, b, c, d=double_variable: change_state("dashboard", purchase_button, single_variable.get(), double_variable.get(), executive_variable.get(), suite_variable.get(), date1_variable.get(), date2_variable.get()))
    executive_variable.trace("w", lambda a, b, c, d=executive_variable: change_state("dashboard", purchase_button, single_variable.get(), double_variable.get(), executive_variable.get(), suite_variable.get(), date1_variable.get(), date2_variable.get()))
    suite_variable.trace("w", lambda a, b, c, d=suite_variable: change_state("dashboard", purchase_button, single_variable.get(), double_variable.get(), executive_variable.get(), suite_variable.get(), date1_variable.get(), date2_variable.get()))
    date1_variable.trace("w", lambda a, b, c, d=date1_variable: change_state("dashboard", purchase_button, single_variable.get(), double_variable.get(), executive_variable.get(), suite_variable.get(), date1_variable.get(), date2_variable.get()))
    date2_variable.trace("w", lambda a, b, c, d=date2_variable: change_state("dashboard", purchase_button, single_variable.get(), double_variable.get(), executive_variable.get(), suite_variable.get(), date1_variable.get(), date2_variable.get()))

# Defines the purchase subprogram to process the dashboard input
def purchase(single, double, executive, suite, coupon, date1, date2, invalid_selections, selection):
    # Initialises two lists for processing
    user_entries, room_quantities, days = [single, double, executive, suite], [], (int(date2.get()[:2]) - int(date1.get()[:2]))

    # Runs a for loop to append valid user entries onto room amounts
    for x in user_entries: room_quantities.append(int(x.get())) if str(x["state"]) == "readonly" else room_quantities.append(0)
    if max(room_quantities) > 0:
        if days > 0:
            # Calls the invoice subprogram if the user's input is valid
            invoice(room_quantities, date1.get(), date2.get(), days, coupon)
        # Outputs error messages if the user's input is invalid
        else:
            selection.set("Invalid dates entered.")
    else:
        selection.set("Please select at least one room.")

    invalid_selections.grid(column=0, row=11, columnspan=2)

# Defines the invoice subprogram that prints a table for an overview of the user's selections
def invoice(rooms, date1, date2, days, coupon):
    invoice_screen.pack(expand=True)
    dashboard_screen.pack_forget()
    root.title("The ICS3U Hotel | Invoice")
    root.geometry("350x300")

    total_price = 0

    # Defines the Tkinter variables for output onto the GUI
    hotel_text = tkinter.Label(invoice_screen, text="Thank you for choosing the ICS3U Hotel!")
    starting_date = tkinter.Label(invoice_screen, text="Check-in Date: %s" % date1)
    ending_date = tkinter.Label(invoice_screen, text="Check-out Date: %s" % date2)
    adjust_button = tkinter.ttk.Button(invoice_screen, text="Back", command=dashboard)
    confirm_button = tkinter.ttk.Button(invoice_screen, text="Confirm", command=lambda: invoice_submit(total_price, date1, date2, rooms))
    # https://stackoverflow.com/questions/47515014/how-do-i-use-tkinter-treeview-to-list-items-in-a-table-of-a-database
    # https://www.tutorialspoint.com/how-can-i-set-the-row-height-in-tkinter-treeview
    # Using Treeview to make a table
    table = tkinter.ttk.Treeview(invoice_screen, show="headings", columns=["Unit Type", "Quantity", "Pricing ($HKD/day)"], height=6)
    table.column("Unit Type", anchor="center", width=120, stretch=False)
    table.heading("Unit Type", text="Unit Type")
    table.column("Quantity", anchor="center", width=80, stretch=False)
    table.heading("Quantity", text="Quantity")
    table.column("Pricing ($HKD/day)", anchor="center", width=120, stretch=False)
    table.heading("Pricing ($HKD/day)", text="Pricing ($HKD/day)")
    # Creates a for loop to insert each row onto the table
    for w in range(len(rooms)):
        if rooms[w] > 0:
            # https://stackoverflow.com/questions/14029245/putting-an-if-elif-else-statement-on-one-line
            # One-line if-elif-else through nesting
            room_type = "Single Bedroom" if w == 0 else "Double Bedroom" if w == 1 else "Executive Room" if w == 2 else "President Suite"
            table.insert("", w, w, values=(room_type, rooms[w], database[w+5]))
            total_price += (int(database[w+5]) * rooms[w]) * days
    if coupon.get() == 1:
        table.insert("", 4, 4, values=("Breakfast Coupon", "", 50))
        total_price += (50*days)
    table.insert("", 5, 5, values=("", "Grand Total:", total_price))

    # Outputs the Tkinter widgets onto the GUI
    hotel_text.grid(column=0, row=0, columnspan=2)
    table.grid(column=0, row=1, columnspan=2)
    starting_date.grid(column=0, row=2)
    ending_date.grid(column=1, row=2)
    adjust_button.grid(column=0, row=3, sticky="ew")
    confirm_button.grid(column=1, row=3, sticky="ew")

# Defines the invoice submission subprogram to process the invoice details
def invoice_submit(price, date1, date2, rooms):
    # Updates the database list with the selected rooms list
    for i in range(4): database[i] = int(database[i]) - int(rooms[i])
    database[4] = int(database[4]) + price

    # Generates a list with 99 unique numbers in a random order
    key_list = random.sample(range(900,1000),99)

    # Runs a for loop to create a unique file with the key name
    for g in range(len(key_list)):
        try:
            key_file = open("RoomKeys/%s.txt" % (key_list[g]), "w")
            key_file.write(user_entry)

            # Removes the existing database file and replaces it with an updated version

            # https://www.w3schools.com/python/python_file_remove.asp
            # Removing a file
            os.remove("RoomKeys/database.txt")
            # https://stackoverflow.com/questions/10355290/error-must-be-str-not-generator-in-python
            # Using join to place a generator inside of a file
            open("RoomKeys/database.txt", "w").write("\n".join(str(database[v]) for v in range(len(database))))
            # Calls the transaction subprogram
            transaction(key_list[g])
            break
        except:
            continue
    else:
        assigned_id = tkinter.Label(confirmation_screen, text="There were no available rooms.")
        menu_button = tkinter.ttk.Button(confirmation_screen, text="Menu", command=menu)
        menu_button.grid(column=0, row=2)

# Defines the transaction subprogram to give the user their key
def transaction(key):
    transaction_screen.pack(expand=True)
    invoice_screen.pack_forget()

    root.title("The ICS3U Hotel | Transaction")
    root.geometry("350x300")

    # Defines the Tkinter variables
    purchase_text = tkinter.Label(transaction_screen, text="Transaction successful!")
    key_text = tkinter.Label(transaction_screen, text="Your room key is %s." % (key))
    enjoy_text = tkinter.Label(transaction_screen, text="Enjoy your stay at the ICS3U Hotel!")
    menu_button = tkinter.ttk.Button(transaction_screen, text="Logout", command=menu)

    # https://www.geeksforgeeks.org/python-append-to-a-file/
    # Append to a file
    user_file = open(file, "a").write("%s" % key)

    # Places the information onto the screen
    purchase_text.grid(column=0, row=0)
    key_text.grid(column=0, row=1)
    enjoy_text.grid(column=0, row=2)
    menu_button.grid(column=0, row=3)

# Defines the toggle_state subprogram to change the state of a Tkinter widget using arguments
def toggle_state(item, user):
    # Uses if statements to check the current state to update it
    # https://www.geeksforgeeks.org/how-to-change-tkinter-button-state/
    # Changing button state
    if str(item["state"]) == "disabled":
        if user == "customer":
            item["state"] = "readonly"
        elif user == "manager":
            item["state"] = "enabled"
    else:
        item["state"] = "disabled"

# Defines the change_state subprogram to change the state of a Tkinter widget by checking multiple arguments when fields are filled
def change_state(*args):
    # https://stackoverflow.com/questions/16687124/python-tkinter-disable-the-button-until-all-the-fields-are-filled
    # Enables button when all fields are filled
    valid = False
    if args[0] == "register":
        if args[2] and args[3] and args[4] and args[5] and args[6]:
            valid = True
    elif args[0] == "dashboard":
        if (args[2] or args[3] or args[4] or args[5]) and (args[6] and args[7]):
            valid = True
    if valid == True:
        args[1]["state"] = "readonly"
    else:
        args[1]["state"] = "disabled"

# Defines the manager_dashboard subprogram where the manager can access a system to change the hotel information
def manager_dashboard():
    manager_screen.pack(expand=True)
    login_screen.pack_forget()
    information_screen.pack_forget()
    price_screen.pack_forget()
    statistics_screen.pack_forget()

    root.title("The ICS3U Hotel | Manager")
    root.geometry("350x300")

    # Declares the Tkinter variables to output onto the screen
    dashboard_text = tkinter.Label(manager_screen, text="The ICS3U Hotel Management Dashboard")
    customer_button = tkinter.ttk.Button(manager_screen, text="View Customer Information", command=customer_information)
    prices_button = tkinter.ttk.Button(manager_screen, text="Change Room Prices", command=change_prices)
    revenue_button = tkinter.ttk.Button(manager_screen, text="View Hotel Statistics", command=hotel_statistics)
    logout_button = tkinter.ttk.Button(manager_screen, text="Logout", command=menu)

    # Outputs the Tkinter variables
    dashboard_text.grid(column=0, row=0, sticky="ew")
    customer_button.grid(column=0, row=1, sticky="ew")
    prices_button.grid(column=0, row=2, sticky="ew")
    revenue_button.grid(column=0, row=3, sticky="ew")
    logout_button.grid(column=0, row=4)

# Defines the customer_information subprogram where a table with all users' information is outputted
def customer_information():
    information_screen.pack(expand=True)
    manager_screen.pack_forget()

    root.title("The ICS3U Hotel | Customer Info")
    root.geometry("750x300")

    # Declares Tkinter variables
    information_text = tkinter.Label(information_screen, text="Customer Information")
    table = tkinter.ttk.Treeview(information_screen, show="headings", columns=["Name", "Credit Card", "Email", "HKID", "Login Code", "Room Key"], height=5)
    table.column("Name", anchor="center", width=120, stretch=False)
    table.heading("Name", text="Name")
    table.column("Credit Card", anchor="center", width=120, stretch=False)
    table.heading("Credit Card", text="Credit Card")
    table.column("Email", anchor="center", width=120, stretch=False)
    table.heading("Email", text="Email")
    table.column("HKID", anchor="center", width=120, stretch=False)
    table.heading("HKID", text="HKID")
    table.column("Login Code", anchor="center", width=120, stretch=False)
    table.heading("Login Code", text="Login Code")
    table.column("Room Key", anchor="center", width=120, stretch=False)
    table.heading("Room Key", text="Room Key")
    back_button = tkinter.ttk.Button(information_screen, text="Back", command=manager_dashboard)

    # Uses a for loop to check through all UserIDs to read the information and insert it into the table
    for j in range(800):
        try:
            file = open("UserIDs/%s.txt" % (j)).read().splitlines()
            while len(file) < 6:
                file.append("N/A")
            table.insert("", j, j, values=(file[0], file[1], file[2], file[3], file[4], file[5]))
        except:
            continue

    # Outputs the Tkinter variables
    information_text.grid(column=0, row=0)
    table.grid(column=0, row=1)
    back_button.grid(column=0, row=2)

# Defines the change_prices subprogram where the room prices can be changed
def change_prices():
    price_screen.pack(expand=True)
    manager_screen.pack_forget()

    root.title("The ICS3U Hotel | Prices")
    root.geometry("350x300")

    # Declares the Tkinter variables
    single_check = tkinter.Checkbutton(price_screen, text="Single Bedroom Price: ", command=lambda: toggle_state(single_price, "manager"))
    double_check = tkinter.Checkbutton(price_screen, text="Double Bedroom Price: ", command=lambda: toggle_state(double_price, "manager"))
    executive_check = tkinter.Checkbutton(price_screen, text="Executive Room Price: ", command=lambda: toggle_state(executive_price, "manager"))
    suite_check = tkinter.Checkbutton(price_screen, text="President Suite Price: ", command=lambda: toggle_state(suite_price, "manager"))
    single_check.deselect()
    double_check.deselect()
    executive_check.deselect()
    suite_check.deselect()
    single_price = tkinter.ttk.Entry(price_screen, width=10)
    double_price = tkinter.ttk.Entry(price_screen, width=10)
    executive_price = tkinter.ttk.Entry(price_screen, width=10)
    suite_price = tkinter.ttk.Entry(price_screen, width=10)
    # https://www.delftstack.com/howto/python-tkinter/how-to-set-default-text-of-tkinter-entry-widget/
    # Setting the default text of an entry
    single_price.insert(0, database[5])
    double_price.insert(0, database[6])
    executive_price.insert(0, database[7])
    suite_price.insert(0, database[8])
    single_price["state"], double_price["state"], executive_price["state"], suite_price["state"] = "disabled", "disabled", "disabled", "disabled"
    confirm_button = tkinter.ttk.Button(price_screen, text="Confirm", command=lambda: process_price(single_price, double_price, executive_price, suite_price, price_notify, notification))
    return_button = tkinter.ttk.Button(price_screen, text="Back", command=lambda: [manager_dashboard(), price_notify.pack_forget()])

    notification = tkinter.StringVar()
    price_notify = tkinter.Label(price_screen, textvariable=notification)

    # Outputs the Tkinter variables onto the GUI
    single_check.grid(column=0, row=0)
    single_price.grid(column=1, row=0)
    double_check.grid(column=0, row=1)
    double_price.grid(column=1, row=1)
    executive_check.grid(column=0, row=2)
    executive_price.grid(column=1, row=2)
    suite_check.grid(column=0, row=3)
    suite_price.grid(column=1, row=3)
    confirm_button.grid(column=0, row=4, columnspan=2)
    return_button.grid(column=0, row=5, columnspan=2)

# Defines the process_price subprogram to process the selections in change_prices()
def process_price(single, double, executive, suite, price_notify, notification):
    # Assigns the input into a list and initialises an empty list
    entered_prices, new_prices = [single, double, executive, suite], []

    # https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
    # Using enumerate to access the index in a list
    # Creates a for loop to append the valid information into the empty list
    for index, h in enumerate(entered_prices):
        try:
            if str(h["state"]) == "enabled" and int(database[index+5]) != int(h.get()):
                new_prices.append(int(h.get()))
            else:
                new_prices.append(0)
        except:
            new_prices.append(0)

    # Creates an if statement to check for the maximum value of the new price list
    if max(new_prices) > 0:
        # Creates a for loop and updates the database list with the new prices
        for u in range(len(new_prices)):
            if new_prices[u] > 0:
                database[u+5] = new_prices[u]
        # Removes the database file and creates a new one with the updated information
        os.remove("RoomKeys/database.txt")
        open("RoomKeys/database.txt", "w").write("\n".join(str(database[v]) for v in range(len(database))))
        price_notify.grid(column=0, row=6, columnspan=2)
        return(notification.set("The prices have been updated."))
    else:
        price_notify.grid(column=0, row=6, columnspan=2)
        return(notification.set("Please change a price."))

# Defines the hotel_statistics subprogram to view the revenue and available rooms of the hotel
def hotel_statistics():
    statistics_screen.pack(expand=True)
    manager_screen.pack_forget()

    root.title("The ICS3U Hotel | Statistics")
    root.geometry("350x300")

    # Initialises the Tkinter variables
    daily_income, monthly_income = tkinter.StringVar(), tkinter.StringVar()
    daily_text = tkinter.Label(statistics_screen, textvariable=daily_income)
    monthly_text = tkinter.Label(statistics_screen, textvariable=monthly_income)
    available_single = tkinter.Label(statistics_screen, text="Available Single Bedrooms: %s" % database[0])
    available_double = tkinter.Label(statistics_screen, text="Available Double Bedrooms: %s" % database[1])
    available_executive = tkinter.Label(statistics_screen, text="Available Executive Rooms: %s" % database[2])
    available_suite = tkinter.Label(statistics_screen, text="Available President Suites: %s" % database[3])
    back_button = tkinter.ttk.Button(statistics_screen, text="Back", command=manager_dashboard)

    # Checks the database list for the monthly revenue and calculates the daily revenue to output
    if int(database[4]) > 0:
    # https://stackoverflow.com/questions/5180365/python-add-comma-into-number-string
    # Using .format to add commas in numbers for currency printing
        daily_income.set("Daily Revenue: ${:,.2f}".format(round((int(database[4])/31), 2)))
        monthly_income.set("Monthly Revenue: ${:,.2f}".format(int(database[4])))
    else:
        daily_income.set("Daily Revenue: No Revenue")
        monthly_income.set("Monthly Revenue: No Revenue")

    # Outputs all of the Tkinter information onto the screen
    daily_text.grid(column=0, row=0)
    monthly_text.grid(column=0, row=1, pady=(0,5))
    available_single.grid(column=0, row=2)
    available_double.grid(column=0, row=3)
    available_executive.grid(column=0, row=4)
    available_suite.grid(column=0, row=5)
    back_button.grid(column=0, row=6)

# Initialises the starting variables for the initial setup of the system
manager_id, initial_rooms, initial_prices = "M123", [10,10,5,2], [500,800,1500,5000]

# https://careerkarma.com/blog/python-check-if-file-exists/
# os.path to check the existence of file paths and creates them if they don't exist
if not os.path.isdir("UserIDs"):
    os.mkdir("UserIDs")
if not os.path.isdir("RoomKeys"):
    os.mkdir("RoomKeys")
if not os.path.isfile("RoomKeys/database.txt"):
    open("RoomKeys/database.txt", "w").write(("\n".join(str(initial_rooms[v]) for v in range(len(initial_rooms)))) + "\n0\n" + "\n".join(str(initial_prices[r]) for r in range(len(initial_prices))))

# Assigns tkinter.Tk() to root to use easily
root = tkinter.Tk()

# https://www.tutorialspoint.com/how-to-switch-between-two-frames-in-tkinter
# Frame swapping in Tkinter to avoid the unnecessary creation of new windows
menu_screen = tkinter.Frame(root)
login_screen = tkinter.Frame(root)
register_screen = tkinter.Frame(root)
dashboard_screen = tkinter.Frame(root)
confirmation_screen = tkinter.Frame(root)
invoice_screen = tkinter.Frame(root)
transaction_screen = tkinter.Frame(root)
manager_screen = tkinter.Frame(root)
information_screen = tkinter.Frame(root)
price_screen = tkinter.Frame(root)
statistics_screen = tkinter.Frame(root)

# Calls the menu subprogram to start the entire program
menu()

# Calls root.mainloop() to enable the GUI
root.mainloop()