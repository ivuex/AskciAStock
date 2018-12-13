# -*- coding:utf-8 -*-

def camel2underline(string):
    string = string[0].lower() + string[1:]
    res_str = string[0].lower()
    minOrd = ord('A')
    maxOrd = ord('Z')
    for i in list(range(1, len(string))):
        char = string[i]
        if minOrd <= ord(char) <= maxOrd:
            res_str += '_' + char.lower()
        else:
            res_str += char
    return res_str
# print(camel2underline('AbcDefgZ'))


