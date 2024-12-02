#!/usr/bin/env python3
from selenium import webdriver
from components.filter import LeftFilter
driver = webdriver.Chrome
left_filter = LeftFilter(driver)
left_filter.select_option("I know OOP")
