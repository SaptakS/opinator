## opinator
A plugin to do sentiment analysis of reviews in ecommerce website.

##Implementing the project
####Plugin
* The plugin code can be found [here](https://github.com/SaptakS/opinator-plugin)
* Clone the repo to your local machine.
* Go to chrome://extensions in your google chrome browser.
* Check the `Developer mode` checkbox.
* Click on `load unpacked extension` and browse to the plugin folder.

####Flask
* Install the requirements from [requirements.txt]()
* Run the [run.py]() module. This will start your flask server.

####Sentiment
* Download the stanford corenlp module from [here](http://nlp.stanford.edu/software/corenlp.shtml)
* Unzip it and place it in [mindwrap]().
* Execute `export _JAVA_OPTIONS="-Xmx1024M"` in terminal.
* Run [corenlp.py]() module.

####Database
* Make a mysql user `vivek` with pass `vivek`
* Make a mysql database named `op20`
* [Grant all privileges to the user to this database](http://stackoverflow.com/questions/5016505/mysql-grant-all-privileges-on-database)
* Move the [db_create.py]() to its parent folder, run it and move it back.
