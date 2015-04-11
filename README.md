# opinator
A plugin to do sentiment analysis of reviews in ecommerce website.

# OpinatorScraper
Scrapes reviews from ecommerce websites.

The project uses Scrapy to scrape data from ecommerce websites.

## Functioning of the project
###Plugin Module
* The background.js ensures that on creating a new tab or updating the url of the new tab, the script.js for
  extracting product code is run.
* The script.js file checks whether the url of the current tab matches the regular expression to be a valid product page of Amazon.
  It then extracts the product code and sends it to DriverPHP.php of Review Extraction Module for review scraping and sentiment analysis.
* On returning sentiment analysis, script.js prints the sentiment on the product page.
###Review Extraction Module
* DriverPHP.php executes the ScrapyDriver_AmazonSpider.py, giving ProductID of the product as command line
  argument.
* DriverPHP.php will decide which "Spider" to call based on the url and the
  corresponding "ScrapyDriver" file would be executed.
* ScrapyDriver_AmazonSpider.py executes the "Spider" through command line.

### Scrapy version: 0.24.0
