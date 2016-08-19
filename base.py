#!-*- coding: utf-8 -*-


def create_x(str_info='hello world',num=30,style='*'):
    # create_x() 用来生成 “******** 用户信息 ********”,这样的单行字符串
    # * 号的个数可以通过参数 'num' 指定
    # 字符信息也通过参数 'str_info' 指定
    xing = num * style
    print('{0} {1} {0}'.format(xing,str_info)) 


if __name__ == '__main__':
    create_x(str_info='用户信息',style='~')
    
