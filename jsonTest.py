import urllib2
import json
import string

def getInfo():
    info = urllib2.urlopen('http://198.211.113.33:3000/printers')
    str_info = ''
    for line in info:
        str_info += line
    return str_info

printerDict = dict()

def name(msg):
    start = msg.find('-')
    if start == -1:
        return "name error"
    else:
        return msg[start+2:]

def status(msg):
    if msg == "go.gif":
        status = "available"
    elif msg == "yield.gif":
        status = "warning"
    elif msg == "stop.gif":
        status = "not working"
    else:
        status = "unknown"
    return status

class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

    def dict_to_object(self, d):
        if 'name' in d and 'icon' in d:
            printer_name = name(d.pop('name'))
            printer_status = status(d.pop('icon'))
            printerDict[printer_name] = printer_status

encoded_object = getInfo()
myobj_instance = MyDecoder().decode(encoded_object)
for printer in printerDict:
    print printer, printerDict[printer]
