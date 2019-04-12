import logging

from com.nimmetry.di.LoadListData import LoadListData

logging.basicConfig(filename="Application.log", format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.DEBUG)

logging.getLogger(__name__).addHandler(logging.NullHandler())

logging.info('Script Execution Starts  ')
api_url = input('Enter a valid url (Hint:: <http|s>://<url>/api) :: \n')
username = input('Enter a valid username(Hint:foo) \n')
password = input('Enter a valid password(Hint: boo) \n')

send_details = input('Are you sure to proceed (yes/no)? (yes) ::\n')
if send_details.lower() == 'yes':
    loadData = LoadListData(user_name=username, password=password, api_url=api_url)
    loadData.main()

else:
    print('Please re-run and enter valid details')

logging.info('Script Execution ends')
