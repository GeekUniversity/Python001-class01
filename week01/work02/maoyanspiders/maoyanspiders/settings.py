# Scrapy settings for maoyanspiders project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'maoyanspiders'

SPIDER_MODULES = ['maoyanspiders.spiders']
NEWSPIDER_MODULE = 'maoyanspiders.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'maoyanspiders (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 4

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

DEFAULT_REQUEST_HEADERS = {
    'Content-Type': 'text/plain; charset=UTF-8',
    'Origin': 'https://maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Cookie': 'uuid_n_v=v1; uuid=8F2963A0B78111EA801551553EAD9849E8BF317E589D41B68B14B6F443E579CD; mojo-uuid=90a5645c0238bb3a951ac59e8fd65d83; _lxsdk_cuid=172ef9a5a3fc8-07571fc6a3cbfd-3b634404-100200-172ef9a5a3fc8; _lxsdk=8F2963A0B78111EA801551553EAD9849E8BF317E589D41B68B14B6F443E579CD; _csrf=7fe6b8fd7f6009827c861629fa3a689b692edb874432c829f68b2e076f21b0d2; lt=h31FdelCwTksoMj7EAe6GfOW66IAAAAAAwsAABHGRHJIus4lrdzgqc6NmPYFWzQMpRwonE9iCVPCj4bDjgmFxcCukXMPn2pga014vA; lt.sig=O9K2Yocxjo6gTL1h0Q5XTTHMh8k; mojo-session-id={"id":"b3b43f4d0beea2a1aead937ab9702f63","time":1593966163414}; mojo-trace-id=1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593162021,1593162054,1593964239,1593966163; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593966163; __mta=150738441.1593157769843.1593964355051.1593966163549.18; _lxsdk_s=1731fac1974-ed2-1bf-8ce%7C%7C6'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'maoyanspiders.middlewares.MaoyanspidersSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'maoyanspiders.middlewares.MaoyanspidersDownloaderMiddleware': 543,
#}
DOWNLOADER_MIDDLEWARES = {
    'maoyanspiders.middlewares.MaoyanspidersDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'maoyanspiders.middlewares.RandomHttpProxyMiddleware': 400,

}
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'maoyanspiders.pipelines.MaoyanspidersPipeline': 300,
}
HTTP_PROXY_LIST = [
     'http://95.179.218.202:80',
     'http://61.135.185.111:9090',
]
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
