import lianjia_downloder
import lianjia_html_parser
import lianjia_url_manager
import lianjia_outputer


class LianjiaSpider(object):
    def __init__(self):
        self.urls = lianjia_url_manager.UrlManager()
        self.downloader = lianjia_downloder.HtmlDownloader()
        self.parser = lianjia_html_parser.HtmlParser()
        self.outputer = lianjia_outputer.HtmlOutper()

    def draw(self):
        count = 1
        self.urls.url_store()
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d:%s' % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_data = self.parser.parse(new_url, html_content)
                self.outputer.collectd_data(new_data)
                count += 1
                if count == 80:
                    break
            except Exception as e:
                print('craw faild: ', e)
        self.outputer.output_html()


if __name__ == '__main__':

    LianjiaSpider().draw()
