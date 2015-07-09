import requests
from datetime import datetime

DESIRED_STATIONS = [
    37,
    192,
    49
]

url = 'http://www.divvybikes.com/stations/json'

bar = "-"*20
barline = "\n{bar}\n".format(**vars())

DATE_TITLE = "DATE"
TIME_TITLE = "TIME"
title = """
{bar}
{DATE_TITLE:<12}{TIME_TITLE:<11}
{date:<12}{time:<11}
{bar}
""".strip()

data_output = """
Street Address:  {stAddress1}
Total Docks:     {totalDocks}
Available Docks: {availableDocks}
Available Bikes: {availableBikes}
In Service:      {statusValue}
""".strip()

output = """
{formatted_title}
{formatted_data}
{bar}
""".strip()

def station_info(station_id):
    if json_object['stationBeanList'] == []:
        print 'I am sorry there is no data.'
        return
    requested_station_results = filter(lambda s: s["id"] == station_id, json_object['stationBeanList'])
    if not requested_station_results:
        print "Station {id} not found".format(id=station_id)
    return data_output.format(**requested_station_results[0])

if __name__ == '__main__':
    date = datetime.now().strftime('%Y-%m-%d')
    time = datetime.now().strftime('%H:%M:%S')

    response = requests.get(url)
    json_object = response.json()

    formatted_title = title.format(**vars())
    formatted_data = barline.join(map(station_info,DESIRED_STATIONS))
    print output.format(**vars())