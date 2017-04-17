import requests


class HtmlDownloader(object):
    def download(self, new_url):
        if new_url is None:
            return None
        res = requests.get(new_url)
        return res.text
