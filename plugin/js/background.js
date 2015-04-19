/*
	[*] - init() is the function to iniatialize the details of the current tab.
	[*] - script.js is the file which makes a regex check and extracts the product code from the url.
*/
function init() {

	// set the id of the current tab
	chrome.tabs.query({ lastFocusedWindow: true, active: true }, function (tabs) {
		currentTabId = tabs[0].id;
	});	
	
}

//execute the script when a new url is loaded in the tab or when the page is refreshed
chrome.tabs.onUpdated.addListener(function(activeInfo){
	chrome.tabs.executeScript(null, {file: "js/jquery-1.11.1.js"});
	chrome.tabs.executeScript(null, {file: "js/script.js"});
});

//execute the script when a new tab is created with a url		
chrome.tabs.onCreated.addListener(function(tab) {
	chrome.tabs.executeScript(null, {file: "js/jquery-1.11.1.js"});
	chrome.tabs.executeScript(null, {file: "js/script.js"});
});
