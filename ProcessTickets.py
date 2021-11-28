import os
import time
import sys
# imports datetime to reformat the created data received from json
from datetime import datetime
from pull_json_data import GetJSONData

getJson = GetJSONData()


class Ticket:
    def Header(self):
        print("Ticket Id", 2 * " ", "Subject",
              41 * " ", "Created at", 10 * " ", "Assigned by", 6 * " ", "Status")
        print(150 * "_")
        print("\n")

    def GetAllTickets(self):
        while True:
            data = getJson.Get_Data()
            tickets = data['tickets']
            os.system('cls')

            print(9 * "-")
            self.Header()
            self.PrintTickets(tickets)
            break



    def PrintTickets(self, tickets):
        count = 0
        for ticket in tickets:
            self.DisplayAllTickets(ticket)
            count += 1
        return

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
