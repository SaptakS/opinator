## opinator
The back end for a plugin to do sentiment analysis of reviews in ecommerce website.

# OpinatorScraper
Scrapes reviews from ecommerce websites.

The project uses Scrapy to scrape data from ecommerce websites.

##Implementing the project

####Scrapy
* install the requirements from requirement.txt

####Sentiment Analysis
* install pexpect, xmltodict, unidecode
* download and unzip stanford-corenlp-full-2014-08-27.zip in the scraper folder

If you are on redhat linux please look into your SELinux settings for running JVM 

## Functioning of the project

#### Review Extraction Module
* driverPHP.php executes the scrapyDriverFile.py, giving ProductID of the product as command line
  argument.
* scrapyDriverFile.py executes the "Spider" through command line.

