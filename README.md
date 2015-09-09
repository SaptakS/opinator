## opinator
A plugin to do sentiment analysis of reviews in ecommerce website.

##Implementing the project
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
* Unzip it and place it in [mindwrap](https://github.com/SaptakS/opinator/tree/master/mindwrap).
* Execute `export _JAVA_OPTIONS="-Xmx1024M"` in terminal.
* Run [corenlp.py](https://github.com/SaptakS/opinator/blob/master/mindwrap/corenlp.py) module.
* This will start your `json-rpc` server.

####Database
* You can skip the next point if you can make changes to [DB_URI](https://github.com/SaptakS/opinator/blob/master/config.py#L15)
* Create a mysql user `vivek` with pass `vivek`
* Create a mysql database named `op20`
* [Grant all privileges to the user to this database](http://stackoverflow.com/questions/5016505/mysql-grant-all-privileges-on-database)
* Move the [db_create.py](https://github.com/SaptakS/opinator/blob/master/database/db_create.py) to its parent folder, run it and move it back.
