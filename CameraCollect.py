# -*- coding: utf-8 -*-
"""
user:Created by jid on 2021/1/29
email:jid@hwtc.com.cn
description:
"""
import logging
import time

from PyQt5.QtCore import pyqtSignal, QObject

from SerialComm import SerialComm


class CameraCollect(QObject):
    signal = pyqtSignal()

    def __init__(self):
        super(CameraCollect, self).__init__()
        self.serial_comm = None

    def init_camera(self, com_port):
        self.serial_comm = SerialComm(com_port, 115200)
        self.serial_comm.set_xyLv_mode()

    def measure(self, show_count):
        time.sleep(0.1)
        self.serial_comm: SerialComm
        if self.serial_comm is not None:
            measure_data = self.serial_comm.measure()
            logging.info(str(show_count) + '---' + str(measure_data))
            self.signal.emit()
