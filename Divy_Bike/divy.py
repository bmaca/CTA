import requests
import json
from datetime import datetime
import sys
import logging

url = 'http://www.divvybikes.com/stations/json'
response = requests.get(url)
json_object = response.json()

time_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print "-" * 20
print "DATE        TIME"
print time_date
print "-" * 20

# handle error handling if user doesnt pass in an argument
if len(sys.argv) != 2:
    logging.error("Must provide a street address as an argument in order for the program to work")
    sys.exit(1)

station_address = sys.argv[1]

def station_info(station_address):
    if json_object['stationBeanList'] == []:
        print 'I am sorry there is no data.'
    else:
        for data in json_object['stationBeanList']:
            if data['stAddress1'] == station_address:
                print ('Street Address: {0}'.format(data['stAddress1']))
                print ('Total Docks: {0}'.format(data['totalDocks']))
                print ('Available Docks: {0}'.format(data['availableDocks']))
                print ('Available Bikes: {0}'.format( data['availableBikes']))
                print ('In Service: {0}'.format( data['statusValue']))
            else:
                pass

                
if __name__ == '__main__':
    print "-" * 20
    station_info(station_address)
    print "-" * 20
logger = logging.getLogger(__name__)
