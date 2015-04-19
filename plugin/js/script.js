/*
	[*] - On loading the page, it checks whether the regex matches the url of the page.
		  If it does then it calss the function extractUrl() for extracting product code nd sending it to a php file
	[*] - after reviews are extracted and sentiment analysis is done, the addReview() funciton operates.
		  It will display the review to the page.
	[*] - In amazon there can be 2 kinds of product url mainly.
			(i)www.amazon.com/gp/product/<product_code>/
			(ii)www.amazon.com/<product-name>/dp/<product_code>/
		  We design the regex for checking accordingly and while extracting we take this into account.
*/
window.onload = function(){
	
	var url = document.URL;
	var regex_valid = /www.amazon.+\/gp\/product\/\w+\/|www.amazon.+\/.+\/dp\/\w+\//g;	//regex to check whether the url is valid or not
	var n = url.search(regex_valid);

	// search() returns -1 if the url doesnt contain the regex.
	if(n == -1){
		alert("URL Not Valid for review");
		n = 0;
	}

	else if(n != -1){
		//valid url
		extractUrl();		
	}


	//to display the review	
	function addReview(data) {

		// checks if already added. If not added then adds the display
		if(!$('.opinator')[0]) {

			//creating a new div with classname as opinator	
			var div = document.createElement('div');		
			div.className = 'opinator';
						
			//creating a button
			div.innerHTML = '<button value="opinator" style="background: aquamarine;width: 300px;height: 100px;position: relative;left: 35%;top: -5em;opacity: .8;border-radius: 20px;">'+data+'</button>';
			
			//appending it to the exact location.
			$('ul.a-button-list').append(div);
			
		}			
	}


	//extract product code and send it for review scraping and sentiment analysis.
	function extractUrl() {
	  
		var url = document.URL;	  	  
		var extracting_regex = /\/dp\/\w+\/|\/product\/\w+\//g;		//product code extracting regex
		var match = url.match(extracting_regex);					//match extracts the string which matches the regex from the url.
		match = ""+match;
		var pCode = "";

		/*if the extracted string has "product" then the beginning index of the product code in the string match is 9.
		else if it contains "dp" then the beginning index of the product code in the string match is 2.*/
		if(match.match(/product/g)) {
			pCode = match.slice(9, match.length-1);	  	
		} else if(match.match(/dp/g)) {
			pCode = match.slice(4, match.length-1);	  	
		}

		alert(pCode);


		
		//here we put the code to send the product code to driverphp to extract review and do sentiment analysis.
		var posting = $.post( "http://172.19.13.67/opinator/test.php", { product_code : pCode } );

		// Put the results in a div
		posting.done(function( data ) {
			addReview(data);
			//alert("Data Loaded: " + data);
		});
	}
}