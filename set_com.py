import serial
from serial.tools import list_ports


def grep_com(grep='2341:0043'):
    ports = list(list_ports.grep(grep))
    assert len(ports) == 1, f'more than 1 port matching {grep}'
    port = ports[0]
    return port.device


def set_com(high=False, port=None, timeout=1, dtr=False):
    com = serial.Serial()
    com.port = grep_com() if port is None else port
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
