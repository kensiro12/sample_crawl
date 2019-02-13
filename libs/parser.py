from bs4 import BeautifulSoup

def getProductInfo(li):

    name = li.find("span", {"class": "name"}).text
    price = li.find("span", {"class": "sum"}).text
    link = li.find("li")["onclick"].replace("location.", "").replace("';", "")
    image = li.find("div", {"class": "p_img"})
    image2 = image.find("src").replace
    #image2 = image.find("src").replace("img class=", "").replace(" onerror="this.", "").replace('width="190', '')

    print('==================================')
    print(name, price, image, link)
    return {"name": name, "link": link}
    # 반복문인데도 불고하고, 하나의 아이템 이름, 링크만 찾음
    # return값을 왜 못받아오는지?

def parse(pageString):

    bsObj = BeautifulSoup(pageString, 'html.parser')
    uls = bsObj.findAll("div", {"class": "p_m_list"})

    #print(uls)
    return [getProductInfo(li) for li in uls]


'''
def getProductInfo(li):

    name = li.find("span", {"class": "name"}).text
    price = li.find("span", {"class": "sum"}).text
    #link = li.find('onclick')
    image = li.find("div", {"class": "p_img"})
    #print(link)
    print(image)
    # 왜 dic으로 값을 못받을까?????
    #return {"price": price}

def parse(pageString):

    bsObj = BeautifulSoup(pageString, 'html.parser')
    uls = bsObj.findAll("div", {"class": "p_con"})

    return [getProductInfo(li) for li in uls]

'''