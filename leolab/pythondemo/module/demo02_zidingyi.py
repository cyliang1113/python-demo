# coding: utf-8

import sys
sys.path.append('../../../')
import leolab.pythondemo.module.add_module as add_module
from leolab.pythondemo.module.add_module import add2

print(add_module)
print(add_module.add(1, 2))
print(add_module.sum)
print(add2(2, 2))

print(add_module.__name__)
print(__name__)
print(sys.path)