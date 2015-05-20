class revscraperPipeline(object):
    """ Pipeline to a txt file """
    def process_item(self, item, spider):
        reviews = item['reviews']
        fp = open ("/var/www/html/opinator/mindwrap/raw_text/new_sample", 'a+')
        for i in reviews:
            fp.writelines([str(i), '\n'])
        return item
