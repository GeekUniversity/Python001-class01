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
    'Cookie': '__mta=150738441.1593157769843.1593160824465.1593161146500.4; uuid_n_v=v1; uuid=8F2963A0B78111EA801551553EAD9849E8BF317E589D41B68B14B6F443E579CD; _csrf=881c753de6d6a03771df0f24440c46402284b4ae084412209952f35da589d0f4; mojo-uuid=90a5645c0238bb3a951ac59e8fd65d83; mojo-session-id={"id":"7e3d93bc6657c31e418683e2b29017e8","time":1593157769493}; _lxsdk_cuid=172ef9a5a3fc8-07571fc6a3cbfd-3b634404-100200-172ef9a5a3fc8; _lxsdk=8F2963A0B78111EA801551553EAD9849E8BF317E589D41B68B14B6F443E579CD; lt=3vkYTSGMiRVJ99Zoas-CTnwvDXEAAAAA5woAAP0L56xTZWSA-mAli6O0geEhxzYIFV5NlCW10zKHRcTc_XBQ1zEJb1fai41iWWdFjA; lt.sig=0kqbR7qaUc8LVsV_z41gSc9nk30; mojo-trace-id=66; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593160833,1593161667,1593162012,1593162021; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593162021; __mta=150738441.1593157769843.1593161146500.1593162020659.5; _lxsdk_s=172ef9a5a41-f1a-c45-38e%7C%7C93'
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
