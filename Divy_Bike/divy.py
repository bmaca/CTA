import requests
import json
from datetime import datetime


url = 'http://www.divvybikes.com/stations/json'
response = requests.get(url)
json_object = response.json()

time_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print time_date

print '----------------'

def fetch_bikes_sprout():
    if json_object['stationBeanList'] == []:
        print 'I am sorry there is no data'
    else:
        for data in json_object['stationBeanList']:
            if data['id'] == 37:
                print ('Street Address: {0}' .format(data['stAddress1']))
                print ('Total Docks: {0}'.format(data['totalDocks']))
                print ('Available Docks: {0}'.format(data['availableDocks']))
                print ('Available Bikes: {0}'.format( data['availableBikes']))
                print ('In Service: {0}' .format( data['statusValue']))
                continue

def fetch_bikes_train():
    if json_object['stationBeanList'] == []:
        print 'I am sorry there is no data.'
    else:
        for data in json_object['stationBeanList']:
            if data['id'] == 192:
                print ('Street Address: {0}' .format(data['stAddress1']))
                print ('Total Docks: {0}'.format(data['totalDocks']))
                print ('Available Docks: {0}'.format(data['availableDocks']))
                print ('Available Bikes: {0}'.format( data['availableBikes']))
                print ('In Service: {0}' .format( data['statusValue']))
                continue

def fetch_another_closer_route():
    if json_object['stationBeanList'] == []:
        print 'I am sorry there is no data.'
    else:
        for data in json_object['stationBeanList']:
            if data['id'] == 49:
                print ('Street Address: {0}' .format(data['stAddress1']))
                print ('Total Docks: {0}'.format(data['totalDocks']))
                print ('Available Docks: {0}'.format(data['availableDocks']))
                print ('Available Bikes: {0}'.format( data['availableBikes']))
                print ('In Service: {0}' .format( data['statusValue']))
                continue


fetch_bikes_sprout()
print '--------------'
fetch_bikes_train()
print '--------------'
fetch_another_closer_route()
