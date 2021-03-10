# -*- coding: utf-8 -*-
"""
user:Created by jid on 2020/4/15
email:jid@hwtc.com.cn
description:
"""
import logging
import os
import re
import shutil
import time
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler


def logging_write(path, filename, formatter, level=logging.INFO):
    if not os.path.exists(path):
        os.makedirs(path)

    # 创建一个logger
    logger = logging.getLogger()
    logger.setLevel(level)

    # 创建一个handler，用于写入日志文件
    # fh = logging.FileHandler(path + filename, encoding='utf-8')
    # fh.setLevel(level)

    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # 定义handler的输出格式
    formatter = logging.Formatter(formatter)
    # fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 创建TimedRotatingFileHandler对象
    log_file_handler = TimedRotatingFileHandler(filename=path + filename, when="H", interval=1, backupCount=168,
                                                encoding='utf-8')
    # log_file_handler.suffix = "%Y-%m-%d.txt"
    log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)

    # 给logger添加handler
    # logger.addHandler(fh)
    logger.addHandler(ch)
    logger.addHandler(log_file_handler)


def delete_folder_by_date(folder, days, formatter):
    logging.debug('delete_folder_by_date -> %s' % folder)
    if os.path.exists(folder):
        dirs = os.listdir(folder)
        current_time_stamp = get_time_stamp('%s' % datetime.now().strftime(formatter))
        logging.debug('delete_folder_by_date current_time_stamp-> %s' % current_time_stamp)
        for inner_folder in dirs:
            time_stamp = get_time_stamp(inner_folder)
            logging.debug('delete_folder_by_date time_stamp-> %s' % time_stamp)
            if current_time_stamp - time_stamp > 86400 * days:
                shutil.rmtree(os.path.join(folder, inner_folder))


def delete_folder_by_count(folder, counts):
    logging.debug('delete_folder_by_count -> %s' % folder)
    if os.path.exists(folder):
        files = os.listdir(folder)
        files.reverse()
        logging.debug('delete_folder_by_count -> %s' % files)
        if len(files) > counts:
            del_files = files[counts:]
            for file in del_files:
                path = os.path.join(folder, file)
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)


def get_time_stamp(date):
    time_array = time.strptime(date, "%Y-%m-%d")
    time_stamp = int(time.mktime(time_array))
    return time_stamp
