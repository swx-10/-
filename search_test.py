import os
import ahocorasick
import pickle

def creat_trie(data_file, save_file):
    ac = ahocorasick.Automaton()

    with open(data_file, encoding='utf-8') as f:
        lines = f.readlines()
        for id, line in enumerate(lines):
            #向tire树中添加数据
            ac.add_word(line.strip(), line.strip())

    ac.save(save_file, pickle.dumps)

def load_trie(trie_data):
    """加载保存的trie树数据，并转化为ac自动机"""
    #加载tire数据
    trie = ahocorasick.load(trie_data, pickle.loads)

    #将trie树转换为AC自动机，以启用Aho-Corasick搜索
    trie.make_automaton()
    return trie

if __name__=="__main__":
    cwd = os.path.dirname(__file__)
    #创建trie树
    # creat_trie(os.path.join(cwd, 'datas', 'aircraft.txt'), os.path.join(cwd, 'air.data'))

    trie_path = os.path.join(os.path.dirname(__file__), 'air.data')

    ac = load_trie(trie_path)

    max_len = max([len(x) for x in ac])
    #匹配字符串,是否在tire前缀树中，match前缀匹配
    print(ac.match('极光'))

    