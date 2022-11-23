# This is a simple text analysis project aiming to reveal news sentiment for the given dataset in csv format
# Author: Daila1
#Created Time: 2022.11.23

## Import and Check Data
import pandas as pd
dt1 = pd.read_csv("C:/Users/huawei/OneDrive - Nanyang Technological University/Desktop/Github Program/Text_Mining Project/news.csv")
dt1.head()

## Set Environment
# Need to install nlkt and download vader_lexicon ahead
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

## Analysis and Visual
positive = []
negative = []
neutral = []
for i in range(len(dt1["clean_text"])):
    score = analyzer.polarity_scores(dt1.iloc[i,-1])["compound"]
    if score < -0.05:
        negative.append(dt1.iloc[i,0])
    elif score <0.05:
        neutral.append(dt1.iloc[i,0])
    else:
        positive.append(dt1.iloc[i,0])

import matplotlib.pyplot as plt
name = ["Positive","Negative","Neutral"]
value = [len(positive),len(negative),len(neutral)]
plt.bar(name,value)



