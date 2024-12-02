#!/usr/bin/env python3
from selenium import webdriver
from components.filter import LeftFilter
from components.base import Base
driver = webdriver.Chrome
left_filter = LeftFilter(driver)
print(left_filter.__dict__)
print(isinstance(left_filter, LeftFilter))
print(isinstance(left_filter, Base))
