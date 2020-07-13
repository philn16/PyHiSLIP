#!/usr/bin/env python
from pyhislip import HiSLIP

scope=HiSLIP()
scope.connect('192.168.168.156')
print(scope.ask("*IDN?"))
