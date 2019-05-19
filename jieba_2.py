#encoding=utf-8

import jieba

#if happened SyntaxError: (Unicode error)
#https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca

jieba.load_userdict(r"C:\Users\WymenLaw\Desktop\userdict.txt")

data = [
   "世界经济论坛也叫达沃斯论坛。",
   "The World Economic Forum is also called the Davos Forum."
   ]

for d in data:
    seg_list = jieba.cut(d)
    #词与词之间用","连接
    print('，'.join(seg_list))
    
