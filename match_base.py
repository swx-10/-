from search_test import load_trie
import os

class Base_m():
    """匹配的基类"""
    def __init__(self, trie_file):
        if not os.path.exists(trie_file):
            raise '%s 不存在！'%(trie_file)

        self.trie = load_trie(trie_file)

    def match(self, sentence:str):
        pass

class Fmm_m(Base_m):
    """前向最大匹配"""
    def __init__(self, max_len, trie_file):
        super(Fmm_m, self).__init__(trie_file)
        self.max_len = max_len
    
    def match(self, sentence: str):
        if sentence is None or len(sentence) == 0:
            return []
        
        index = 0
        text_size = len(sentence)
        while text_size > index:
            word = ''
            for size in range(min(self.max_len+index,text_size), index, -1):
                word = sentence[index:size]
                if self.trie.exists(word):
                    index = size - 1
                    # break

                    # index += 1
                    yield word
                    break
            index += 1

class Rmm_m(Base_m):
    """后向最大匹配"""
    def __init__(self,max_len, trie_file):
        super(Rmm_m, self).__init__(trie_file)
        self.max_len = max_len

    def match(self, sentence: str):
        if sentence is None or len(sentence) == 0:
            return []

        result = []
        index = len(sentence)
        win_size = min(index,self.max_len)
        while index > 0:
            word = ''
            for size in range(index-win_size,index):
                word = sentence[size:index]
                if self.trie.exists(word):
                    index = size + 1
                    result.append(word)
                    break
            index -= 1

        result.reverse()
        for word in result:
            yield word

class Bimm_m(Base_m):
    """双向最大匹配"""
    def __init__(self,max_len, trie_file):
        super().__init__(trie_file)
        self.fmm = Fmm_m(max_len=max_len, trie_file=trie_file)
        self.rmm = Rmm_m(max_len=max_len, trie_file=trie_file)
    
    def match(self, sentence: str):
        if sentence is None or len(sentence) == 0:
            return []

        fmm_result = [word for word in self.fmm.match(sentence)]
        rmm_result = [word for word in self.rmm.match(sentence)]
        if len(fmm_result) == len(rmm_result):
            if fmm_result == rmm_result:
                result = fmm_result
            else:
                result = fmm_result if min([len(x) for x in fmm_result]) > min([len(x) for x in rmm_result]) else rmm_result
        else:
            result = fmm_result if len(fmm_result) > len(rmm_result) else rmm_result

        for word in result:
            yield word


if __name__=="__main__":

    trie_path = os.path.join(os.path.dirname(__file__), 'name.data')

    sentence = '同温层加油机可以给攻击鹰战斗机加油'
    #前向最大匹配
    fmm = Fmm_m(trie_file=trie_path, max_len=8)
    # word = fmm.match(sentence)
    
    #后向最大匹配
    rmm = Rmm_m(max_len=8, trie_file=trie_path)
    # word = rmm.match(sentence)

    #双向最大匹配
    bimm = Bimm_m(max_len=8, trie_file=trie_path)
    word = bimm.match(sentence)
    for m in word:
        print(m)