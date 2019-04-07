import datetime
import time

from com.nimmetry.di.LoadListData import LoadListData

ts = time.time()

print('Script Starts at ' + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
username = input('Enter a valid username:: \n')
password = input('Enter a valid password:: \n')

loadData = LoadListData(user_name=username, password=password)

print('Script ends at ' + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
