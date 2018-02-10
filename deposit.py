import requests
import json

customerId = "5882f8101756fc834d8eb69d"
apiKey = "89aa70192f549a177bab372469a7c78a"
accountId = "5a7f0c516514d52c7774b106"

url = "http://api.reimaginebanking.com/accounts/{}/deposits?key={}".format(accountId, apiKey)

header = {"Content-Type": "application/json"}
payload = {"key": apiKey}
body = {
        "medium": "balance",
        "transaction_date": "2018-02-10",
        "status": "pending",
        "description": "Deposit from coin robot!",
        "amount": 0.25
       }

def found_coin():
	r = requests.post(url, headers=header, data=json.dumps(body)).json()
	if(r["code"] == 201):
		print("Coin successfully deposited in your account!")