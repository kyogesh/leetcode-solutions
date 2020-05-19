from collections import OrderedDict


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        result = "1"
        for i in range(n - 1):
            dict_ = OrderedDict()
            last = ''
            temp = ''
            for i in result:
                if i not in dict_:
                    if last != '':
                        temp += ''.join([str(v) + str(k) for k, v in dict_.items()])
                        del dict_[last]
                    dict_[i] = 1
                else:
                    dict_[i] += 1
                last = i
            result = temp + ''.join([str(v) + str(k) for k, v in dict_.items()])
        return result
