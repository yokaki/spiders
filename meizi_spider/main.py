import downloader
import html_parser
import url_manager
import outputer


class Main(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = outputer.HtmlOutputer()

    def draw(self, first_url):
        count = 1
        self.urls.add_new_url(first_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()  # 返回url列表的pop
                print('craw %d:%s' % (count, new_url))
                html_content = self.downloader.download(new_url)  # 返回的是页面的html
                link, new_data = self.parser.parse(new_url, html_content)  # 返回新的url和img列表
                self.urls.add_new_urls(link)
                self.outputer.collect_data(new_data)
                count += 1
                if count == 3:
                    break
            except Exception as e:
                print('craw faild', e)
        self.outputer.output_html()


if __name__ == '__main__':
    rout_url = 'http://jandan.net/ooxx'
    spider7 = Main()
    spider7.draw(rout_url)
