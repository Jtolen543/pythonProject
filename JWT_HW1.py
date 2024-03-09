print("Available movies today: \nA)12 Strong:   1)2:30   2)4:40   3)7:50   4)10:50")
print("B)Coco:        1)12:40  2)3:45")
print("C)The Post:    1)12:45  2)3:35   3)7:05   4)9:55")

movie_choice = input("Movie choice:  ")
showtime = input("Showtime:      ")

if movie_choice == "A":
    if showtime == "1" or showtime == "2" or showtime == "3" or showtime == "4":
        number_of_adult_tickets = int(input("Adult tickets: "))
        number_of_kid_tickets = int(input("Kid tickets:   "))
        if number_of_kid_tickets + number_of_adult_tickets <= 30:
            print(f"Total cost:    ${round(12.45*number_of_adult_tickets + 9.68*number_of_kid_tickets,2)}")
        else:
            print("Invalid option; please restart app...")
    else:
        print("Invalid option; please restart app...")
elif movie_choice == "B":
    if showtime == "1":
        number_of_adult_tickets = int(input("Adult tickets: "))
        number_of_kid_tickets = int(input("Kid tickets:   "))
        if number_of_kid_tickets + number_of_adult_tickets <= 30:
            print(f"Total cost:    ${round(11.17 * number_of_adult_tickets + 8.00 * number_of_kid_tickets,2)}")
    elif showtime == "2":
        number_of_adult_tickets = int(input("Adult tickets: "))
        number_of_kid_tickets = int(input("Kid tickets:   "))
        if number_of_kid_tickets + number_of_adult_tickets <= 30:
                print(f"Total cost:    ${round(12.45 * number_of_adult_tickets + 9.68 * number_of_kid_tickets,2)}")
        else:
                print("Invalid option; please restart app...")
    else:
            print("Invalid option; please restart app...")
elif movie_choice == "C":
    if showtime == "1":
        number_of_adult_tickets = int(input("Adult tickets: "))
        number_of_kid_tickets = int(input("Kid tickets:   "))
        if number_of_kid_tickets + number_of_adult_tickets <= 30:
            print(f"Total cost:    ${round(11.17 * number_of_adult_tickets + 8.00 * number_of_kid_tickets,2)}")
        else:
            print("Invalid option; please restart app...")
    elif showtime == "2" or showtime == "3" or showtime == "4":
        number_of_adult_tickets = int(input("Adult tickets: "))
        number_of_kid_tickets = int(input("Kid tickets:   "))
        if number_of_kid_tickets + number_of_adult_tickets <= 30:
            print(f"Total cost:    ${round(12.45 * number_of_adult_tickets + 9.68 * number_of_kid_tickets,2)}")
        else:
            print("Invalid option; please restart app...")
    else:
        print("Invalid option; please restart app...")
else:
    print("Invalid option; please restart app...")

if movie_type == "movie":
