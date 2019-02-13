from libs.crawl import getPageStr
from libs.parser import parse


#for page_no in range(1, 3):
     #   driver.get('http://soramall.net/shop/goods/goods_list.php/np=%s&sp=1&category=022&sort=hit&order=desc' % str(page_no))
      #  html = driver.page_source

       # return html


driver = getPageStr(1)
for pageNo in range(1, 3):

    base_url = 'http://soramall.net/shop/goods/goods_list.php?np={}&sp=1&category=022&sort=hit&order=desc'
    url = base_url.format(pageNo)
    driver = driver.get(url)
    html = driver.page_source

    result = parse(html)

# 반복문을 실행할 경우, 매번 새롭게 접속을 하게 되는데, 이렇게 구현되는게 맞는지?

'''
pageString = getPageStr(2)
result = parse(pageString)
'''
