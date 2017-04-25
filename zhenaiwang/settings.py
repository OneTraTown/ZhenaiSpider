# -*- coding: utf-8 -*-

# Scrapy settings for zhenaiwang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhenaiwang'

SPIDER_MODULES = ['zhenaiwang.spiders']
NEWSPIDER_MODULE = 'zhenaiwang.spiders'

DOWNLOAD_DELAY = 1

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'zhawdb'
MONGODB_COLLECTION = 'zhaw'

HEDULER = "scrapy_redis.scheduler.Scheduler"    #调度
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  #去重
SCHEDULER_PERSIST = True       #不清理Redis队列
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"    #队列

DEFAULT_REQUEST_HEADERS = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
   'Accept': 'application/json, text/javascript, */*; q=0.01',
   'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
   'Accept-Encoding': 'gzip, deflate',
   'X-Requested-With': 'XMLHttpRequest',
   'Referer': 'http://search.zhenai.com/v2/search/pinterest.do?'
              'sex=1&agebegin=18&ageend=-1&workcityprovince=-1&workcitycity=-1'
              '&info=&h1=-1&h2=-1&salaryBegin=-1&salaryEnd=-1&occupation=-1&h=-1'
              '&c=-1&workcityprovince1=-1&workcitycity1=-1&constellation=-1&animals=-1'
              '&stock=-1&belief=-1&lvBegin=-1&lvEnd=-1&condition=66&orderby=hpf&hotIndex=&online=',
}

ITEM_PIPELINES = {
    'zhenaiwang.pipelines.ZhenaiwangPipeline':300
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' : None,
    'zhenaiwang.spiders.rotate_useragent.RotateUserAgentMiddleware': 400
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhenaiwang (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhenaiwang.middlewares.ZhenaiwangSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhenaiwang.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhenaiwang.pipelines.ZhenaiwangPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
