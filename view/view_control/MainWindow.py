# -*- coding: utf-8 -*-
"""
user:Created by jid on 2021/1/29
email:jid@hwtc.com.cn
description:
"""
import logging
import os
import sched
import threading
import time

from PyQt5.QtWidgets import QMainWindow
from serial.tools import list_ports

from CameraCollect import CameraCollect
from view.ui.MainFrame import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.start_btn.clicked.connect(self.start_collect)
        self.prev_btn.clicked.connect(self.show_prev_pattern)
        self.next_btn.clicked.connect(self.show_next_pattern)
        serial_list = self.scan_serial_list()
        self.camera_collect = CameraCollect()
        self.camera_collect.signal.connect(self.show_next_pattern)
        self.show_count = 0
        self.scheduler = sched.scheduler(time.time)
        self.comm_cb.addItems(serial_list.values())
        self.connect_btn.clicked.connect(self.init_camera)

    def init_camera(self):
        self.scheduler.enter(0, 1, self.connect)
        thread = threading.Thread(target=self.scheduler.run)
        thread.setDaemon(True)
        thread.start()

    def connect(self):
        self.camera_collect.init_camera(self.comm_cb.currentText())

    @staticmethod
    def scan_serial_list():
        plist = list_ports.comports()
        serial_list = {}
        for port in plist:
            if port.serial_number is not None:
                serial_list.update({port.serial_number: port.device})
            else:
                serial_list.update({port.device: port.device})
        return serial_list

    def start_collect(self):
        """
        调用相机采集模块采集当前Pattern数据,采集完成后切换到下一个Pattern再采集,直到将所有Pattern数据采集完
        """
        self.show_count = 0
        self.scheduler.enter(1, 1, self.measure)
        thread = threading.Thread(target=self.scheduler.run)
        thread.setDaemon(True)
        thread.start()

    def measure(self):
        self.camera_collect.measure(self.show_count)

    def show_prev_pattern(self):
        os.popen('adb shell am broadcast -a cn.com.hwtc.forceic_whitebalance_debug.prev')

    def show_next_pattern(self):
        logging.debug('show_next_pattern %d' % self.show_count)
        os.popen('adb shell am broadcast -a cn.com.hwtc.forceic_whitebalance_debug.next')
        if self.show_count < 26:
            self.show_count += 1
            # self.camera_collect.measure(self.show_count)
            self.scheduler.enter(1, 1, self.measure)
            thread = threading.Thread(target=self.scheduler.run)
            thread.setDaemon(True)
            thread.start()
