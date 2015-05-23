from sys import path
from subprocess import Popen
#from cgi import FieldStorage

sys.path[:0] = ['/var/www/html/opinator/database', '/var/www/html/opinator/mindwrap']

from dbdriver import driver
from sentiment import sentiment_calculator

def drive():

    """
    data = FieldStorage()
    product_id = str(data.getvalue('product_code'))
    website_name = str(data.getvalue('website'))
    url = str(data.getvalue('url'))
    """
    
    # The below variables are for testing purpose, the actual data has to come
    # from plugin
    product_id = 'B00VEB055E'
    website_name = 'AmazonIN'
    url = 'http://www.amazon.in/gp/product/B00VEB055E/ref=s9_ri_gw_g23_i2?pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=center-3&pf_rd_r=0X4SSMGC8SMPYGX1QV2P&pf_rd_t=101&pf_rd_p=609217867&pf_rd_i=1320006031'
    status, sentiment = driver(website_name=website_name, product_id=product_id, action='query')

    update_flag = 0
    if status == 'outdated':
        print 'outdated'
        update_flag = 1
    elif status == 'present':
        print 'already present in db'
        print 'sentiment:', sentiment
        exit()
        # return 'sentiment' to plugin code
    elif status == 'absent':
        print 'new product'
        # this implies the product is new

    """
    p = Popen(['scrapy', 'crawl', '-a', 'product_id=%s' % product_id , 'revscraper'], cwd='/var/www/html/opinator/scraper')
    p.wait()
    print 'Scraper working'
    """
    sentiment_score, sentiment = sentiment_calculator()
    print 'sentiment_score:', sentiment_score
    print 'sentiment:', sentiment

    #################
    # code to return sentiment to the plugin goes here
    ################

    # update the database
    if update_flag == 1:
        driver(website_name=website_name, product_id=product_id, action='update', url=url,
                sentiment_score=sentiment_score, sentiment=sentiment)
        print 'updated'
        return
    else:
        driver(website_name=website_name, product_id=product_id, action='insert', url=url,
                sentiment_score=sentiment_score, sentiment=sentiment)
        print 'inserted'
        return

drive()
