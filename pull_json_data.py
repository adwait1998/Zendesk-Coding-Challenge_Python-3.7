import json
import requests
import os
import time


class GetJSONData:

    # Constructor defining MAX_PER_PAGE and Params
    def __init__(self):
        self.MAX_PER_PAGE = 25
        self.params = {"per_page": self.MAX_PER_PAGE, "page": 1}

    # Helper Function for max_value_per_page
    def get_max_per_page(self):
        return self.MAX_PER_PAGE

    # Helper Function for getting params
    def get_params(self):
        return self.params

    def Get_Data(self):
        # Reads Credentials from credentials.json file for authentication
        with open("credentials.json", 'r') as f:
            # Saving details in a variable
            store_data = json.load(f)
            # Using JSON data in store_data to hit the API
            url = "https://" + store_data[
                "subdomain"] + ".zendesk.com/api/v2/tickets.json"
            response = requests.get(url, params=self.params, auth=(
                store_data["email"], store_data["password"]))

            #Calling CheckResponse() to check if data is received
            data = self.CheckResponse(response)
        return data

    def GetSingleTicket(self, id):
        # Reads Credentials from credentials.json file for authentication
        with open("credentials.json", 'r') as f:

            # Saving details in a variable
            store_data = json.load(f)

            # Using JSON data in store_data to hit the API
            # Using "id" to fetch a single ticket.
            url = "https://" + store_data[
                "subdomain"] + ".zendesk.com/api/v2/tickets/" + id + ".json"
            response = requests.get(url, auth=(
                store_data["email"], store_data["password"]))
            data = self.CheckResponse(response)
        return data

    def CheckResponse(self, response):
        # If response code is 200 then data is received using the credentials.
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
        else:
            print("\nRequest failed. Please try again. \n")
            time.sleep(2)
