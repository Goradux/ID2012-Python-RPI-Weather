#!/usr/bin/env python
# -*- coding: utf-8 -*-


# standard libraries
from datetime import datetime
import time


# sensor related libraries
import busio
import adafruit_bme680
import board


def main():
    
    # read from the sensors BME680
    log_name = datetime.now().strftime('%Y-%m-%d_%H-%M.txt')
    data_labels = 'Timestamp,'
    print('The log name is:', log_name)
    with open('./data/{}'.format(log_name), 'a') as log:
        log.write(data_labels)
        log.write('\n')
    
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)
    except Exception as e:
        print(e)
        print('Could not configure the sensor. Exiting...')
        exit(1)

    
    while True:
        timestamp = datetime.now()
        
        print()
        print(timestamp)
        
        # read data
        try:
            print('Temperature: {} degrees C'.format(sensor.temperature))
            print('Gas: {} ohms'.format(sensor.gas))
            print('Humidity: {}%'.format(sensor.humidity))
            print('Pressure: {}hPa'.format(sensor.pressure))
        except:
            print('Bad data')
        
        try:
            t = str(round(sensor.temperature))
        except:
            t = 'None'
        try:
            g = str(round(sensor.gas)))
        except:
            g = 'None'
        try:
            h = str(round(sensor.humidity))
        except:
            h = 'None'
        try:
            p = str(round(sensor.pressure))
        except:
            p = 'None'

        # write to the log
        with open('./data/{}'.format(log_name), 'a') as log:
            log.write(str(timestamp) + ',' + t + ',' + g + ',' + h + ',' + p + '\n')
        print('sleeping 5s')
        time.sleep(5)


if __name__ == '__main__':
    import sys
    main()
    #sys.exit(main(sys.argv))

