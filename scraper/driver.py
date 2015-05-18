from subprocess import call

pID = str(1473605202)
call(['scrapy', 'crawl', 'revscraper', '-a', 'productID=%s' % pID])
