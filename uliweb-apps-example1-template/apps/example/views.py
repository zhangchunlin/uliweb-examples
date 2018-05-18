#coding=utf-8
from uliweb import expose, functions

@expose('/')
def home_example():
    return {}

@expose('/layout0')
def layout0_example():
    return {}

@expose('/layout1')
def layout1_example():
    return {}

@expose('/layout2')
def layout2_example():
    return {}

@expose('/1column')
def one_column_example():
    return {}

@expose('/1column_fluid')
def one_column_fluid_example():
    return {}

@expose('/2column_sidebar')
def two_column_sidebar_example():
    return {}

@expose('/full_column')
def full_column_example():
    return {}
