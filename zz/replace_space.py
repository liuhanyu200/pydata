# coding:utf-8
# 2021年07月05日11点25分19秒
# 从cmd窗口导出的pip包中间存在空格，不能直接二次使用，需要做一个处理，替换中间空格为 ==

# 返回不为空的字符串
def is_not_empty(s):
    return s and len(s.strip()) > 0


# 读取requirements.txt的内容替换空格输出到out.txt里面
f = open('requirements.txt', 'r')
out = open('out.txt', 'w')
# 读取文件每一行，循环处理
for line in f.readlines():
    # 将每一行的字符串变成一个list，删除空格元素,通过join将list连接成一个字符串写入文件
    new_line = '=='.join(list(filter(is_not_empty, line.split(' '))))
    out.write(new_line)
f.close()
out.close()
