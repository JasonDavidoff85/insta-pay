import requests
import json
import sys

# All things that will remain constant
apiKey = '5d40f2852229ce9f706e44f3ed93dad1'

# This finds what number the input name is assigned to in the API (order of creation)
# This is used in other constants
user = sys.argv[1]
def getNumber(user):
    urlyy = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)
    response = requests.get(urlyy)
    morf = 0
    c = 0

    while (morf == 0):
	client = response.json()[c]["first_name"]
        if (user == client):
                morf = 1
                return c
                    
        c = c + 1


identifier = int(getNumber(user))

url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)
response=requests.get(url)
userId=(response.json()[identifier]["_id"])

# METHODS ----------------------------------------------------------------------------


# This method returns a first and last name from just a first name
def find_full_name(identifier):
	url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)
	response=requests.get(url)
	firstName=(response.json()[identifier]["first_name"])
	lastName=(response.json()[identifier]["last_name"])
	fullName= firstName + " " + lastName
	return(fullName)


# This method gets the last four digits of the user ID
def lastFourDigits(identifier):
	url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)

	response=requests.get(url)

	userId=(response.json()[identifier]["_id"])
	fourId = userId[-4:]
	return(fourId)


# This method determines what account numbers are related to a type of account
# ie., what number(0-2) accounts are Checking
def find_account_type(Type):
	# Useable "Type"'s are (Checking, Credit Card)
	url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(
	userId,apiKey)
	response=requests.get(url)
	i = 0
	# varone and two are not set as 0 because 0 is a meaningful output
	varone = -1
	vartwo = -1
	while (i<3):
		account_type = (response.json()[i]["type"])
		if (account_type == Type):
			if (varone==-1):
				varone = i
			else:			
				vartwo = i
		if (account_type == "Credit Card"):
			i = 4
		else:
			i = i + 1

	if (vartwo == -1):
		vartwo == None
	return(varone,vartwo)



# This method checks the balance of all accounts as mentioned in find_account_type
def get_checking_balance(Type):
	# Useable "Type"'s are (Checking, Credit Card)
	url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(
	userId,apiKey)
	response=requests.get(url)
	i = 0
	# varone and two are not set as 0 because 0 is a meaningful output
	varone = -1
	vartwo = -1
	while (i<3):
		account_type = (response.json()[i]["type"])
		if (account_type == Type):
			if (varone==-1):
				varone = i
			else:			
				vartwo = i
		if (account_type == "Credit Card"):
			i = 4
		else:
			i = i + 1
	url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(
	userId,apiKey)
	response=requests.get(url)
	if (vartwo==-1):
		checkbalone = (response.json()[varone]["balance"])
		checkbaltwo = None
	else:
		checkbalone = (response.json()[varone]["balance"])
		checkbaltwo = (response.json()[vartwo]["balance"])
	return(checkbalone,checkbaltwo)

# This method returns the account numbers of Type specified
def find_account_number(Type):
	# Useable "Type"'s are (Checking, Credit Card)
	url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(
	userId,apiKey)
	response=requests.get(url)
	i = 0
	# varone and two are not set as 0 because 0 is a meaningful output
	varone = -1
	vartwo = -1
	while (i<3):
		account_type = (response.json()[i]["type"])
		if (account_type == Type):
			if (varone==-1):
				varone = i
			else:			
				vartwo = i
		if (account_type == "Credit Card"):
			i = 4
		else:
			i = i + 1


	oneId = (response.json()[varone]["_id"])
	twoId = (response.json()[vartwo]["_id"])
	if (vartwo == -1):
		twoId = None
	return(oneId,twoId)


# This finds the last four digits of any accounts
def lastFourAccount(Type):
	# Useable "Type"'s are (Checking, Credit Card)
	url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(
	userId,apiKey)
	response=requests.get(url)
	i = 0
	# varone and two are not set as 0 because 0 is a meaningful output
	varone = -1
	vartwo = -1
	while (i<3):
		account_type = (response.json()[i]["type"])
		if (account_type == Type):
			if (varone==-1):
				varone = i
			else:			
				vartwo = i
		if (account_type == "Credit Card"):
			i = 4
		else:
			i = i + 1


	oneId = (response.json()[varone]["_id"])
	twoId = (response.json()[vartwo]["_id"])
	oneIdfour = oneId[-4:]
	twoIdfour = twoId[-4:]
	if (vartwo == -1):
		twoIdfour = None
	return(oneIdfour,twoIdfour)



Type = "Checking"
print(find_full_name(identifier))
print(lastFourDigits(identifier))
print(find_account_type(Type))
print(get_checking_balance(Type))
print(find_account_number(Type))
print(lastFourAccount(Type))



