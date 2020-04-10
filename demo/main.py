from scrapy import cmdline

# 命令
# 创建项目
# scrapy startproject 项目名(douban)
# 创建爬虫文件
# scrapy genspider 爬虫名(douban_spider) 域名(movie.douban.com/top250)
# 开始爬
# scrapy crawl douban_spider

cmdline.execute('scrapy crawl douban_spider'.split())