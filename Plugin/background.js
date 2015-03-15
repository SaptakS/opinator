chrome.browserAction.onClicked.addListener(
				function(tab)
				{
					chrome.tabs.executeScript(null, {file: "jquery-1.11.2.js"});					
					chrome.tabs.executeScript(null, {file: "script.js"});
						
				});