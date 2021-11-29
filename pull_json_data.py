import json
import requests
import os
import time


class GetJSONData:
    def __init__(self):
        self.MAX_PER_PAGE = 25
        self.params = {"per_page": self.MAX_PER_PAGE, "page": 1}

    def get_max_per_page(self):
        return self.MAX_PER_PAGE

    def get_params(self):
        return self.params

    def Get_Data(self):
        with open("credentials.json", 'r') as f:
            store_data = json.load(f)
            url = "https://"+store_data[
                "subdomain"]+".zendesk.com/api/v2/tickets.json"
            response = requests.get(url, params=self.params, auth=(
                store_data["email"], store_data["password"]))
            data = self.CheckResponse(response)
        return data

    def GetSingleTicket(self, id):
        with open("credentials.json", 'r') as f:

            store_data = json.load(f)

            url = "https://"+store_data[
                "subdomain"]+".zendesk.com/api/v2/tickets/"+id+".json"
            response = requests.get(url, auth=(
                store_data["email"], store_data["password"]))
            data = self.CheckResponse(response)
        return data

    def CheckResponse(self, response):

        if response.status_code == 200:
            data = json.loads(response.text)
            return data
        else:
            print("\nRequest failed. Please try again. \n")
            time.sleep(2)
