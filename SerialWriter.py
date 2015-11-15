import serial
import time
ser = serial.Serial('COM3',9600)
ser.readline()
ser.write('333')
time.sleep(2)
ser.write('666')
time.sleep(2)
ser.write('111')
    

