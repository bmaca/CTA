from xml.etree.ElementTree import parse
import urllib

u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=126')
data = u.read()
f = open('rt126.xml', 'wb')
f.write(data)
f.close()

doc = parse('rt126.xml')

latitude = 41.879875
longitude = -87.628833

for bus in doc.findall('bus'):
	lon = float(bus.findtext('lon'))
	if lon > longitude:
		direction = bus.findtext('d')
		if direction.startswith('West'):
			busid = bus.findtext('id')
			print "BudId:",busid
			print "long:", lon
