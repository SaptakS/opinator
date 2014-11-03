chrome.browserAction.onClicked.addListener(
				function(tab)
				{
					
					
					//chrome.tabs.executeScript(null, {code:"var url = document.URL;alert(url)"});
					
					
					
					chrome.tabs.executeScript(null, {file: "script.js"});
					
					
					//chrome.tabs.executeScript(null, {code:"var elem = document.getElementsByClassName('header');elem[0].style.display='none'"});
					
					/*chrome.tabs.executeScript(null, {code:"var url = document.URL;alert(url);"});
					chrome.tabs.executeScript(null, {code:"var regex = /www.flipkart.com\/.+\/product-reviews.+/g;"});
					chrome.tabs.executeScript(null, {code:"var n = url.search(regex);alert(n);"});
					chrome.tabs.executeScript(null, {code:"if(url.search(regex) != -1) { alert('yes');}else {alert('no');}"});*/
					
				});