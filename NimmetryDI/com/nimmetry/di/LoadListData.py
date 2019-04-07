import requests


class LoadListData:

    def __init__(self, user_name, password):
        try:
            print('Enters into init Fn().. ')
            self.user_name = user_name
            self.password = password
            print('Initializing rest_call fn().. with ' + user_name + ' : ' + password)
            self.result = LoadListData.rest_call(user_name=user_name, password=password)
            print('Completes rest_call function')
            print('Exit from init fn().. ')
        except Exception as init_error:
            print(init_error)

    '''
    Method to get connected to API, fetch Domain and load data
    @param user_name
    @param password
    @return
    '''

    @staticmethod
    def rest_call(user_name, password):
        return_value = False
        try:
            # Trying to login into API with Credentials
            print("Initiating the Rest Call Function.. ")
            url = 'https://restapi.nimmetry.com/api/user/login'
            login_user_data = {"user": {"loginId": user_name, "password": password}}

            resp = requests.post(url, json=login_user_data)
            if resp.status_code != 201:
                print('POST /tasks/ {}'.format(resp.status_code))
            else:
                print('Please check URL/username/password')
            access_token = resp.json()["message"]["token"]

            # Domains List
            print('Trying to fetch list of domains in api')
            domain_url = 'https://restapi.nimmetry.com/api/domain'
            access_domain_token = {'x-access-token': access_token}
            resp1 = requests.get(domain_url, access_domain_token)
            if resp1.status_code != 201:
                print('GET /tasks/ {}'.format(resp1.status_code))
            else:
                print('Please check token and login details to fetch domains list')

            print("\n Successfully Fetched  List of domains")

            # load from domain list by fetching the list
            domain_list_dict = {}
            for entry in resp1.json()['message']:
                domain_id = entry['_id']
                domain_name = entry['name']
                domain_list_dict[domain_id] = domain_name

            # Equating with user choice and list given to get load data
            print("list of domains:: \n")
            print(domain_list_dict)
            load_domain_input = input("Enter Id from above list  ::\n")
            for entry in resp1.json()['message']:
                domain_id_1 = entry['_id']
                if load_domain_input == domain_id_1:

                    load_domain_url = 'https://restapi.nimmetry.com/api/load/domain/' + load_domain_input
                    headers2 = {'x-access-token': access_token}
                    load_response = requests.get(load_domain_url, headers=headers2)

                    for test in load_response.json()['message']:
                        name = test['name']
                        source_name = test['source']['name']
                        src_timestamp = test['source']['createdTimestamp']
                        target_name = test['target']['name']
                        target_timestamp = test['target']['createdTimestamp']
                        print(
                            'Load Name :: ' + name + ' Source Name :: ' + source_name + ' Source TimeStamp :: ' + src_timestamp + ' Target:: ' + target_name + ' target ts:: ' + target_timestamp)
                    print('Fetched Data...')

            return_value = True
        except Exception as rest_call_error:
            print(rest_call_error)
            return_value = False

        return return_value
