#! /usr/bin/python

# Import and init an XBee device
from xbee import XBee,ZigBee
import serial

#ser = serial.Serial('COM3', 9600)

# Use an XBee 802.15.4 device
# To use with an XBee ZigBee device, replace with:
#xbee = ZigBee(ser)
#xbee = XBee(ser)

xbee.remote_at(
    dest_addr_long='\x00\x00\x00\x00\x00\x00\xFF\xFF',
    dest_addr='\xFF\xFE',
    command='D1',
    parameter='\x05')

xbee.remote_at(
    dest_addr_long='\x00\x00\x00\x00\x00\x00\xFF\xFF',
    dest_addr='\xFF\xFE',
    command='WR')

ser.close()
