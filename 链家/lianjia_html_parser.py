from bs4 import BeautifulSoup


class HtmlParser(object):
    def __init__(self):
        self.dataobj = {}

    def parse(self, new_url, html_content):
        if new_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_data = self._get_new_data(new_url, soup)
        return new_data

    def _get_new_data(self, new_url, soup):
        # <li class="clear">
        data_list = soup.find_all('li', {'class': 'clear'})
        return data_list
