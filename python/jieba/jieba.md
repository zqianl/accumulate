##jieba ##

来自：http://www.oschina.net/p/jieba

### [http://git.oschina.net/fxsjy/jieba](http://git.oschina.net/fxsjy/jieba) ###

	
### [http://www.oschina.net/p/jieba](http://www.oschina.net/p/jieba) ###

### 功能 1)：分词 ###

jieba.cut方法接受两个输入参数: 1) 第一个参数为需要分词的字符串 2）cut_all参数用来控制是否采用全模式

jieba.cut_for_search方法接受一个参数：需要分词的字符串,该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细

注意：待分词的字符串可以是gbk字符串、utf-8字符串或者unicode

jieba.cut以及jieba.cut_for_search返回的结构都是一个可迭代的generator，可以使用for循环来获得分词后得到的每一个词语(unicode)，也可以用list(jieba.cut(...))转化为list
	

	#encoding=utf-8
	import jieba

	seg_list = jieba.cut("我来到北京清华大学",cut_all=True)
	print "Full Mode:", "/ ".join(seg_list) #全模式

	seg_list = jieba.cut("我来到北京清华大学",cut_all=False)
	print "Default Mode:", "/ ".join(seg_list) #精确模式

	seg_list = jieba.cut("他来到了网易杭研大厦") #默认是精确模式
	print ", ".join(seg_list)

	seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造") #搜索引擎模式
	print ", ".join(seg_list)

	output:
	【全模式】: 我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学

	【精确模式】: 我/ 来到/ 北京/ 清华大学

	【新词识别】：他, 来到, 了, 网易, 杭研, 大厦    (此处，“杭研”并没有在词典中，但是也被Viterbi算法识别出来了)

	【搜索引擎模式】： 小明, 硕士, 毕业, 于, 中国, 科学, 学院, 科学院, 中国科学院, 计算, 计算所, 后, 在, 日本, 京都, 大学, 日本京都大学, 深造

### 功能 2) ：添加自定义词典 ###

开发者可以指定自己自定义的词典，以便包含jieba词库里没有的词。虽然jieba有新词识别能力，但是自行添加新词可以保证更高的正确率

	用法： jieba.load_userdict(file_name) # file_name为自定义词典的路径

	词典格式和dict.txt一样，一个词占一行；每一行分三部分，一部分为词语，另一部分为词频，最后为词性（可省略），用空格隔开

	范例：

	之前： 李小福 / 是 / 创新 / 办 / 主任 / 也 / 是 / 云 / 计算 / 方面 / 的 / 专家 /

	加载自定义词库后：　李小福 / 是 / 创新办 / 主任 / 也 / 是 / 云计算 / 方面 / 的 / 专家 /

	自定义词典：https://github.com/fxsjy/jieba/blob/master/test/userdict.txt

	用法示例：https://github.com/fxsjy/jieba/blob/master/test/test_userdict.py

	"通过用户自定义词典来增强歧义纠错能力" --- https://github.com/fxsjy/jieba/issues/14
	

### 功能 3) ：关键词提取 ###

jieba.analyse.extract_tags(sentence,topK) #需要先import jieba.analyse

setence为待提取的文本

topK为返回几个TF/IDF权重最大的关键词，默认值为20

代码示例 （关键词提取）
https://github.com/fxsjy/jieba/blob/master/test/extract_tags.py

### 功能 4) : 词性标注 ###

	>>> import jieba.posseg as pseg
	>>> words =pseg.cut("我爱北京天安门")
	>>> for w in words:
	...    print w.word,w.flag
	...
	我 r
	爱 v
	北京 ns
	天安门 ns

### 功能 5) : 并行分词 ###

原理：将目标文本按行分隔后，把各行文本分配到多个python进程并行分词，然后归并结果，从而获得分词速度的可观提升

基于python自带的multiprocessing模块，目前暂不支持windows

	用法：

	jieba.enable_parallel(4) # 开启并行分词模式，参数为并行进程数

	jieba.disable_parallel() # 关闭并行分词模式

	例子： https://github.com/fxsjy/jieba/blob/master/test/parallel/test_file.py

	实验结果：在4核3.4GHz Linux机器上，对金庸全集进行精确分词，获得了1MB/s的速度，是单进程版的3.3倍。


### 功能 6) : Tokenize：返回词语在原文的起始位置 ###

注意，输入参数只接受unicode

	默认模式
	result = jieba.tokenize(u'永和服装饰品有限公司')
	for tk in result:
   		print "word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2])
	word 永和                start: 0                end:2
	word 服装                start: 2                end:4
	word 饰品                start: 4                end:6
	word 有限公司            start: 6                end:10


	搜索模式
	result = jieba.tokenize(u'永和服装饰品有限公司',mode='search')
	for tk in result:
    	print "word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2])
	word 永和                start: 0                end:2
	word 服装                start: 2                end:4
	word 饰品                start: 4                end:6
	word 有限                start: 6                end:8
	word 公司                start: 8                end:10
	word 有限公司            start: 6                end:10

### 功能 7) : ChineseAnalyzer for Whoosh搜索引擎 ###

引用： from jieba.analyse import ChineseAnalyzer

用法示例：https://github.com/fxsjy/jieba/blob/master/test/test_whoosh.py

### 其他词典 ###

占用内存较小的词典文件 https://github.com/fxsjy/jieba/raw/master/extra_dict/dict.txt.small

支持繁体分词更好的词典文件 https://github.com/fxsjy/jieba/raw/master/extra_dict/dict.txt.big

下载你所需要的词典，然后覆盖jieba/dict.txt 即可或者用jieba.set_dictionary('data/dict.txt.big')