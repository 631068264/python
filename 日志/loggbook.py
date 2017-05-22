#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2017/4/11 21:50
@annotation = ''
"""
import sys

import logbook
from logbook import Logger, StreamHandler

StreamHandler(sys.stdout).push_application()
# logbook.set_datetime_format("local")

# patch warn
logbook.base._level_names[logbook.base.WARNING] = 'WARN'
log = Logger('My Awesome Logger')
log.warn('This is too cool for stdlib')
