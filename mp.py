import sys
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085
import httplib, urllib

sensor = Adafruit_DHT.DHT22
pin = 4
sensor2 = BMP085.BMP085()

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:

    print(' ')
    print('--------------------------------')
    print('           DHT22 Data')
    print('--------------------------------')
    print('Temp = {0:0.2f} *C\nHumidity = {1:0.2f} %'.format(temperature, humidity))
    print('--------------------------------')
    print('           BMP180 Data')
    print('--------------------------------')
    print('Temp = {0:0.2f} *C'.format(sensor2.read_temperature()))
    print('Pressure = {0:0.2f} mm Hg'.format(sensor2.read_pressure()*0.00750062))
    print('Altitude = {0:0.2f} m'.format(sensor2.read_altitude()))
    print('Sealevel Pressure = {0:0.2f} mm Hg'.format(sensor2.read_sealevel_pressure()*0.00750062))
    print('--------------------------------')
    print(' ')

    params = urllib.urlencode({
        'v': 1,
        'tid': 'UA-88068717-1',
        'cid': '666',
        't': 'event',
        'ec': 'sensors',
        'ea': 'living room',
#       'el': round(sensor2.read_pressure()*0.00750062,2),
        'cm1': round(temperature,2),
        'cm2': round(humidity,2),
        'cm3': round(sensor2.read_pressure()*0.00750062,2)
    })

    connection = httplib.HTTPConnection('www.google-analytics.com')
    connection.request('POST', '/collect', params)


else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
