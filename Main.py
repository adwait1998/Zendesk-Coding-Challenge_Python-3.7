#!/usr/bin/env python3

# install pip3 install requests


from ProcessTickets import Ticket
import os
import time


class Main():
    def display_menu(self):
        os.system('cls')
        print("")
        print("Mobile Ticket viewer")
        print("Select an option from below:\n")
        print("1) List all the tickets ")
        print("2) List a single ticket ")
        print("Enter q to quit \n")

    def MainMenu(self):
        os.system('cls')

        while True:
            self.display_menu()
            choice = input("Enter 1 to display all tickets")
            if choice == "1":
                os.system('cls')
                tickets.GetAllTickets()
            elif choice == "2":
                os.system('cls')
                tickets.GetSingleTicket()
            elif choice == "q":
                print("\nThank you :) )\n")
                break


if __name__ == '__main__':
    tickets = Ticket()
    object = Main()
    object.MainMenu()
