#!/usr/bin/env python

from pyntc import ntc_device as NTC

device = NTC(
    host='192.168.122.3',
    username='dilraj',
    password='dilraj',
    device_type='cisco_ios_ssh'
    )
device.open()

run = device.running_config
print (run)
device.close()
