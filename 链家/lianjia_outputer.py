class HtmlOutper(object):
    def __init__(self):
        self.datas = []

    def collectd_data(self, new_data):
        if new_data is None:
            return
        self.datas += new_data

    def output_html(self):
        html1 = """
          <!DOCTYPE html>
              <html lang="en">
                  <head>
                      <meta charset="UTF-8">
                      <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
                      <title>链家</title>
                      <style>
      *{margin: 0;padding: 0;}

      body{display: flex;padding: 10px;flex-wrap: wrap}

    </style>
                  </head>
              <body>

          """
        html2 = """</body>
                  </html>
              """
        f = open('meizi.html', 'w', encoding='utf8')
        f.write(html1)
        for i in self.datas:
            f.write(str(i))
        f.write(html2)
        f.close()
