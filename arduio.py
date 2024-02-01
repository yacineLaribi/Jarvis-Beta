import serial
import time 
arduino_serial = serial.Serial('COM10', 9600)
time.sleep(2)
arduino_serial.write('1'.encode())
time.sleep(2)
arduino_serial.close()

        
