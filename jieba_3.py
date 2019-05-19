# -*- coding: utf-8 -*-

#关键词提取
"""
基于 TF-IDF 算法的关键词抽取 
　　 　　jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=(‘ns’, ‘n’, ‘vn’, ‘v’)) 
　　 　　参数解释： 
　　 　　　　(1)sentence ：待提取的文本； 
　　 　　　　(2)topK ：返回K个权重最大的关键词 
　　 　　　　(3)withWeight ：是否返回权重 
　　 　　　　(4)allowPOS ：是否仅包括指定词性的词
"""
import jieba.analyse

kWords = jieba.analyse.extract_tags("你吃了吗？我吃了，你呢？我还很饱，不是很想吃，现在超级想睡觉的。没什么啦~问问而已。哈哈", topK=5, withWeight=True)
for word, weight in kWords:
    print (word, ":", weight)

#----------------------------------------------------

"""
注： 关键词提取所使用逆文频（IDF）库、停用词库可切换成自定路径 
　　基于 TextRank 算法的关键词抽取 
　　 　　jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=(‘ns’, ‘n’, ‘vn’, ‘v’)) 
　　 　　参数解释： 
　　 　　　　(1)sentence ：待提取的文本； 
　　 　　　　(2)topK ：返回K个权重最大的关键词 
　　 　　　　(3)withWeight ：是否返回权重 
　　 　　　　(4)allowPOS ：是否仅包括指定词性的词 
　　 　　TextRank基本思想： 
　　 　　　　(1)分词 
　　 　　　　(2)找词之间共现关系，构建图 
　　 　　　　(3)计算图中节点的PageRank
"""

kWords = jieba.analyse.textrank("今天吃什么呢？", topK=5, withWeight=True)
for word, weight in kWords:
    print (word, ":", weight)


