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


class TestCodes(unittest.TestCase):

    def CredentialsCheck(self):
        response = requests.get(
            "https://zccadwaitpatil.zendesk.com/api/v2/tickets.json", auth=(
                "adwait1234@gmail.com", "e7?jJTK#9aMEa3M"))
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)

    def FalseCredentialsCheck(self):

        response = requests.get(
            "https://zccadwaitpatil.zendesk.com/api/v2/tickets.json", auth=(
                "adwait1234@gmail.com", "Random Password"))

        self.assertEqual(response.status_code, 401 or 400)

    @patch('ProcessTickets.input', create=True)
    def TestInput(self, mocked_input):
        mocked_input.side_effect = ['ff']
        ProcessTickets.Ticket.GetSingleTicket
        self.assertRaises(ValueError)

    @patch('ProcessTickets.input', create=True)
    def TestInput(self, mocked_input):
        mocked_input.side_effect = [250]
        ProcessTickets.Ticket.GetSingleTicket
        self.assertTrue("\nInvalid range..You have only ")

    @patch('Main.input', create=True)
    def TestMainMenu(self, mocked_input):
        mocked_input.side_effect = [3]
        Main.Main.MainMenu
        self.assertTrue("\nThanks for visiting. :)\n")


    @patch('pull_json_data.GetJSONData.get_max_per_page', create=True)
    def TestMaxEntriesPerPage(self, mocked_input):
        mocked_input.side_effect = ['90']
        data = getJson.Get_Data()
        self.assertEqual(getJson.MAX_PER_PAGE, len(data['tickets']))


    def TestSingleTickets(self):
        id = str(15)
        data = getJson.GetSingleTicket(id)

        ticket_id = str(data['ticket']['id'])
        self.assertEqual(ticket_id, id)


if __name__ == "__main__":
    unittest.main()

