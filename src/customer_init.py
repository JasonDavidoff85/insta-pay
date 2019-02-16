import requests
import json
apiKey = '5d40f2852229ce9f706e44f3ed93dad1'

# Terry Initialization:
url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)

payload = {
	"first_name":"Terry",
	"last_name":"Keffer",
	"address":{
		"street_number":"West Egg",
		"street_name":"Drillfield Drive",
		"city":"Blacksburg",
		"state":"VA",
		"zip":"24061",
		}
}

response = requests.post(
	url,
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)


response=requests.get(url)
terryId=(response.json()[3]["_id"])

url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(
terryId,apiKey)

payload = {
	"type":"Checking",
	"nickname":"checky",
	"rewards":0,
	"balance":2000,
}

response = requests.post(
	url,
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(
terryId,apiKey)

payload = {
	"type":"Credit Card",
	"nickname":"cardy",
	"rewards":0,
	"balance":150,
}

response = requests.post(
	url,
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

# Derek Initialization
url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)

payload = {
	"first_name":"Derek",
	"last_name":"Bruce",
	"address":{
		"street_number":"West Egg",
		"street_name":"Drillfield Drive",
		"city":"Blacksburg",
		"state":"VA",
		"zip":"24061",
		}
}

response = requests.post(
	url,
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)


url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)

response=requests.get(url)
derekId=(response.json()[4]["_id"])


url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(
derekId,apiKey)

payload = {
	"type":"Checking",
	"nickname":"dchecky",
	"rewards":0,
	"balance":4200,
}

response = requests.post(
	url,
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(
derekId,apiKey)

payload = {
	"type":"Checking",
	"nickname":"dchecky2",
	"rewards":0,
	"balance":300,
}

response = requests.post(
	url,
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)


url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(
derekId,apiKey)

payload = {
	"type":"Credit Card",
	"nickname":"dcardy",
	"rewards":0,
	"balance":650,
}

response = requests.post(
	url,
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)





