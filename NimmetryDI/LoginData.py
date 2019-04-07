import requests

#Login to App , Get Inputs from Console
url = 'https://restapi.nimmetry.com/api/user/login'

print('Enter Details to access Data Integrator')
loginId = input('Enter Login userName:: \n')
loginPassword = input ('Enter Login password:: \n')


jsonData = {"user":{"loginId":loginId,"password":loginPassword}}
headers = {'Content-type': 'application/json'}

resp = requests.post(url, json=jsonData)
if resp.status_code != 201:
    print('POST /tasks/ {}'.format(resp.status_code))
tokenAccess = resp.json()["message"]["token"]

print("Successfully connected to NDI API.. ")



# Fetch list of domains

domainURL = 'https://restapi.nimmetry.com/api/domain'
accessDToken = {'x-access-token': tokenAccess}

resp1 = requests.get(domainURL,accessDToken)
if resp1.status_code != 201:
    print('GET /tasks/ {}'.format(resp1.status_code))

Domain = resp1.json()["message"]


print(resp1.json())
print(resp1.json()["success"])
print(resp1.json()["message"])
print("\n Successfully Fetched  List of domains")

loadDomain = []

loadDInput = input("Enter loadID based on Name and its index ::\n")

for entry in resp1.json()['message']:
    domainId = entry['_id']
 #   print(domainId)
    if loadDInput == domainId:
        url2 = 'https://restapi.nimmetry.com/api/load/domain/' + loadDInput
  #     print(url2)
        headers2 = {'x-access-token': tokenAccess}
        resp2 = requests.get(url2, headers=headers2)
        loadData = resp2.json()
  #     print(loadData)
        for test in resp2.json()['message']:
            name = test['name']
            sourceName = test['source']['name']
            sourceTimeStamp = test['source']['createdTimestamp']
            targetName = test['target']['name']
            targetTimeStamp = test['target']['createdTimestamp']
            print(name+' :: '+sourceName+':: '+sourceTimeStamp)
            print(name + ' :: ' + targetName + ':: ' + targetTimeStamp)





print('End of program')