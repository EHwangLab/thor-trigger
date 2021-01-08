import serial


def set_com(high=False, port='COM7', timeout=1, dtr=False):
    com = serial.Serial()
    com.port = port
    # com.baudrate = 9600
    com.timeout = timeout
    com.setDTR(dtr)
    com.open()
    # print(com)
    if high:
        com.write(b'HIGH\n')
    else:
        com.write(b'LOW\n')
    com.close()


if __name__ == '__main__':

    set_com(True)
