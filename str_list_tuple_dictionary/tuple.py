#!/usr/bin/env python3
# -*- coding: utf-8 -*-
tup1=(1,2,3,4,5,6,7)                        #如果无组只有一个元素，要以,结尾如  (1,)
tup2=(2,3,4,5,6,7,8)
tup1.count(1)                               #统计元素出现次数
tup1.index(2)                               #找到会2的下标,找到一个后即结束
max(tup1)                                   #返回元组中的最大值
min(tup1)                                   #返回元组中的最小值

'''除了不能修改删除等操作外其它与list一样.不一一列举,重要的事说三次，
tuple(元组)生成后是只读，tuple(元组)生成后是只读，tuple(元组)生成后是只读。'''