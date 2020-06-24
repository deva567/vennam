def WordAnalysis(dataframe,column):
    """This function will give the idea about the set of most used keywords
    included in dataframe column"""
    from wordcloud import WordCloud, STOPWORDS 
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
    import nltk
    from nltk.tokenize import word_tokenize
    from nltk.probability import FreqDist
    from nltk.corpus import stopwords
    from nltk.tokenize import sent_tokenize
    text = " ".join(review for review in dataframe[column])
    tokenized_word=word_tokenize(text)
    stop_words=set(stopwords.words("english"))
    filtered_sent=[]
    for w in tokenized_word:
        if w not in stop_words:
            if w not in [':',',','.',"'",'\\n','-','@','(',')','and/or','?',"'s"]:
                filtered_sent.append(w)
    fdist = FreqDist(filtered_sent)
    fdist.plot(30,cumulative=False)
    plt.show()
    
def WordCloud(dataframe,column):
    """ This function will give the word cloud for given dataframe column """
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    import nltk
    from nltk.tokenize import word_tokenize
    from PIL import Image
    from nltk.corpus import stopwords
    from nltk.tokenize import sent_tokenize
    from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
    text = " ".join(review for review in dataframe[column])
    tokenized_word=word_tokenize(text)
    stop_words=set(stopwords.words("english"))
    filtered_sent=[]
    for w in tokenized_word:
        if w not in stop_words:
            if w not in [':',',','.',"'",'\\n','-','@','(',')','and/or','?',"'s"]:
                filtered_sent.append(w)
    wordcloud = WordCloud(margin=0,stopwords=stop_words,
                      max_words=200,background_color="white", collocations = False).generate(str(filtered_sent))
    plt.figure( figsize=(10,10), facecolor = None)
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()
