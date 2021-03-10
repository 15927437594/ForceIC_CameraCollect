import serial


class SerialComm(object):
    def __init__(self, port, baud_rate):
        super(SerialComm).__init__()
        self.port = port
        self.baud_rate = baud_rate
        self.ser = serial.Serial(self.port, self.baud_rate, timeout=1)

    def get_ser_status(self):
        return self.ser.is_open

    def write_to_ser(self, cmd):
        self.ser.write(cmd)

    def read_from_ser(self):
        line = self.ser.readlines()
        return line

    def set_xyLv_mode(self):
        cmd = b'STR,0\r'
        self.write_to_ser(cmd)
        ret = self.read_from_ser()
        cmd = b'MDS,0\r'
        self.write_to_ser(cmd)
        ret = self.read_from_ser()

    def measure(self):
        cmd = b'MES,0\r'
        self.write_to_ser(cmd)

        ret = self.read_from_ser()
        ret = ret[0]
        str = ret.decode('utf-8')
        # print(str)
        str = str.split(' ')
        str = str[1][0:-1]
        str = str.split(';')
        x = float(str[0]) / 10000
        y = float(str[1]) / 10000
        Lv = float(str[2])
        return x, y, Lv

    def close_serial(self):
        self.ser.close()
