# -*- coding: utf-8 -*-
"""
user:Created by jid on 2020/12/29
email:jid@hwtc.com.cn
description:
"""
import cgitb
import logging
import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from AppConfig import app_config
from view.view_control.MainWindow import MainWindow

if __name__ == '__main__':
    logging_format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=logging_format)
    app_config.load_global_config()
    # 当程序发生异常时,将异常信息以html的格式保存到指定文件夹中
    log_dir = app_config.exception_folder
    logging.debug(log_dir)
    # sys.excepthook = cgitb.Hook(display=0, logdir=log_dir, context=10, format='html')
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('image/icon_HWTC.ico'))
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
