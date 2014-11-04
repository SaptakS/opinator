var url = document.URL;
var regex = /www.+\/product-reviews\/.+/g;
var n = url.search(regex);

if(n == -1){
	alert("URL Not Valid for review");
}

if(n != -1){
	//alert("valid");
	addButton();
	
	
}
	
function addButton() {
    var div = document.createElement('div');
	
	//creating a new div with classname as opinator
    div.className = 'opinator';
	
	//creating a button
    div.innerHTML = '<input type="button" id="opinator_button" value="opinator" onClick="dispUrl();" style="background: aquamarine;width: 300px;height: 100px;position: fixed;left: 35%;top: 30%;font-size: 35px;opacity: .8;border-radius: 20px;"/>';
	
	//add jquery to page
	var jq = document.createElement('SCRIPT');
	jq.type="text\/javascript";
	document.body.appendChild(jq);
	jq.src='http://code.jquery.com/jquery-1.10.2.js';
	
	//append to the body
	document.body.appendChild(div);
	


//$(#opinator).click(dispUrl());

	var oScript = document.createElement('SCRIPT');
	oScript.innerHTML = 'function dispUrl() {\
							var posting = $.post( "http://172.19.13.132/opinator/test.php", { url: document.URL} );\
							posting.done(function( data ) {\
								alert("Data Loaded:" + data);\
							});\
						}';
	document.body.appendChild(oScript);
}