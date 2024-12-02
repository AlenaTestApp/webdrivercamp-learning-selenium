#!/usr/bin/env python3
from components.base import Base
from selenium import webdriver
driver = webdriver.Chrome()

base = Base(driver)
print(base.__dict__)
print(type(base))
