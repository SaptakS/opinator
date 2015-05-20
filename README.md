## opinator
A plugin to do sentiment analysis of reviews in ecommerce website.

# OpinatorScraper
Scrapes reviews from ecommerce websites.

The project uses Scrapy to scrape data from ecommerce websites.

##Implementing the project
####Plugin
* Go to chrome://extensions in your google chrome browser.
* Check the 'Developer mode' checkbox.
* click on 'load unpacked extension..' and browse to the plugin folder.

####Scrapy
* install the requirements from requirement.txt

####Sentiment Analysis
* install pexpect, xmltodict, unidecode
* download and unzip stanford-corenlp-full-2014-08-27.zip in the scraper folder

If you are on redhat linux please look into your SELinux settings for running JVM 

## Functioning of the project
#### Plugin Module
* The background.js ensures that on creating a new tab or updating the url of the new tab, the script.js for
  extracting product code is run.
* The script.js file checks whether the url of the current tab matches the regular expression to be a valid product page of Amazon.
  It then extracts the product code and sends it to DriverPHP.php of Review Extraction Module for review scraping and sentiment analysis.
* On returning sentiment analysis, script.js prints the sentiment on the product page.

#### Review Extraction Module
* driverPHP.php executes the scrapyDriverFile.py, giving ProductID of the product as command line
  argument.
* scrapyDriverFile.py executes the "Spider" through command line.

### Scrapy version: 0.24.5
