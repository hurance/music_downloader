V0.1 #1.11
*使用此工程前需仔细阅读下项
1.代码文件在code文件夹中
2.运行代码前保证Python版本3.7及以上
3.安装库：
	pip install requests
	pip install prettytable
4.下载成功音乐将会存入code中的music文件夹中
5.此工程音乐下载源来在与QQ音乐，目前不能下载VIP歌曲，考虑之后会添加
6.之后预计会更新UI文件，将此工程整合成音乐播放及下载器。

V0.2 #1.12
1.目前已加入下载vip音乐功能，采用加入VIP账号的cookie
可自行找到header,修改cookie即可。
2.需要下载vip歌曲请用download_vip.py下载，测试账号有三天会员时间。

V0.3 #1.13
1.新增下载源，网易云音乐。
2.最新版本请用Download_Mutiple_Source.py
3.使用前请配置环境
  安装库：
      pip install beautifulsoup4
      pip install selenium
4.网易云音乐采用的是动态js加载html,所以不直接抓取html。故本工程使用
selenium模拟网页，待js加载结束获取标签。用户需保证电脑上有Chrome浏览器，
下面介绍如何配置webdriver:
   1.查询浏览器版本，在设置的关于chrome中查看版本
     例：版本 96.0.4664.110（正式版本） （64 位）
   2.下载同版本chromedriver.exe
     下载地址：https://sites.google.com/chromium.org/driver/downloads
   3.将chromedriver放置谷歌浏览器根目录，python根目录
      具体教程：https://blog.csdn.net/ysfscdn/article/details/119239382
   4.修改py文件webdriver地址
      将executable_path="D:/toolfile/python/selenium/chromedriver.exe"
      改为自己chromedriver.exe所在路径。
 自此配置完成

V0.4 #1.15
1.新增UI界面，主文件为DM_with_ui.py，需将更新后Download_Mutiple_Source.py和music_downloader.py置于同一根目录。
2.修复Download_Mutiple_Source.py数据错误bug
3.ui文件已放入ui文件夹中，可自行采用
