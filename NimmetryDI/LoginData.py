import requests

#Login to App , Get Inputs from Console
url = input('Enter REST EndPoint URL to login : ')

loginId = input('Enter userName:: ')
loginPassword = input ('Enter login password:: ')


jsonData = {"user":{"loginId":loginId,"password":loginPassword}}
headers = {'Content-type': 'application/json'}

resp = requests.post(url, json=jsonData)
if resp.status_code != 201:
    print('POST /tasks/ {}'.format(resp.status_code))
tokenAccess = resp.json()["message"]["token"]

print("Successfully connected to NDI API.. ")



# Fetch list of domains

url1 = input('Enter EndPoint URL to fetch Domains List:: ')
headers1 = {'x-access-token': tokenAccess}

resp1 = requests.get(url1,headers1)
if resp1.status_code != 201:
    print('GET /tasks/ {}'.format(resp1.status_code))

print(resp1.json())
print("\n Successfully Fetched  List of domains")

#domainId = resp1.json()['message']['_id']

#print('Domain Id is: '+domainId)

url2 = input('Enter load list from domain ::')


headers2 = {'x-access-token': tokenAccess}
resp2 = requests.get(url2,headers=headers2)

loadData = resp2.json()
print(loadData)
print("succesfully fetched list of data...")



