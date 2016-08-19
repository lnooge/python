# -*- coding: utf-8 -*-


import os,sys
import platform
import base

'''
platform.platform() #获取操作系统的名称及版本号
platform.version() #获取操作系统的版本号
platform.architecture() #获取操作系统的位数
platform.machine() #计算机类型
platform.node() #计算机的网络名称
platform.processor() #计算机cpu信息
platform.uname() #包含上面的信息汇总


获取python的一些信息
platform.python_build()
platform.python_compiler()
platform.python_branch()
platform.python_implementation()
platform.python_revision()
platform.python_version()
platform.python_version_tuple()


'''


def info():
    base.create_x('系统信息')
    print('操作系统名称及版本号：{:>8}'.format(platform.platform()))
    print('操作系统的版本号：[{:>8}]'.format(platform.version()))
    print('计算机类型：{:>8}'.format(platform.machine()))
    print('计算机的网络名称：[{:>8}]'.format(platform.node()))
    print('CPU的信息：[{:>8}]'.format(platform.processor()))
    base.create_x('Python信息',num=29)
    print('{}'.format(platform.python_build()))
    print('{}'.format(platform.python_compiler()))
    print('{}'.format(platform.python_branch()))
    print('{}'.format(platform.python_implementation()))
    print('{}'.format(platform.python_revision()))
    print('{}'.format(platform.python_version()))
    print('{}'.format(platform.python_version_tuple()))
info()
