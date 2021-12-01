import requests
from bs4 import BeautifulSoup


def get_articles(keywords):
    response = requests.get('https://habr.com/ru/all/')
    response.raise_for_status()
    soup = BeautifulSoup(response.text, features="html.parser")
    articles = soup.find_all('article', class_='tm-articles-list__item')
    keywords_set = set(keywords)
    for article in articles:
        header = article.find('h2')
        article_text = article.find('div', class_='tm-article-body tm-article-snippet__lead').text
        public_date = article.find('span', class_="tm-article-snippet__datetime-published").text
        post_link = 'https://habr.com' + article.find('a', class_="tm-article-snippet__title-link").get('href')
        article_set = set(article_text.text.strip().split(" "))
        if keywords_set & article_set:
            print(f'Дата: {public_date} - Заголовок: {header} - Ссылка: {post_link}')


if __name__ == '__main__':
    # определяем список ключевых слов
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']

    get_articles(KEYWORDS)
