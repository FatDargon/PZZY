# -*- coding:UTF-8 -*-
def pretty_dict(obj, indent=' '):
    def _pretty(obj, indent):
        for i, tup in enumerate(obj.items()):
            k, v = tup
            # 如果是字符串则拼�?""
            if isinstance(k, basestring): k = '"%s"' % k
            if isinstance(v, basestring): v = '"%s"' % v
            # 如果是字典则递归
            if isinstance(v, dict):
                v = ''.join(_pretty(v, indent + ' ' * len(str(k) + ': {')))  # 计算下一层的indent
                # case,根据(k,v)对在哪个位置确定拼接�?�?
            if i == 0:  # �?�?,拼左花括�?
                if len(obj) == 1:
                    yield '{%s: %s}' % (k, v)
                else:
                    yield '{\n %s: %s,\n' % (k, v)
            elif i == len(obj) - 1:  # 结尾,拼右花括�?
                yield '%s%s: %s\n}' % (indent, k, v)
            else:  # 中间
                yield '%s%s: %s,\n' % (indent, k, v)
    print ''.join(_pretty(obj, indent))
# d = { "root": { "folder2": { "item2": None, "item1": None }, "folder1": { "subfolder1": { "item2": None, "item1": None }, "subfolder2": { "item3": None } } } }
# pretty_dict(d)
def pretty_list(obj):
    for item in obj:       
        pretty_dict(item, indent=' ')
        print "*"*20


def pretty_little_list(obj):
    '''
    打印utf-8的list
    '''
    for item in obj:
        print item
