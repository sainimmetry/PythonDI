import datetime
import logging
import sys
import time


from com.nimmetry.di.LoadListData import LoadListData

logging.getLogger(__name__).addHandler(logging.NullHandler())


logging.basicConfig(filename="Application.log", format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.DEBUG)

ts = time.time()

logging.info('Script Starts at ' + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
api_url = input('Enter a valid url (Hint:: <http|s>://<url>/api) :: \n')
username = input('Enter a valid username(Hint:foo) \n')
password = input('Enter a valid password(Hint: boo) \n')

send_details = input('Are you sure to proceed (yes/no)? (yes) ::\n')
if send_details.lower() == 'yes':
    loadData = LoadListData(user_name=username, password=password, api_url=api_url)
else:
    print('Please enter valid details')
    sys.exit()

logging.info('Script ends at ' + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
