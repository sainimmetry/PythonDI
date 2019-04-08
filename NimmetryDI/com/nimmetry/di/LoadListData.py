import logging

from com.nimmetry.utils.RequestHandler import RequestHandler

logging.basicConfig(filename="Application.log", format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)

logging.basicConfig(filename="Application.log", format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.ERROR)


class LoadListData:

    def __init__(self, user_name, password, api_url):
        try:
            logging.info('Enters into init Fn().. ')
            self.user_name = user_name
            self.password = password
            self.api_url = api_url
            logging.info(' Initializing rest_call fn().. ')
            self.result = LoadListData.user_login(user_name=user_name, password=password, api_url=api_url)
            logging.info('Completes rest_call function')
            logging.info('Exit from init fn().. ')
        except Exception as init_error:
            logging.error('Error ' + init_error.__str__())
        else:
            logging.info('Successfully completed init Fn() ')

    '''
    Method to get connected to API, fetch Domain and load data
    @param user_name
    @param password
    @return
    '''

    @staticmethod
    def user_login(user_name, password, api_url):

        try:
            # Trying to login into API with User Credentials
            logging.info('Trying to login into API with User Credentials')
            login_url = api_url + '/user/login'
            logging.info("Initiating the Rest Call Function with url " + login_url)
            login_user_data = {"user": {"loginId": user_name, "password": password}}
            # Call Post method from Request handler
            logging.info('Call Post method from Request handler')
            request_handler = RequestHandler()
            user_response = request_handler.post_request_handler(end_point=login_url, header=login_user_data)
            access_token = user_response.json()["message"]["token"]

            # Calling domain list and load
            LoadListData.domain_list_data(api_url=api_url, access_token=access_token, request_object=request_handler)
            return_value = True
        except Exception as rest_call_error:
            print('Error While calling ' + rest_call_error.__str__())
            return_value = False

        return return_value

    @staticmethod
    def domain_list_data(api_url, access_token, request_object):
        try:
            # Domains List
            logging.info('Trying to fetch list of domains in api')
            domain_url = api_url + '/domain'
            access_domain_token = {'x-access-token': access_token}
            logging.info("Initiating the Rest Call Function with url " + domain_url)
            resp1 = request_object.get_request_handler(end_point=domain_url, header=access_domain_token)
            logging.info("\n Successfully Fetched  List of domains")

            # load from domain list by fetching the list
            logging.info('load from domain list by fetching the list ')
            domain_list_dict = {}
            for entry in resp1.json()['message']:
                domain_id = entry['_id']
                domain_name = entry['name']
                domain_list_dict[domain_id] = domain_name

            # Equating with user choice and list given to get load data
            print("list of domains:: \n" + domain_list_dict.__str__())
            user_load_domain_input = input("Enter Id from above list  ::\n")
            for entry in resp1.json()['message']:
                domain_id_1 = entry['_id']
                if user_load_domain_input == domain_id_1:
                    # load data from selected domain
                    logging.info('load data from selected domain')
                    LoadListData.load_data(api_url=api_url, load_domain_input=user_load_domain_input,
                                           request_object=request_object, access_token=access_token)

        except Exception as data_error:
            print(data_error)

    @staticmethod
    def load_data(api_url, load_domain_input, request_object, access_token):
        try:
            logging.info('Enters into load_data fn()')
            load_domain_url = api_url + '/load/domain/' + load_domain_input
            logging.info('load data domain url :' + load_domain_url)
            load_data_header = {'x-access-token': access_token}
            logging.info('Enters into Get Request Handler...::')
            load_response = request_object.get_request_handler(end_point=load_domain_url,
                                                               header=load_data_header)

            for test in load_response.json()['message']:
                name = test['name']
                source_name = test['source']['name']
                src_timestamp = test['source']['createdTimestamp']
                target_name = test['target']['name']
                target_timestamp = test['target']['createdTimestamp']
                print(
                    'Load Name :: ' + name + ' Source Name :: ' + source_name + ' Source TimeStamp :: '
                    + src_timestamp + ' Target:: ' + target_name + ' target ts:: ' + target_timestamp)

        except Exception as load_data_error:
            logging.error('Error while fetching load data ' + load_data_error.__str__(), load_data_error)
