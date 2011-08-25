#!/usr/bin/env python

import serial

ser = serial.Serial("/dev/ttys005")

line = ser.readline()
print line

ser.close()