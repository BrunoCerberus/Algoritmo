#!/usr/bin/python3.4
'''
Created on Apr 28, 2015

@author: bruno
'''

import time

def printHeader(title):
    print("""Content-type: text/html
    
    <?xml version = "1.0" encoding = "UTF-8"?>
    <!DOCTYPE html PUBLIC
        "-//w3c//DTD XHTML 1.0 Strict//EN"
        "DTD/xhtml1-sctrict.dtd">
    <html xmlns = "http://www.w3.org/1999/xhtml">
    <head><title>%s</title></head>
    
    <body>""" % title)
    
    printHeader("Current date and time")
    print(time.ctime(time.time()))
    print("</body></html>")
