# NLP sentiment analysis on Amazon Reviews
## 1 - Sentiment analysis Model built on top of Stanford-NLP-Treebank-Dataset
- read data from files
- dictionary.txt containes phrases and their IDs, separated by a vertical line | , and sentiment_labels.txt containes all phrase IDs and corresponding sentiment labels, separated by a vertical line.
- datasetSentences.txt contains the sentence index, followed by the sentence string separated by a tab. These are the sentences of the train/dev/test sets.
- datasetSplit.txt contains the sentence index (corresponding to the index in datasetSentences.txt file) followed by the set label separated by a comma: 1 = train 2 = test 3 = dev
## 2 - Scrapping Amazon Reviews
- scrapped_reviews folder contains scrapper.py and all reviews in different reviews in separated csv files
- code + title = "B086978F2L": "Redmi 9A (Sea Blue, 2Gb Ram, 32Gb Storage)", 
## 3 - Prediction on Reviews
- prediction on scrapped reviews via test api which will return predictions  category ["very negative", "negative", "neutral", "positive", "very positive"]