import requests
#采集网站上的个人会员的JSON数据
#获取url

def wozhuliangyuan_url(page):
    for i in range(1,page+1):
        url = 'http://www.7799520.com/api/user/pc/list/search?startage=21&endage=30&gender=2&marry=1&page={}'.format(i)
        r = requests.get(url)
        data = r.json()
        #获取数据
        data = data['data']['list']
        for dat in data:
            #保存数据
            with open('wozhuliangyuan1.txt','a',encoding='utf-8') as f:
                f.write(str(dat)+'\n')

if __name__ == "__main__":
    wozhuliangyuan_url(5)