#Jellybean Republic Delivery

while True:
    print("Welcome to Jellybean Republic Delivery Services!\n")

    weight = float(input("What is the weight of your package in grams? "))
    print('''Here are some modes of transportation that are available:
    A. Hot Air Balloon - 1000.00 Jellies for the first 500g + 1.50 Jellies for every gram in excess
    B. Submarine - 5000.00 Jellies for the first 500g + 5.00 Jellies for every gram in excess\n''')

    mode = input("What mode of transportation would you like to use? ").upper()

    if (mode == 'A'):
        if (weight <= 500):
            cost = 1000.00

        else:
            a = weight - 500
            cost = 1000.00 + (a * 1.50)

    elif (mode == 'B'):
        if (weight <= 500):
            cost = 5000.00

        else:
            a = weight - 500
            cost = 5000.00 + (a * 5.00)

    print("The delivery cost is " + str(cost) + " Jellies")

    answer = input("Would you like to send another package? (y/n): ").upper()

    if (answer == 'Y'):
        pass

    elif (answer == 'N'):
        break

    else:
        print("Error!")
