import requests
import json
from datetime import datetime


url = 'http://www.divvybikes.com/stations/json'
response = requests.get(url)
json_object = response.json()

time_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print "-" * 20
print "DATE        TIME"
print time_date
print "-" * 20

def station_info(station_id):
    if json_object['stationBeanList'] == []:
        print 'I am sorry there is no data.'
    else:
        for data in json_object['stationBeanList']:
            if data['id'] == station_id:
                print ('Street Address: {0}'.format(data['stAddress1']))
                print ('Total Docks: {0}'.format(data['totalDocks']))
                print ('Available Docks: {0}'.format(data['availableDocks']))
                print ('Available Bikes: {0}'.format( data['availableBikes']))
                print ('In Service: {0}'.format( data['statusValue']))

                
if __name__ == '__main__':
    print "-" * 20
    station_info(37)
    print "-" * 20
    station_info(192)
    print "-" * 20
    station_info(49)

    
    