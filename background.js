chrome.browserAction.onClicked.addListener(
				function(tab)
				{

					//chrome.tabs.executeScript(null, {code:"var url = document.URL;alert(url)"});
					
					chrome.tabs.executeScript(null, {file: "script.js"});
						
				});