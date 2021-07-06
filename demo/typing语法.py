# coding:utf-8
"""
在传入参数时通过“参数名:类型”的形式声明参数的类型；

返回结果通过"-> 结果类型"的形式声明结果的类型。

在调用的时候如果参数的类型不正确pycharm会有提醒，但不会影响程序的运行。

对于如list列表等，还可以规定得更加具体一些，如：“-> List[str]”,规定返回的是列表，并且元素是字符串。

typing常用的类型：

int,long,float: 整型,长整形,浮点型;

bool,str: 布尔型，字符串类型；

List, Tuple, Dict, Set:列表，元组，字典, 集合;

Iterable,Iterator:可迭代类型，迭代器类型；

Generator：生成器类型；
"""
from typing import List


def display_table(self, orders: List[List[str]]) -> List[List[str]]:
    """
    很多人在写完代码一段时间后回过头看代码，很可能忘记了自己写的函数需要传什么参数，返回什么类型的结果，
    就不得不去阅读代码的具体内容，降低了阅读的速度，加上Python本身就是一门弱类型的语言，这种现象就变得更加的严重，
    而typing这个模块很好的解决了这个问题。
    """
    pass
