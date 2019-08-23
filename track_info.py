"""
Package tracking Function.
# -*- coding:utf-8 -*-
# Copyright (c) 2018-present, Makiras
"""
import random
import string
import time

from selenium import webdriver

firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument('--headless')
# firefox_options.add_argument('--disable-gpu')


class TrackInfo:

    def __init__(self):
        super(TrackInfo).__init__()
        self.webdriver = webdriver.Firefox(firefox_options=firefox_options, executable_path='./geckodriver'
                                           , service_log_path='/dev/null')
        self.webdriver.get("https://baidu.com")  # Keep Browse alive
        random.seed(time.time())

    def query_package(self, package_num: string, sf_phone: string = None) -> (string, []):
        """
        May throw error, remember catch it.
        :param: package_num , the number of package
        :param: sf_phone, the last 4 number of sender's phone or receiver's phone number
        :return: type: [[string, string, string], ] information: [[date, time, info], ]
        """
        self.webdriver.delete_all_cookies()
        self.webdriver.get("https://m.kuaidi100.com/result.jsp?nu=" + package_num)
        if sf_phone is not None and len(sf_phone) is 4:
            try:
                check_dialog = self.webdriver.find_element_by_class_name("check-dialog")
                input_wrap = check_dialog.find_element_by_class_name("input-wrap").find_element_by_xpath("./input[1]")
                input_wrap.send_keys(sf_phone)
                check_dialog.find_element_by_class_name("btn").click()
            except:
                print("[WARN]: MAY NOT BE SHUNFENG OR HAS BEEN CACHED")
        time.sleep(1)
        try:
            self.webdriver.find_element_by_class_name("more-text").click()
        except:
            print("[WARN]: NO EXPAND NEED OR HAS BEEN CACHED")
        result_list = self.webdriver.find_element_by_class_name("result-list")
        time.sleep(1)
        if len(result_list.text) is 0:
            print("[WARN]: NO INFO FOUND")
            return package_num, []
        else:
            raw_text = result_list.text.split('\n')
            package_info = []
            for ith in range(0, len(raw_text), 3):
                package_info.append(raw_text[ith:ith + 3])
            return package_num, package_info

    def query_packages(self, packages_query_list: [[string, string]]):
        """
        :param packages_query_list: [[package_num, phone_num], ]
        :return: [(package_num, package_info), ]
        """
        packages_info = []
        for package_query in packages_query_list:
            package_info = self.query_package(package_query[0], package_query[1])
            packages_info.append(package_info)
        return packages_info

    def __del__(self):
        self.webdriver.quit()


if __name__ == "__main__":
    tracker = TrackInfo()
    # just show usage, cannot run
    print(tracker.query_packages([["3653214123428", "0888"], ["3653214441328", ""]]))
    print(tracker.query_package("3632141234328", "0888"))
