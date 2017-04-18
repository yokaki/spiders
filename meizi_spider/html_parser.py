from bs4 import BeautifulSoup
import re


class HtmlParser(object):
    def __init__(self):
        pass

    def _get_new_urls(self, page_url, soup):
        link = soup.find('a', {'class': 'previous-comment-page'}).get('href')
        return link

    def _get_new_data(self, page_url, soup):
        img_list = soup.find_all('img', src=re.compile(r'//wx*?'))
        src_list = []
        for i in img_list:
            src = 'http:' + i.get('src')
            src_list.append({'src':src})
        return src_list

    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        link = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return link, new_data
