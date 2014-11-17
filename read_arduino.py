#!/usr/bin/python

import os
import httplib
import serial
import re
import json

ser = serial.Serial('/dev/ttyACM0', 4800)

headers = {"Content-type": "application/json",
           "Accept": "application/json"}
r_unwanted = re.compile("[\n\r]")

while 1 :
    msg = ser.readline()
    body = json.dumps({"data": msg, "is_ax25": False})
    body = r_unwanted.sub("", body)
    print body

    conn = httplib.HTTPConnection(os.environ['APRS_DASHBOARD_HOST'], os.environ['APRS_DASHBOARD_PORT'])
    conn.request("PUT", "/api/v1/message", body, headers)
    resp = conn.getresponse()
    print(resp.status, resp.reason)


