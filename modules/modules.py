import serial
import sys

ser = serial.Serial(sys.argv[1], 9600)
ser.open()
ser.write(b'Message sent using pySerial')
ser.close()