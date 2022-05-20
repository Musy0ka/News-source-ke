from flask import Flask, render_template

from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def home ():

  newsapi = NewsApiClient(api_key= 'a71b570af85a4a83871d2e569a90d250')

  top_headlines = newsapi.get_top_headlines(sources = 'bbc-news')

  all_articles = newsapi.get_everything(sources='bbc-news')

  return render_template('home.html')

if __name__ == '__main__':
  app.run(debug=True)