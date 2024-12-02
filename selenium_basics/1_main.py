#!/usr/bin/env python3
from selenium import webdriver
from components.base import Base

driver = webdriver.Chrome
base = Base(driver)
print(base.__dict__)
print(type(base))
