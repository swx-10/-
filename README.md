# 查找-前向最大匹配
前向匹配算法是指从左到右逐渐匹配词库中的词语。首先会规定词的最大长度，每次寻找都从当前位置开始，选取词的最大长度的语句片段和词库里的每个词进行匹配，如果没有找到，则缩短长度继续寻找，直到找到或成为单字。如果成为单字也没有找到，则将匹配位置向后挪一个。若找到了，则删除/跳过这个词然后开始下一个最大长度词组的循环。如果剩余长度不足最大长度，则取剩余长度然后进行循环。

### 匹配实例：
>待匹配子串：“我们经常有意见分歧”
假设字典最长词为5
词典：[“我们”，“经常”，“有”，“有意见”，“意见”，“分歧”]

##### 第一轮：从前往后取长度为5的子串为“我们经常有”
>我们经常有 （词典没有该词，去掉最右一个字）
我们经常 （词典没有该词，去掉最右一个字）
我们经（词典没有该词，去掉最右一个字）
我们（词典有该词，从待分词子串中删除该词）

##### 第二轮：取子串“经常有意见”
>经常有意见 （x）
经常有意 （x）
经常有 （x）
经常 （√）

##### 第三轮：取子串“有意见分歧”
>有意见分歧 （x）
有意见分 （x）
有意见 （√）

##### 第四轮：取子串“分歧”
>分歧 （√）  

前向最大匹配法最终的匹配结果为：[我们 , 经常 , 有意见 , 分歧]

# 后向最大匹配
与前向最大匹配类似，前向最大匹配是从左到右匹配，后向最大匹配则是从右到左进行匹配。

### 匹配实例：
>待匹配子串：“我们经常有意见分歧”
假设词典最长词为5
词典：[“我们”，“经常”，“有”，“有意见”，“意见”，“分歧”]

##### 第一轮：从前往后取长度为5的子串为“有意见分歧”
>有意见分歧 （词典没有该词，去掉最左一个字）
意见分歧 （词典没有该词，去掉最左一个字）
见分歧（词典没有该词，去掉最左一个字）
分歧（词典有该词，从待分词子串中删除该词）

##### 第二轮：取子串“经常有意见”
>经常有意见 （x）
常有意见 （x）
有意见（√）

##### 第三轮：取子串“我们经常”
>我们经常 （x）
们经常 （x）
经常 （√）

##### 第四轮：取子串“我们”
>我们 （√）

后向最大匹配法最终的匹配结果为：“我们 / 经常 / 有意见 / 分歧”
前向最大匹配和后向最大匹配的结果有90％的概率是一样的。

# 双向最大匹配法
将前向最大匹配算法和后向最大匹配算法进行比较，从而确定正确的方法。

### 算法流程：
>（1）比较前向最大匹配和后向最大匹配结果
（2）如果匹配数量结果不同，那么取匹配数量较少的那个
（3）如果匹配数量结果相同
1、匹配结果相同，说明没有歧义，可以返回任何一个
2、匹配结果不同，返回最小词长度大的那个