import json


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        if new_data not in self.datas:
            self.datas += new_data

    def output_html(self):
        json_data = json.dumps(self.datas, ensure_ascii=False)
        f = open('douban.json', 'w', encoding='utf8')
        f.write(json_data)
        f.close()

