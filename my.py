import sys
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085

sensor = Adafruit_DHT.DHT22
pin = 4
sensor2 = BMP085.BMP085()

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:

    print(' ')
    print('--------------------------------')
    print('           DHT22 Data')
    print('--------------------------------')
    print('Temp = {0:0.1f} *C\nHumidity = {1:0.1f} %'.format(temperature, humidity))
    print('--------------------------------')
    print('           BMP180 Data')
    print('--------------------------------')
    print('Temp = {0:0.2f} *C'.format(sensor2.read_temperature()))
    print('Pressure = {0:0.2f} mm Hg'.format(sensor2.read_pressure()*0.00750062))
    print('Altitude = {0:0.2f} m'.format(sensor2.read_altitude()))
    print('Sealevel Pressure = {0:0.2f} mm Hg'.format(sensor2.read_sealevel_pressure()*0.00750062))
    print('--------------------------------')
    print(' ')

else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
