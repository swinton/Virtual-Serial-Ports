#!/usr/bin/env python

import serial

ser = serial.Serial("/dev/ttys006")

ser.write("hello world\n")

ser.close()