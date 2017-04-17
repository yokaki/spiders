from bs4 import BeautifulSoup


class HtmlParser(object):
    def parser(self, new_url, html_content):
        datas = []
        if new_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser')
        items = soup.find_all('tr', {'class': 'item'})
        for i in items:
            title = i.find('div', {'class': 'pl2'}).find('a').get('title')
            rating_nums = i.find('span', {'class': 'rating_nums'}).text
            info = i.find('p', {'class': 'pl'}).text
            img = i.find('img').get('src')
            datas.append({'title': title, 'rating_nums': rating_nums, 'info': info, 'img': img})
        return datas
