from lxml import etree
import requests as req
import re
def ip1(shuru):
    # str1 = input("请输入：")
    str2=("http://ip138.com/ips138.asp?ip="+shuru+"&action=2")
    url=str2
    r=req.get(url).content.decode('gb2312')  
    html = etree.HTML(r)
    html_data=html.xpath('/html/body/table/tr[3]/td[1]/ul/li/text()')
    resule={}
    res=str(html_data)
    t=re.findall("""'(.*?)：(.*?)'""",res)
    p=str(t)
    print(dict(eval(p.replace('[','').replace(']',''))))
def ip(shuru):
    str2=("http://ipwhois.cnnic.cn/bns/query/Query/ipwhoisQuery.do?queryOption=ipv4&txtquery={}").format(shuru)
    r=req.get(str2).content.decode('utf-8') 
    html = etree.HTML(r)
    chuli=html.xpath('//*[@size="2"]/text()')
    S=str(chuli).replace('[','').replace(']','').split("a0',")
    d=[x.replace('\\x','') for x in S]
    for i in range (0,20):
        D=d[i]
        print(D)
def ac(shuru):
    str3=("http://ipwhois.cnnic.net.cn/bns/query/Query/ipwhoisQuery.do?txtquery={}&queryOption=asn&CSRT=13716581114779199258").format(shuru)
    r1=req.get(str3).content.decode('utf-8')
    html1 = etree.HTML(r1)
    chuli=html1.xpath('//*[@size="2"]/text()')
    S=str(chuli).replace('[','').replace(']','').split("a0',")
    d=[x.replace('\\x','') for x in S]
    for i in range (0,20):
        D=d[i]
        print(D)
        

    
if __name__ == "__main__":
    shuru=input("输入ip或者ac号:")
    if re.match('^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',shuru):
        ip1(shuru)
        ip(shuru)
                                                                   
    elif re.match('(AS)?[0-9]{4}',shuru):
        ac(shuru)
    else:
        print('错误')
