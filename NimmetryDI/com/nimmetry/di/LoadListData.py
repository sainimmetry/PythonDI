import logging

from com.nimmetry.utils.Constants import USER_API, LOAD_DOMAIN_DATA, DOMAIN_LIST
from com.nimmetry.utils.RequestHandler import RequestHandler

logging.basicConfig(filename="Application.log", format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.DEBUG)


class LoadListData:

    def __init__(self, user_name, password, api_url):
        try:
            logging.debug('Enters into init Fn().. ')
            self.user_name = user_name
            self.password = password
            self.api_url = api_url
            logging.debug('Exit from init fn().. ')
        except Exception as init_error:
            logging.exception('Error while Initialing  ' + init_error.__str__())
        else:
            logging.debug('Successfully completed init Fn() ')

    '''
    Method to get connected to API, fetch Domain and load data
    @param user_name
    @param password
    @return
    '''

    def user_login(self):
        try:
            # Trying to login into API with User Credentials
            logging.debug('Trying to login into API with User Credentials')
            login_url = self.api_url + USER_API
            logging.debug("Initiating the Rest Call Function with url " + login_url)
            login_user_data = {"user": {"loginId": self.user_name, "password": self.password}}
            # Call Post method from Request handler
            logging.debug('Calling Post method from Request handler')
            request_handler = RequestHandler()
            user_response = request_handler.post_request_handler(end_point=login_url, header=login_user_data)
            self.access_token = user_response.json()["message"]["token"]
            return self.access_token

        except Exception as rest_call_error:
            logging.exception('Error While calling ' + rest_call_error.__str__())
            return self.access_token

    def domain_list_data(self, request_object):
        try:
            #  Get Domains List
            logging.info('Trying to fetch list of domains in api')
            domain_url = self.api_url + DOMAIN_LIST
            logging.debug("Initiating the Rest Call Function with url " + domain_url)
            resp1 = request_object.get_request_handler(end_point=domain_url, header=self.access_token)
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
                self.domain_id_1 = entry['_id']
                if user_load_domain_input == self.domain_id_1:
                    # load data from selected domain
                    logging.info('loading data from selected domain')

                    #   LoadListData.load_data(api_url=self.api_url, load_domain_input=user_load_domain_input,
                    #                         request_object=request_object, access_token=self.access_token)
                    logging.info('Completed and exit from domain_list_data fn() ')
                    return self.domain_id_1

        except Exception as data_error:
            return self.domain_id_1
            logging.exception('Data Error while processing ' + data_error.__str__())

    def load_data(self, request_object):
        try:
            logging.debug('Enters into load_data fn()')
            load_domain_url = self.api_url + LOAD_DOMAIN_DATA + self.domain_id_1
            logging.debug('Enters into Get Request Handler...::' + load_domain_url)
            load_response = request_object.get_request_handler(end_point=load_domain_url,
                                                               header=self.access_token)
            logging.debug('load data from domain response ::' + load_response.__str__())
            for test in load_response.json()['message']:
                name = test['name']
                source_name = test['source']['name']
                src_timestamp = test['source']['createdTimestamp']
                target_name = test['target']['name']
                target_timestamp = test['target']['createdTimestamp']
                print(
                    'Load Name :: ' + name + ' Source Name :: ' + source_name + ' Source TimeStamp :: '
                    + src_timestamp + ' Target:: ' + target_name + ' target ts:: ' + target_timestamp)

            logging.info('data load completed for user specified domain list')
            return 'Completed'

        except Exception as load_data_error:
            logging.exception('Error while fetching load data ' + load_data_error.__str__())
            return 'Failed'

    '''
    @self
    @main
    This method is used to user login API, Get Domain List, get data load from Domain
    '''
    def main(self):
        try:
            logging.debug('Enter into Main() Fn')
            logging.info('Process flow initiated ')
            logging.debug('Entered into main fn().. ')
            request_handler = RequestHandler()

            access_token = self.user_login()
            if access_token is not None:
                domain_id = self.domain_list_data(request_handler)
            else:
                logging.info('Please check the Web API Call ')

            if domain_id is not None:
                run_status = self.load_data(request_handler)
            else:
                logging.info('Please check log for further details.. ')

            if run_status == 'Completed':
                print('Process Completed Successfully ')
                logging.info('Process Completed Successfully ')
            else:
                print('Error in loading data')
                logging.info('Error in loading data')

        except Exception as Main_Error:
            logging.execption('Error While Executing Main Fn \n' + Main_Error.__str__())
