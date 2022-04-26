#! usr/bin/env python3
# -*- coding:utf-8 -*-
import os,sys
parentdir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,parentdir)

import configparser
from config.conf import cm

HOST = 'HOST'

class ReadConfig():
    
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read(cm.ini_file,encoding='utf-8')
    
    def _get(self,section,option):
        '''获取配置'''
        return self.config.get(section,option)

    def _set(self,section,option,value):
        '''更新配置'''
        self.config.set(section,option,value)
        with open(cm.ini_file,'w') as f:
            self.config.write(f)
    @property
    def url(self):
        return self._get(HOST,HOST)
    
    @property
    def ecnew_url(self):
        return self._get('ecnewtest', 'url')
    
    @property
    def ecnew_userinfo(self):
        username = self._get('ecnewtest','username')
        password = self._get('ecnewtest','password')
        return username,password

ini = ReadConfig()

if __name__ == '__main__':
    print('url:'+ini.url)