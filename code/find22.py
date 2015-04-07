from xml.etree.ElementTree import parse
import urllib

u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()

doc = parse('rt22.xml')

latitude = 41.879875
longitude = -87.628833

for bus in doc.findall('bus'):
	lat = float(bus.findtext('lat'))
	if lat > latitude:
		direction = bus.findtext('d')
		if direction.startswith('North'):
			busid = bus.findtext('id')
			print "BudId:",busid
			print "lat:", lat
