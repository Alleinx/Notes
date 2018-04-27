# Version :  2018/4/28 , ends to P.27 , start from P.28 next time
# See     : 【Python网络爬虫与信息提取】.MOOC. 北京理工大学
#            URL:'https://www.bilibili.com/video/av9784617/?p=28'
# 
import requests

# BeautifulSoup -> 默认编码:'UTF-8'
from bs4 import BeautifulSoup

r = requests.get('https://python123.io/ws/demo.html')

demo = r.text

soup = BeautifulSoup(demo, 'html.parser')

# soup.prettify()函数返回更加友好的html string;
print(soup.prettify())


# <title>This is a python demo page</title>
print(soup.title)

# <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
print(soup.a)

# a
print(soup.a.name)

# p
print(soup.a.parent.name) 

# body
print(soup.a.parent.parent.name)

# <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
# @return : {'href': 'http://www.icourse163.org/course/BIT-268001', 'class': ['py1'], 'id': 'link1'}
# 作用: 获取标签的属性,将其存储到字典中
print(soup.a.attrs)

# <a ...>Basic Python</a>
# @return : 'Basic Python'
# 从标签中获取值
print(soup.a.string)


print(soup.html.contents)

for i in soup.html.children:
    print(i)

# Elements of BeautifulSoup:
# Tag             :  <> , </>
# Name            :  <tag>.name
# Attributes      :  <tag>.attrs
# NavigableString :  <tag.string>
# Comment         :  

# soup = BeautifulSoup(demo,'html.parser')
    # demo 是 html 格式的字符串
    # 'html.parser' 是一种解析html网页的方式

# soup.tag ->返回第一个匹配的标签
    # soup.p ->返回网页的第一个p标签,及其中的属性+内容

# soup.tag.attrs ->返回一个字典,其中存储标签的属性值.
    # soup.p.attrs -> {'href': 'http://www.icourse163.org/course/BIT-268001', 'class': ['py1'], 'id': 'link1'}
    # soup.p.attrs['href'] -> 'http://www.icourse163.org/course/BIT-268001'

# soup.tag.string ->返回标签中的内容
    # soup.p.stirng -> 'Basic Python'


# html 基本格式
    # 遍历方式:

        # 讲解所使用的例子:
            # <body>
                #   <p><b>content</b></p><p>hello world!</p>
            # </body>

        # background knowledge:
        #       <body>        
        #       /    \
        #      <p>   <p>
        #      /       \
        #    <b>    'hello world!'
        #    /
        #  'content'
        # HTML 结点树

        # 下行遍历

            # 从<html> 开始向下遍历
            # 注意: 只会匹配第一次出现的tag, 比如html中有多个 <p> , 但只会匹配第一个.

                # soup.tag.contents
                    # tag节点所有子结点的列表, 将 tag 所有儿子结点存入列表.
                    # @return : [<p><b>content</b></p>]
                    

                # soup.tag.children
                    # 返回迭代类型,包含tag的子结点.
                    # @return :<p><b>content</b></p>

                # soup.tag.descendants
                    # 子孙结点的迭代类型,包含所有子孙结点,用于循环遍历
                    # 不同于.children 和 .contents , .descendants返回所有子结点:

                    # @return : 
                    # <p><b>content</b></p>
                    # <b>content</b>
                    # 'content'

        # 上行遍历
            # 从<html>下的某个 Tag 向上遍历

                # soup.tag.parent
                    # 返回结点的父亲标签
                
                # soup.tag.parents
                    # 节点先辈标签的迭代类型,用于循环遍历先辈结点.

        # 平行遍历
            # 平级Tag 之间的遍历, 可遍历父节点下的所有平级结点,无论类型是否相同.
            # 平行遍历发生在同一个父节点的各节点间 : Eg. 同在<body>下结点的可以相互遍历,但无法遍历<head>中的结点.
            # <>之间的字符串,'\n'也单独构成结点.

                # soup.tag.next_sibling
                    # 返回 html文本顺序的下一个平行结点标签

                # soup.tag.previous_sibling
                    # 返回 html文本顺序的上一个平行结点标签

                # soup.tag.next_siblings
                    # 迭代类型,返回html文本顺序的后续所有平行结点的标签

                # soup.tag.previous_siblings
                    # 迭代类型,返回html文本顺序的后续所有平行结点的标签

# TODO: LEARN MORE 

# XML
    # <name> ... </name> ->有内容
    # <name />           ->无内容
    # <!--   -->         ->comment

# JSON
    # key : value
        # "name" : "J"
    # key : list
        # "name" : ["J","Y"]
    # key : dict
        # "name" : {
        #       "new_name" : "A"
        #       "old_name" : "B" 
        # }

# YAML 
    # 无类型键值对 key : value
    # name : VFIW

    # name :
        # new_name : A
        # old_name : B

    # 表达并列关系
    # name :
        # -A
        # -B

    # | 表示整块数据
    # text : |
    # LONG STRING HERE ...

