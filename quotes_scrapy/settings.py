BOT_NAME = "quotes_scrapy"

SPIDER_MODULES = ["quotes_scrapy.spiders"]
NEWSPIDER_MODULE = "quotes_scrapy.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure a delay for requests (default: 0)
DOWNLOAD_DELAY = 2

# Default headers for requests
DEFAULT_REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}

# Enable/disable extensions
EXTENSIONS = {
    "scrapy.extensions.telnet.TelnetConsole": None,
}

# Enable or disable pipelines

# Enable and configure the AutoThrottle extension (disabled by default)
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
