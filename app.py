from flask import Flask, render_template

from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def home ():

  newsapi = NewsApiClient(api_key= 'a71b570af85a4a83871d2e569a90d250')

  top_headlines = newsapi.get_top_headlines(sources = 'bbc-news')

  all_articles = newsapi.get_everything(sources='bbc-news')

  t_articles = top_headlines['articles']

  news = []
  desc = []
  img = []
  p_date = []
  url = []

  for i in range(len(t_articles)):
    main_article = t_articles[i]

    #append all the contents in to each of lists
    news.append(main_article['title'])
    desc.append(main_article['description'])
    img.append(main_article['urlToImage'])
    p_date.append(main_article['publishedAt'])
    url.append(main_article['url'])

    contents = zip(news,desc,img,p_date,url)

  return render_template('home.html', contents=contents)

if __name__ == '__main__':
  app.run(debug=True)