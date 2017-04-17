class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def url_store(self):
        base_url = 'http://cd.lianjia.com/ershoufang/pg'
        for i in range(5, 100):
            self.new_urls.add(base_url + str(i))
