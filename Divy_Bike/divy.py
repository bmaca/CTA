import requests
import json

url = 'http://www.divvybikes.com/stations/json'
response = requests.get(url)
json_object = response.json()

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
                continue



fetch_bikes_sprout()
print '--------------'
fetch_bikes_train()
