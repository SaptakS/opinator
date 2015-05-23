from os import remove

from corenlp import batch_parse

def sentiment_calculator():
    corenlp_dir = "stanford-corenlp-full-2014-08-27/"
    raw_text_directory = "/var/www/html/opinator/mindwrap/raw_text/"
    parsed = batch_parse(raw_text_directory, corenlp_dir,raw_output=False)  # It returns a generator object
    data = parsed[0]['sentences']
    sentimentSum = 0.0

    for i in xrange(len(data)):
	    sentimentValue = data[i]['sentimentValue']
	    sentimentSum += sentimentValue

    sentimentAvg = float(sentimentSum / len(data))
    print "Sentiment Value: ",sentimentAvg
    if sentimentAvg > 2:
	    sent = 'Positive'
    elif sentimentAvg < 2:
	    sent = 'Negative'
    else:
	    sent = 'Average'

    #os.remove('/var/www/html/opinator/mindwrap/raw_text/new_sample')
    return (sentimentAvg, sent)
