import json


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        num = 1
        for d in self.datas:
            d = json.dumps(d, ensure_ascii=False)
            f = open('./data/meizi' + str(num) + '.json', 'w', encoding='utf8')
            f.write(d)
            f.close()
            num += 1
