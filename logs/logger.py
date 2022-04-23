#! usr/bin/env python3
# -*- coding:utf-8 -*-
import os,sys
parentdir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,parentdir)

import logging
from config.conf import cm

class Log:
    def __init__(self):
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)

            #创建一个handle写入文件
            fh = logging.FileHandler(cm.log_file, encoding='utf-8')
            fh.setLevel(logging.INFO)

            #创建一个handle输出控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            #定义输入格式
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            #添加到hanler
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

            #关闭通道
            self.logger.removeHandler(fh)
            self.logger.removeHandler(ch)
    @property
    def fmt(self):
        return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'

log = Log().logger

if __name__ == '__main__':
    log.info('hello word!')
    log.removeHandler()