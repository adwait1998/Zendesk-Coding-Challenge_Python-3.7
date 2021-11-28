import json
import requests
import os
import time


class GetJSONData:

    def Get_Data(self):
        with open("credentials.json", 'r') as f:
            store_data = json.load(f)
            url = "https://"+store_data[
                "subdomain"]+".zendesk.com/api/v2/tickets.json"
            response = requests.get(url, params=None, auth=(
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
