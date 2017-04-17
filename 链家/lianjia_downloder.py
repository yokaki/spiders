from urllib import request


class HtmlDownloader(object):
    def download(self, new_url):
        if new_url is None:
            return None
        res = request.urlopen(new_url)
        if res.getcode() != 200:
            return None
        return res.read()
