#!/usr/bin/python

from xbee import XBee, ZigBee
import serial
import time
import sqlite3

def get_temperature(data):

    item = data['samples']

    temperature = ((item[0].get('adc-0')*1.2/1023)-0.5)*100
    print temperature

    #if format=="F":
        #convert to farenheit
        #tempature = (tempature * 1.8) + 32
    conn=sqlite3.connect('../../data-dev.sqlite3')

    curs=conn.cursor()
    curs.execute("INSERT INTO tempdata (temperature, date) VALUES (?, ?)", (temperature,int(time.time())))
    print "cla"
    # commit the changes
    conn.commit()


#   ----------------------------------------

PORT = 'COM3'
BAUD_RATE = 9600

ser = serial.Serial(PORT, BAUD_RATE)

xbee = ZigBee(ser, callback=get_temperature)

# Do other stuff in the main thread
while True:
    try:
        conn = sqlite3.connect('../../data-dev.sqlite3')
        #time_range = int(time.time()) - (60*60*24.0) #grab the last 24 hours
        cur = conn.cursor()
        cur.execute("SELECT * FROM command")

        rows = cur.fetchall()
        print rows[0][1]

        if rows[0][1]=="none":
            print "spento"
        elif rows[0][1]=="open":
            print "acceso"
            cur.execute("UPDATE command SET command='none' WHERE Id=1")
            conn.commit()



        time.sleep(.1)
    except KeyboardInterrupt:
        break

xbee.halt()
ser.close()
