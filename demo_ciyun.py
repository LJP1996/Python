import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
text= open(r'C:\Users\鹏COMPUTER\Desktop\we.txt').read()

wordlist_after_jieba = jieba.cut(text, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
background_pic = plt.imread(r'C:\Users\鹏COMPUTER\Pictures\Saved Pictures\stormtrooper_mask.jpg')

my_wordcloud = WordCloud(max_font_size=200,min_font_size=30,font_path="D:\pycharm\fonts\truetype\sim\simfang.ttf",mask=background_pic,background_color='White').generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()