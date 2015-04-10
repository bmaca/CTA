from xml.etree.ElementTree import parse
import urllib
import time

u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=126')
data = u.read()
f = open('rt126.xml', 'wb')
f.write(data)
f.close()

doc = parse('rt126.xml')

latitude = 41.879875
longitude = -87.628833

def monitor_bus():
	for bus in doc.findall('bus'):
		lon = float(bus.findtext('lon'))
		if lon > longitude:
			direction = bus.findtext('d')
			if direction.startswith('West'):
				busid = bus.findtext('id')
			print "BudId:",busid
			print "long:", lon

print '*' *10

#added 8 for the typical 8 hour work day. 
stop = 8
		
while stop >0:
	monitor_bus()
	time.sleep(60)

	stop = stop -1
