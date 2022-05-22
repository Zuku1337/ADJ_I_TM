import nltk


from WordCloudVisualizer import visual as wordcloud_visualizer
from Classification import visual as classifications_visualizer

nltk.download('stopwords')
nltk.download('punkt')

wordcloud_visualizer()
classifications_visualizer()


