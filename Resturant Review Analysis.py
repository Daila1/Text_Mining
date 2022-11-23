# This is a simple text analysis project aiming to gaining insights from customer comments
# Author: Daila1
#Created Time: 2022.11.23

##Data Import
import pandas as pd
dt2 = pd.read_csv("C:/Users/huawei/OneDrive - Nanyang Technological University/Desktop/Github Program/Text_Mining Project/Resturant.txt",sep="/n")
dt2.head()

## Analysis and Visual
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
print(analyzer.polarity_scores(dt2.iloc[1,0]))
positive = []
negative = []
neutral = []
for i in range(len(dt2)):
    score = analyzer.polarity_scores(dt2.iloc[i,0])["compound"]
    if score < -0.05:
        negative.append(dt2.iloc[i,0])
    elif score <0.05:
        neutral.append(dt2.iloc[i,0])
    else:
        positive.append(dt2.iloc[i,0])

import matplotlib.pyplot as plt
name = ["Positive","Negative","Neutral"]
value = [len(positive),len(negative),len(neutral)]
plt.bar(name,value)