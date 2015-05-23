## opinator
The back end for a plugin to do sentiment analysis of reviews in ecommerce website.

# OpinatorScraper
Scrapes reviews from ecommerce websites.

The project uses Scrapy to scrape data from ecommerce websites.

##Implementing the project

####Scrapy
* install the requirements from requirement.txt

####Sentiment Analysis
* We use stanford's nlp package temporarily, written in java with a python
  wrapper.
* Download it from here:
    https://bitbucket.org/torotoki/corenlp-python
* If required - install pexpect, xmltodict, unidecode
* Unzip stanford-corenlp-full-2014-08-27.zip in the opinator folder, delete the rest.

* If you are on redhat linux please look into your SELinux settings for running JVM 
* If you get following error: Could not reserve enough space for object heap
    type in following command in the terminal: export _JAVA_OPTIONS="-Xmx256M"

## Functioning of the project
* driver.py file handles the whole backend of the project.
* The plugin code is expected to send product_id, website_name(in a particular
  format) and the review page url.
* The data from plugin is received in the driver file and it is first checked
  if the product is already in the database and is not 'outdated'. (not
    implemented yet)
* If not outdated, just send the sentiment to plugin and exit.
* Otherwise, scraper is run and the reviews are placed in
  /opinator/mindwrap/raw_text/new_sample.
* Then, to run the SA, sentiment_calculator is run. It returns the sentiment
  score and the sentiment.
* Send the sentiment to the plugin (not implemented yet)
* Insert/Update the database.

#### Review Extraction Module
* We use Python' Scrapy framework for review extraction.
* For each website, different spider will run
* The driver will decide which spider to run and corresponding shell cmd will
  be executed.
* Whatever data the scraper requires (product id and/or url), is passed through
  CLI arguments.
