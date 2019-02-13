from libs.crawl import getPageStr
from libs.parser import parse


#for page_no in range(1, 3):
     #   driver.get('http://soramall.net/shop/goods/goods_list.php/np=%s&sp=1&category=022&sort=hit&order=desc' % str(page_no))
      #  html = driver.page_source

       # return html


for pageNo in range(1, 3):
    pageString = getPageStr(pageNo)
    result = parse(pageString)

# 반복문을 실행할 경우, 매번 새롭게 접속을 하게 되는데, 이렇게 구현되는게 맞는지?

'''
pageString = getPageStr(2)
result = parse(pageString)
'''
