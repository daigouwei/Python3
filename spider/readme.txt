该目录下文件都是基于Python3.5解释器进行编码。
主要是爬虫的基本代码和实战代码。

各文件功能描述如下：
urllibb.py  url相关的基本操作。
regexp.py  正则表达式相关的基础操作。
qiushibaike.py  爬取糗事百科的热点笑话，每按一次enter键，就会刷新一个笑话。
baidutieba.py  输入百度贴吧帖子网址，爬取相关帖子内容，并保存为本地文件。
douban.py  通过输入账号和密码，登录豆瓣，进行后续信息的抓取。主要是解决一个人工解析验证码的过程。bug：有时候
           网页被限制登录，可能是代理的问题，有待进一步优化。
yzu.py  通过输入账号和密码，登录研究生网站。主要是解决一个插入的js动态验证码的解析过程。最后使用了selenium+PhantomJS
        来实现登录yzu获取账号主人信息。解决问题：（1）yzu的验证码是动态的，就算同一个时间点的连接，验证码两次访问也会
        出现不一样的情况，所以直接用selenium截取登录主界面的网页图片。（2）深层frame需要进行切换动作。（3）使用BeautifulSoup
        对获取到的html进行数据处理。（4）下载照片的问题有待后续研究。
requestss.py  主要用来熟悉模块requests的用法。
phantomjss.js  主要熟悉phantomjs的用法，需要使用phantom phantomjss.js来运行。该模块主要是模拟浏览器进行运行。
seleniumm.py  主要用来熟悉selenium的用法，配合chrome可以实现输入点击等类似人为的操作。配合phantom使用可以实现
              动态网页的解析，后期可以用来解决验证码问题，最终可以实现一键申请加班。
beautifulsoupp.py  处理html，解析需要的数据信息。一定程度上可以简化正则表达式的构成。
overtimedatahandlee.py  处理加班时间数据，满足周六日全算，平时只算晚间加班时间。
