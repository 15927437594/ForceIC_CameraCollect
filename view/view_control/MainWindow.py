# -*- coding: utf-8 -*-
"""
user:Created by jid on 2021/1/29
email:jid@hwtc.com.cn
description:
"""
import logging
import os

from PyQt5.QtWidgets import QMainWindow

from CameraCollect import camera_collect
from view.ui.MainFrame import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.start_btn.clicked.connect(self.start_collect)
        self.prev_btn.clicked.connect(self.show_prev_pattern)
        self.next_btn.clicked.connect(self.show_next_pattern)
        camera_collect.signal.connect(self.show_next_pattern)
        self.show_count = 0

    def start_collect(self):
        """
        调用相机采集模块采集当前Pattern数据,采集完成后切换到下一个Pattern再采集,直到将所有Pattern数据采集完
        """
        self.show_next_pattern()

    def show_prev_pattern(self):
        os.popen('adb shell am broadcast -a cn.com.hwtc.forceic_whitebalance_debug.prev')

    def show_next_pattern(self):
        os.popen('adb shell am broadcast -a cn.com.hwtc.forceic_whitebalance_debug.next')
        camera_collect.collect()
        self.show_count += 1
        logging.debug('camera_collect=%d' % self.show_count)
