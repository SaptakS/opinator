import json
# from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
import jsonrpclib
#from pprint import pprint

VALUES = {'Neutral': 0, 'Positive': 1, 'Negative': -1, 'Very negative': -2, 'Very positive': 2}
class StanfordNLP:
    def __init__(self, port_number=8080):
        self.server = jsonrpclib.Server("http://localhost:%d" % port_number)

    def parse(self, text):
        return json.loads(self.server.parse(text))
'''
nlp = StanfordNLP()
#x ='Just got Intex Aqua Trend (Champagne) delivered in the evening... Delivery was prompt, packing was good. NOTE: bought it as a proud indian buying indian company phone... Intex you advertise Grand Features but its very poor quality...you let us down. Seriously I am not blindly criticising... did your team test the product or you are blindsiding customers. Does really makes you wonder if its worth buying products on the Web or its better to See, Test and Buy at regular retailers. Now coming to the Phone... Started exploring few of important features mainly one. DISPLAY: Is it really HD quality. CAMERA: I am not very happy with its supposed to be Sony 13mp Rear Camera Surprised at poor quality of the photos. Does it really have Sony Camera and that too 13MP ?? And the HD Video leaves you wondering what is HD and what is not. FM Radio: Its also pathetic... as instructed with earphone plugged in... it does not pick the stations accurately (some are missed out) and also you need to keep moving around for the stations to sound clear... it reminds you of old childhood times when we used to have Transistor Radios where we had to keep moving around for those AM stations to sound clear, when ever there was change of wind. I will still try and see if some tweaks need to be done to set it right... if not I will return the phone or throw it out if Amazon does not accept the return. And I will update the review later what ever the outcome.'
#x = 'This is a good product'
#x = 'Amazing phone run Smoothly on Lolopop.Camera also good. No laging. Display is very sharp.'

x = 'Its look another good product from home grown handset manufacturer INTEX. Another addition on their 4G segment. Display look superb.Camera quality is good. 3000 mAh battery really good. 4G LTE really working. Full of new features (Flip mute, Air shuffle,HoT Knot & more)'
results = nlp.parse(x)
results = results['sentences']
#pprint (results)
value = 0
count = 0
for result in results:
    count += 1
    #print result['sentiment']
    value = value + VALUES[result['sentiment']]
value = int(value / count)

if value < 0:
    result = 'Negative'
elif value > 0:
    result = 'Positive'
else:
    result = 'Neutral'

#for sentiment, sentiment_value in VALUES.iteritems():
 #   if sentiment_value == value:
  #      result = sentiment

pprint(result)
'''
