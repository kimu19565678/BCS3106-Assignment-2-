from pip._vendor.distlib.compat import raw_input


def print_menu():  ## Your menu design here
    print(30 * "-", "MENU", 30 * "-")
    print("1. Add Orders")
    print("2. Schedule Orders")
    print("3. Cancel Order")
    print("4. Print Receipt")
    print("5. Exit")

list = [{'Order 1','Order2'}, ('Order3'), ['Order4', 'Order5']]
print_menu()
choice = int(input("Please choose an action "))
loop = True

while loop:  ## While loop which will keep going until loop = False
    ## Displays menu


    if choice == 1:
        print("Menu 1 has been selected")


    elif choice == 2:
        print("Menu 2 has been selected")

    elif choice == 3:
        print("Choose Order to cancel")
        print('List:', list)
        list.clear()
        print('Order sucsesfully dropped')

    elif choice == 4:
        print("Menu 4 has been selected")

    elif choice == 5:
        print("Menu 5 has been selected")

        loop = False  # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")
