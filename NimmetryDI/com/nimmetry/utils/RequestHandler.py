import logging

import requests

logging.basicConfig(filename="Application.log", format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.DEBUG)


class RequestHandler:

    @staticmethod
    def post_request_handler(end_point, header):
        try:
            logging.info('Enters into post_request_handler fn() ')
            logging.debug('End point url is:: ' + end_point)
            #       logging.debug('Content Body url is:: ' + header.__str__())
            user_response = requests.post(end_point, json=header)

            if user_response.status_code == 200:
                logging.info('POST /tasks/ {}'.format(user_response.status_code))
            else:
                logging.info('POST /tasks/ {}'.format(user_response.status_code))
                logging.info('Please check the given details \n' + user_response.json())

            logging.info('Exit from post_request_handler fn() ')
            return user_response

        except Exception as post_error:
            logging.exception('Error while post data to api call ' + post_error.__str__())

    @staticmethod
    def get_request_handler(end_point, header):
        try:
            logging.info('Enter into get_request_handler fn() ')
            logging.debug('EndPoint url for get method: ' + end_point)
            get_response = requests.get(end_point, headers=header)

            if get_response.status_code == 200:
                logging.info('GET /tasks/ {}'.format(get_response.status_code))
            else:
                logging.info('GET /tasks/ {}'.format(get_response.status_code))
                logging.info('Please check the given details \n' + get_response.json())

            logging.info('Exit from get_request_handler fn() ')

            return get_response

        except Exception as get_error:
            logging.exception('Error while get data from api call ', get_error.__str__())
