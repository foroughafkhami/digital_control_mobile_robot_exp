import serial import getch
serialport = serial.Serial ("/dev/ttyS0")
serialport.baudrate = 115200
while(True):     x = getch.getch()      if  x=='w':         command = "+100+10015+00"
    elif (x=='s'):         command = "-100-10015+00"
    elif (x=='a'):
        command = "-100+10015+00"
    elif (x=='d'):
        command = "+100-10015+00"
    elif (x=='q'):
        break
    else:
        command = "+000+00015+00"
    serialport.write(command.encode())
