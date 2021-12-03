import os
import time
import sys
# imports datetime to reformat the created data received from json
from datetime import datetime
from pull_json_data import GetJSONData
import textwrap

getJson = GetJSONData()  # Creating an instance GetJSONData Class.


class Ticket:
    # Function for displaying column names with formatting while displaying tickets
    def Header(self):
        print("Ticket Id", 2 * " ", "Subject",
              41 * " ", "Created at", 10 * " ", "Assigned by", 6 * " ", "Status")
        print(150 * "_")
        print("\n")

    # Function for displaying Description
    def HeaderDescription(self):
        print("Description")
        print(30 * "_")
        print("\n")

    # Function for getting all Tickets
    #
    def GetAllTickets(self):
        while True:
            # Using the instance created I hit the API using Get_Data() module
            # Further I extract fields like tickets, next_page and previous page
            data = getJson.Get_Data()
            tickets = data['tickets']
            next_page = data['next_page']
            prev_page = data['previous_page']
            os.system('cls')

            print(9 * "-")
            self.Header()
            # Calling the PrintTickets function

            self.PrintTickets(tickets, getJson.params['page'])

            print("\n\nOPTIONS\n")
            print("1) Enter 1 to view next page ")
            print("2) Enter 2 to view previous page")
            print("3) Return Home (Enter 3)")
            print("\nEnter q to Quit ")

            selection = input("\nEnter your choice: ")
            if selection == "1":
                if next_page is None:
                    os.system('cls')
                    print('No more pages left :( ')
                else:
                    os.system('cls')
                    print("loading...")
                    getJson.params['page'] += 1

            elif selection == "2":
                if prev_page is None:
                    os.system('cls')
                    print('You are already in the first page :)')
                else:
                    os.system('cls')
                    print("loading..")
                    getJson.params['page'] -= 1

            elif selection == "3":
                os.system('cls')
                print("Returning to Home Page....")

                break
            elif selection == "q":
                print("\nThanks You :) :)\n")
                sys.exit()

            else:
                print(
                    "\nInvalid selection :O  !!  Please enter \"1,2,3\" or \"q\""
                )

    def GetSingleTicket(self):
        #Here I again hit the API using Get_Data() for taking a total count.
        data = getJson.Get_Data()
        data_length = data['count']

        while True:

            while True:
                print("\nPlease Enter the Ticket ID\n ")
                TicketID = input('Enter Ticket ID: ')
                try:
                    val = int(TicketID)
                except ValueError:
                    print("\nPlease enter NUMBER only\n")
                    time.sleep(1)
                    os.system('cls')
                    continue
                if 1 <= val <= data_length:
                    break
                else:
                    print(
                        "\nInvalid range. You have only " + str(data_length) +
                        " Tickets...\n")
                    time.sleep(1)
                    os.system('cls')

            os.system('cls')

            #Here I call GetSingleTicket module to get a single ticket if the ID entered is in range.
            data = getJson.GetSingleTicket(TicketID)
            ticket = data['ticket']
            if ticket is not None:
                self.Header()
                self.DisplayAllTickets(ticket)
            else:
                print("\nCould not retrieve the ticket!!! Please try again")
            end = 0
            while True:
                print("\n" + 5 * "-", "Search again" + 5 * "-" + "\n")
                print("1. Enter 1 to Search Again ")
                print("2. Enter 2 to Return to Home Page ")
                print("3. Enter 3 to view Description")
                print("\nEnter q to Quit")

                selection = input("\nEnter your choice: ")
                if selection == "1":
                    os.system('cls')
                    break

                elif selection == "2":
                    os.system('cls')
                    print("Returning to Main Menu ")
                    end = -1
                    break

                elif selection == "3":
                    os.system('cls')
                    print("Displaying Description")
                    self.HeaderDescription()
                    self.DisplayDescription(ticket)
                    continue
                elif selection == "q":
                    print("\nThanks for visiting. :)\n")
                    sys.exit()
                else:
                    print(
                        """\nInvalid selection. Returning to home page""")
                    end = -1
                    break
            if end == -1:
                break
            else:
                continue

    #Function definition fot PrintTickets()
    def PrintTickets(self, tickets, page):
        count = page * getJson.MAX_PER_PAGE
        for ticket in tickets:
            self.DisplayAllTickets(ticket)
            count += 1
        return

    # Function definition fot DisplayAllTickets()
    def DisplayAllTickets(self, ticket):
        ticketId = ticket["id"]
        assigned_by = str(ticket['assignee_id'])
        subject = ticket['subject']
        status = ticket['status']

        created_at = str(datetime.strptime(
            ticket['created_at'], '%Y-%m-%dT%H:%M:%SZ'))
        string = "{:{fill}{align}{width}}"

        print(string.format(
            ticketId, fill='', align='<', width=11) + string.format(
            subject, fill='', align='<', width=45) + string.format(
            created_at, fill='', align='<', width=28) +
              string.format(
                  assigned_by, fill='', align='<', width=18) + string.format(status, fill='', align='<', width=18))

    # Function definition for DisplayDescription()
    def DisplayDescription(self, ticket):
        description = ticket['description']
        string = "{:{fill}{align}{width}}"
        print(string.format(textwrap.fill(description, 50), fill='', align=':<', width=18))
