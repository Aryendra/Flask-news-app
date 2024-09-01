from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def Index():


    



    newsapi = NewsApiClient(api_key='9574b6da5abe4942ac42fdb4e12d3bb5')

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(sources='al-jazeera-english')

    articles=top_headlines['articles']




    news=[]
    desc=[]
    img=[]

    for i in range(len(articles)):
        my_articles=articles[i]
        news.append(my_articles['title'])
        desc.append(my_articles['description'])
        img.append(my_articles['urlToImage'])



    content=zip(news,desc,img)

    return render_template('index.html', content=content)

@app.route('/bbc')
def Bbc():
    
    newsapi = NewsApiClient(api_key='9574b6da5abe4942ac42fdb4e12d3bb5')

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(sources='bbc-news')

    articles=top_headlines['articles']




    news=[]
    desc=[]
    img=[]

    for i in range(len(articles)):
        my_articles=articles[i]
        news.append(my_articles['title'])
        desc.append(my_articles['description'])
        img.append(my_articles['urlToImage'])



    content=zip(news,desc,img)
    return render_template('bbc.html', content=content)
                       






if __name__ == '__main__':
    app.run(debug=True)

