from summarizer import summarize
import nltk
#nltk.download()
with open('/Users/vatsal/NLP J comp/article.txt', 'r') as f:
#with open('/Users/vatsal/Downloads/TextSummarization-master/ab.rtf', 'r') as f:
    text = f.read()
test = summarize(text)
test=test['summary']
print(test)