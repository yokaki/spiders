class UrlManager(object):
    def __init__(self):
        self.new_ulrs = set()
        self.old_urls = set()

    def add_new_url(self, link):
        if link is None:
            return
        if link not in self.new_ulrs and link not in self.old_urls:
            self.new_ulrs.add(link)

    def add_new_urls(self, link):
        if link is None:
            return
        self.add_new_url(link)

    def has_new_url(self):
        return len(self.new_ulrs) != 0

    def get_new_url(self):
        new_url = self.new_ulrs.pop()
        self.old_urls.add(new_url)
        return new_url
