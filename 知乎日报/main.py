import zhihu_collect
import zhihu_url
import zhihu_downloader


class Spider(object):
    def __init__(self):
        self.url = zhihu_url.UrlManager()
        self.downloader = zhihu_downloader.Download()
        self.collect = zhihu_collect.Collect()
        self.num = 1

    def draw(self):
        self.url.get_url_list()
        if self.url.has_url():
            while True:
                try:
                    new_url = self.url.get_new_url()
                    print(self.num, new_url)
                    json_content = self.downloader.download(new_url)
                    self.collect.collect(json_content)
                    print('Saved')
                    self.num += 1
                    if self.num == 600:
                        break
                except Exception as e:
                    print('craw failed:', e)


if __name__ == '__main__':
    Spider().draw()
