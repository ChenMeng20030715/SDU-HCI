import jieba
import wordcloud
# 读取文本
with open("comments.txt",encoding="utf-8") as f:
    s = f.read()
print(s)
ls = jieba.lcut(s) # 生成分词列表
text = ' '.join(ls) # 连接成字符串


stopwords = ["的","是","了"] # 去掉不需要显示的词

wc = wordcloud.WordCloud(font_path="DouyinSansBold.otf",
                         width = 540,
                         height = 400,
                         background_color='white',
                         max_words=100,stopwords=s)
# msyh.ttc电脑本地字体，写可以写成绝对路径
wc.generate(text) # 加载词云文本
wc.to_file("ciyun.png") # 保存词云文件