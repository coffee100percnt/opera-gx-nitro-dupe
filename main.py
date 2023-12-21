import requests
import json
from uuid import uuid4

url = "https://api.discord.gx.games/v1/direct-fulfillment"

with open("proms.txt", "a") as file:
    for i in range(0, int(input("how many? "))):    
        data = {"partnerUserId": str(uuid4())}
        x = requests.post(url, json=data)
        file.write(f'https://discord.com/billing/partner-promotions/1180231712274387115/{json.loads(x.text)["token"]}\n')
