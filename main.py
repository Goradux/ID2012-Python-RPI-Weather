#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2020  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import busio
import adafruit_bme680
import time
import board

from datetime import datetime


# read from the sensors BME680
log_name = datetime.now().strftime('%Y-%m-%d_%H-%M.txt')
data_labels = 'Timestamp,'
print('The log name is:', log_name)
with open('./data/{}'.format(log_name), 'a') as log:
    log.write(data_labels)
    log.write('\n')


def main_loop():
    while True:
        timestamp = datetime.now()
        print('executing')
        # read data
        

        # write to the log
        with open('./data/{}'.format(log_name), 'a') as log:
            log.write(str(timestamp))
            log.write('\n')
        print('sleeping 5s...')
        time.sleep(5)


if __name__ == '__main__':
    import sys
    main_loop()
    #sys.exit(main(sys.argv))

