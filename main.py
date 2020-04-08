# standard libraries
from datetime import datetime
import time
import os
import sys


# sensor related libraries
#import busio
#import adafruit_bme680
#import board
import bme680

def main():

    # read from the sensors BME680
    log_name = datetime.now().strftime('%Y-%m-%d_%H-%M.txt')
    data_labels = 'Timestamp,Temperature,Gas,Humidity,Pressure'
    print('The log name is:', log_name)

    os.system('mkdir data')

    with open('./data/{}'.format(log_name), 'a') as log:
        log.write(data_labels)
        log.write('\n')
    
    try:
        #i2c = busio.I2C(board.SCL, board.SDA)
        sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
    except Exception as e:
        print(e)
        print('Could not configure the sensor. Exiting...')
        exit(1)

    
    while True:
        #timestamp = datetime.now()
        timestamp = round(time.mktime(datetime.now().timetuple()))

        print()
        print(timestamp)
        
        # read data
        try:
            sensor.get_sensor_data()
            print('Temperature: {} degrees C'.format(sensor.data.temperature))
            print('Gas: {} ohms'.format(sensor.data.gas_resistance))
            print('Humidity: {}%'.format(sensor.data.humidity))
            print('Pressure: {}hPa'.format(sensor.data.pressure))
        except:
            print('Bad data')
        
        try:
            t = str(round(sensor.data.temperature))
        except:
            t = 'None'
        try:
            g = str(round(sensor.data.gas_resistance))
        except:
            g = 'None'
        try:
            h = str(round(sensor.data.humidity))
        except:
            h = 'None'
        try:
            p = str(round(sensor.data.pressure))
        except:
            p = 'None'

        # write to the log
        with open('./data/{}'.format(log_name), 'a') as log:
            log.write(str(timestamp) + ',' + t + ',' + g + ',' + h + ',' + p + '\n')
        print('sleeping 1s')
        time.sleep(1)


if __name__ == '__main__':
    main()
    #sys.exit(main(sys.argv))

