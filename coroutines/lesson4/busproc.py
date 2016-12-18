# busproc.py
#
# Bus processor.  This runs as a subprocess from the coprocess.py example

import sys

from coroutines.lesson3.buses import *
from coroutines.lesson4.coprocess import recvfrom

recvfrom(sys.stdin,
         filter_on_field("route","22",
         filter_on_field("direction","North Bound",
         bus_locations())))
