import douban_url_manager
import douban_html_parser
import douban_downloder
import douban_outputer


class DoubanMovie(object):
    def __init__(self):
        self.urls = douban_url_manager.UrlManager()
        self.downloader = douban_downloder.HtmlDownloader()
        self.parser = douban_html_parser.HtmlParser()
        self.outputer = douban_outputer.HtmlOutputer()

    def draw(self):
        count = 1
        self.urls.url_store()
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d :%s' % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_data = self.parser.parser(new_url, html_content)
                self.outputer.collect_data(new_data)
                count += 1

            except Exception as e:
                print('craw faild: ', e)
        self.outputer.output_html()


if __name__ == '__main__':
    DoubanMovie().draw()
