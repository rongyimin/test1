import requests
from bs4 import BeautifulSoup
#import pprint
import json
 
def download_all_htmls():
#下载所有列表页面的HTML，用于后续的分析
    htmls=[]
    for idx in range(3):
        url=f"http://www.crazyant.net/page/{idx+1}"
        print("crawhtml",url)
        r=requests.get(url)
        if r.status_code!=200:
            raise Exception("error")
        htmls.append(r.text)
    return htmls

htmls = download_all_htmls()
#print(htmls[0])

def parse_single_html(html):
    soup=BeautifulSoup(html,'html.parser')
  
    articles=soup.find_all("article")
    datas=[]
    for article in articles:
        
        title_node=(article.find("h2",
                        class_="entry-title").find("a"))
        title=title_node.get_text()
        link=title_node["href"]
        tag_nodes=(article.find("footer",class_="entry-footer"))
        tags=[tag_node.get_text() for tag_node in tag_nodes]
        datas.append({"title":title,"link":link,"tags":tags})
    return datas
 
#pprint.pprint(parse_single_html(htmls[0]))
 
all_datas=[]
for html in htmls:
    all_datas.extend(parse_single_html(html))
all_datas
len(all_datas)
                             
with open("all_article_links.json","w")as fout:
    for data in all_datas:
        fout.write(json.dumps(data,ensure_ascii=Fa1se)+"\n")                
