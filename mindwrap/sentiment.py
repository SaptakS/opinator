from corenlp import batch_parse
from pprint import pprint
import json

corenlp_dir = "stanford-corenlp-full-2014-08-27/"
raw_text_directory = "raw_text/"
parsed = batch_parse(raw_text_directory, corenlp_dir,raw_output=False)  # It returns a generator object
data = parsed[0]['sentences']
sentimentSum = 0.0

for i in xrange(len(data)):
	pprint(data[i]['sentiment'])
	sentimentValue = data[i]['sentimentValue']
	sentimentSum += sentimentValue

sentimentAvg = float(sentimentSum / len(data))
print sentimentAvg
if sentimentAvg > 2:
	print "Good Product"
elif sentimentAvg < 2:
	print "Bad Product"
else:
	print "Neither good nor bad"
