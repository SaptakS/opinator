## opinator
A plugin to do sentiment analysis of reviews in ecommerce website.

##Running Development instance
####Plugin
* The plugin code can be found [here](https://github.com/SaptakS/opinator-plugin)
* Clone the repo to your local machine.
* Go to `chrome://extensions` in your google chrome browser.
* Check the `Developer mode` checkbox.
* Click on `load unpacked extension` and browse to the plugin folder.

####Flask
* Install the [requirements](https://github.com/SaptakS/opinator/blob/master/requirements.txt)
* Run the [run.py](https://github.com/SaptakS/opinator/blob/master/run.py) module. This will start your flask server.

####Sentiment
* Download the stanford corenlp module from [here](http://nlp.stanford.edu/software/corenlp.shtml)
* Unzip it and place it in [analyzer](https://github.com/SaptakS/opinator/tree/master/analyzer).
* Execute `export _JAVA_OPTIONS="-Xmx1024M"` in terminal.
* Run [corenlp.py](https://github.com/SaptakS/opinator/blob/master/analyzer/corenlp.py) module.
* This will start your `json-rpc` server.

####Database
* Make changes to `user` and `pass` in [DB_URI](https://github.com/SaptakS/opinator/blob/master/config.py#L15)
* Create a mysql database named `opinator`
* [Grant all privileges to the user to this database](http://stackoverflow.com/questions/5016505/mysql-grant-all-privileges-on-database/5016587#5016587)
* Run [createdb.py](https://github.com/SaptakS/opinator/blob/master/createdb.py)
