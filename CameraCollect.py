# -*- coding: utf-8 -*-
"""
user:Created by jid on 2021/1/29
email:jid@hwtc.com.cn
description:
"""
import time

from PyQt5.QtCore import pyqtSignal, QObject


class CameraCollect(QObject):
    signal = pyqtSignal()

    def __init__(self):
        super(CameraCollect, self).__init__()

    def collect(self):
        time.sleep(1)
        self.signal.emit()


camera_collect: CameraCollect = CameraCollect()
