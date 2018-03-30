#!/usr/bin/env python

import json
from pyntc import ntc_device as NTC

device = NTC(
    host='192.168.122.3',
    username='dilraj',
    password='dilraj',
    device_type='cisco_ios_ssh'
    )
device.open()

device.config_list(
    [
	'hostname SW1',
    'banner motd @*****WELCOME*****@',
    'int loop 1',
    'ip address 1.1.1.1 255.255.255.255'
    ]
)
print ('Configuration has been applied!')
device.close()
