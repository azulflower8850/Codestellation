import serial
import time
ser = serial.Serial('COM3',9600)
ser.readline()
ser.write('750')

    

