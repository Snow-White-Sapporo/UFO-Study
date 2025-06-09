import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Retrieve data from Power BI (assuming only the "comments" column is imported via PQ)
text = " ".join(dataset["comments"].dropna())  # Remove missing values and concatenate text

# Define stopwords
stop_words = ["may", "might", "will", "another"] + list(STOPWORDS)

# Create WordCloud (specified conditions)
wc = WordCloud(
    background_color='white', 
    stopwords=stop_words, 
    width=3000, height=2000,
    colormap='inferno',
    min_font_size=5,
    min_word_length=2
)

# Generate WordCloud
wordcloud = wc.generate(text)

# Display
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

