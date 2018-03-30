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

output=device.facts

print json.dumps(output, indent=4)
device.close()
