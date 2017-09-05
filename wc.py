from PIL import Image,ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator

image= Image.open('lion.jpg')
keywords = dict()
for i in open("data.txt"):
    s = i.split(' ')
    keywords[s[1].strip()] = float(s[0])
print(keywords)
graph = np.array(image)
wc = WordCloud(font_path = 'library/fonts/WeibeiSC-Bold.otf',background_color='White',max_words=10000,mask=graph).generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off")
plt.show()
