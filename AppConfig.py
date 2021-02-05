# -*- coding: utf-8 -*-
"""
user:Created by jid on 2021/1/29
email:jid@hwtc.com.cn
description:
"""
import os


class AppConfig:

    def __init__(self):
        super(AppConfig, self).__init__()
        self.work_folder = '%s\\ForceIC_CameraCollect' % os.path.expanduser('~')
        self.exception_folder = '%s\\exception' % self.work_folder
        self.config_folder = '%s\\config' % self.work_folder
        self.measure_log = '%s\\measure' % self.config_folder

    def load_global_config(self):
        if not os.path.exists(self.work_folder):
            os.makedirs(self.work_folder)
        if not os.path.exists(self.exception_folder):
            os.makedirs(self.exception_folder)
        if not os.path.exists(self.config_folder):
            os.makedirs(self.config_folder)


app_config: AppConfig = AppConfig()
