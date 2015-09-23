from requests import post
import json

class scraperPipeline(object):

    def process_item (self, item, spider):
        with open("%s.txt" % str(item['file_']), "a") as a:
            a.write(str(item['reviews']))
        return item
