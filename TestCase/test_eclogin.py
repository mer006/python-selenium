#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
from unittest import result
import pytest
from utils.logger import log
from common.readconfig import ini
from page_object.ecloginpage import ECloginPage


class TestECLogin:
    '''打开EC'''
    @pytest.fixture(scope='function',autouse=True)
    def test_openEC(self, drivers):
        eclogin = ECloginPage(drivers)
        eclogin.get_url(ini.ecnew_url)

    def test_001(self, drivers):
        eclogin = ECloginPage(drivers)
        eclogin.input_username_password(ini.ecnew_userinfo[0],ini.ecnew_userinfo[1])
        eclogin.login_click()
        result = re.search(r'1606', eclogin.get_source)
        #result = eclogin.get_source
        log.info(result)
        assert result
