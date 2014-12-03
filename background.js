chrome.browserAction.onClicked.addListener(
				function(tab)
				{

					//to execute a script on clicking the plugin					
					chrome.tabs.executeScript(null, {file: "script.js"});
						
				});