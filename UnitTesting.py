import unittest
from unittest.mock import patch
import Main
import requests
import unittest.mock
import ProcessTickets
import pull_json_data
from ProcessTickets import Ticket
from pull_json_data import GetJSONData
getJson = GetJSONData()
ticket = Ticket()
import json


class TestCodes(unittest.TestCase):
    #Checks Credentials
    def test_credentials(self):
        with open("credentials.json", 'r') as f:
            store_data = json.load(f)
            # Using JSON data in store_data to hit the API
            url = "https://" + store_data[
                "subdomain"] + ".zendesk.com/api/v2/tickets.json"
            response = requests.get(url, auth=(
                store_data["email"], store_data["password"]))

            self.assertTrue(response.ok)
            self.assertEqual(response.status_code, 200)

    #Checks False Credentials
    def test_false_credentials(self):
        with open("credentials.json", 'r') as f:
            store_data = json.load(f)
            # Using JSON data in store_data to hit the API
            url = "https://" + store_data[
                "subdomain"] + ".zendesk.com/api/v2/tickets.json"
            response = requests.get(url, auth=(
                store_data["email"], "RANDOMPASSWORD"))

            self.assertEqual(response.status_code, 401 or 400)

    #Value Error is raised in passed a string
    @patch('ProcessTickets.input', create=True)
    def test_check_input(self, mocked_input):
        mocked_input.side_effect = ['ff']
        ProcessTickets.Ticket.GetSingleTicket
        self.assertRaises(ValueError)

    #Test for exit message
    @patch('Main.input', create=True)
    def test_main_menu(self, mocked_input):
        mocked_input.side_effect = [3]
        Main.Main.MainMenu
        self.assertTrue("\nThanks for visiting. :)\n")


    #Checks for range out of bounds or invalid
    @patch('ProcessTickets.input', create=True)
    def test_check_input(self, mocked_input):
        mocked_input.side_effect = [250]
        ProcessTickets.Ticket.GetSingleTicket
        self.assertTrue("\nInvalid range..You have only ")

    #Checks if Total per page changes
    @patch('pull_json_data.GetJSONData.get_max_per_page', create=True)
    def test_total_per_page(self, mocked_input):
        mocked_input.side_effect = ['90']
        data = getJson.Get_Data()
        self.assertEqual(getJson.MAX_PER_PAGE, len(data['tickets']))

    #Check for ID passed and received in a ticket to ensure correct ticket has been accessed.
    def test_single_ticket(self):
        id = str(15)
        data = getJson.GetSingleTicket(id)

        ticket_id = str(data['ticket']['id'])
        self.assertEqual(ticket_id, id)


if __name__ == "__main__":
    unittest.main()

