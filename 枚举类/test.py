#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2017/4/11 18:23
@annotation = ''
"""
from enum import Enum


# class CustomEnum(Enum):
#     def __repr__(self):
#         return "%s.%s" % (
#             self.__class__.__name__, self._name_)
#
#
# # noinspection PyPep8Naming
class EXECUTION_PHASE(Enum):
    GLOBAL = "[全局]"
    ON_INIT = "[程序初始化]"
    BEFORE_TRADING = "[日内交易前]"
    ON_BAR = "[盘中 handle_bar 函数]"
    ON_TICK = "[盘中 handle_tick 函数]"
    AFTER_TRADING = "[日内交易后]"
    FINALIZED = "[程序结束]"
    SCHEDULED = "[scheduler函数内]"


# e = EXECUTION_PHASE.GLOBAL
# print EXECUTION_PHASE.__members__["GLOBAL"].value
# print EXECUTION_PHASE.GLOBAL.name
# print EXECUTION_PHASE.GLOBAL
# print EXECUTION_PHASE.__members__["GLOBAL"] == EXECUTION_PHASE.GLOBAL
#
# print EXECUTION_PHASE.__members__
# for name, member in EXECUTION_PHASE.__members__.items():
#     print name, '=>', member, ',', member.value
#
# print [member.value for _, member in EXECUTION_PHASE.__members__.items()]
# print [e.value for e in EXECUTION_PHASE]


def enum_all_values(enum_class):
    return [e.value for e in enum_class]


def _enum_to_str(v):
    return v.name


def str_to_enum(enum_class, s):
    return enum_class.__members__[s]


class MINUTE(Enum):
    ONE_MINUTE = 1
    THREE_MINUTE = 3
    FIVE_MINUTE = 5
    QUARTER_HOUR = 15
    HALF_HOUR = 30
    HOUR = 60
    TWO_HOUR = 120
    FOUR_HOUR = 240
    SIX_HOUR = 360
    TWELEVE_HOUR = 720
    DAY = 1440

print MINUTE.ALL

class MINUTE(object):
    ONE_MINUTE = 1
    THREE_MINUTE = 3
    FIVE_MINUTE = 5
    QUARTER_HOUR = 15
    HALF_HOUR = 30
    HOUR = 60
    TWO_HOUR = 120
    FOUR_HOUR = 240
    SIX_HOUR = 360
    TWELEVE_HOUR = 720
    DAY = 1440


class PDMINUTE(Enum):
    MINUTE.ONE_MINUTE = "1min",
    MINUTE.THREE_MINUTE = "3min",
    MINUTE.FIVE_MINUTE = "5min",
    MINUTE.QUARTER_HOUR = "15min",
    MINUTE.HALF_HOUR = "30min",
    MINUTE.HOUR = "1H",
    MINUTE.TWO_HOUR = "2H",
    MINUTE.FOUR_HOUR = "4H",
    MINUTE.SIX_HOUR = "6H",
    MINUTE.TWELEVE_HOUR = "12H",
    MINUTE.DAY = "1D",


for e in PDMINUTE:
    print e
