
var url = document.URL;
var regex = /www.+\/product-reviews\/.+/g;
var n = url.search(regex);

if(n == -1){
	alert("URL Not Valid for review");
}

if(n != -1){
	//alert("valid");
	dispUrl();
	
	
}
	
function addButton(data) {
    
	if(!$('.opinator')[0]) {
	
	var div = document.createElement('div');
	
	//creating a new div with classname as opinator
    div.className = 'opinator';
	
	//creating a button
    div.innerHTML = '<button value="opinator" style="background: aquamarine;width: 300px;height: 100px;position: fixed;left: 35%;top: 30%;opacity: .8;border-radius: 20px;">'+data+'</button>';
	
	//append to the body
	document.body.appendChild(div);
	}
		
}

function dispUrl() {
  // Send the data using post
  var obj = [];
  var url = document.URL;
  var tmp = { 'url' : url };
  obj.push(tmp);
  var jsonObj = JSON.stringify(obj)
  var posting = $.post( "http://172.19.12.176/opinator/test.php", { json : jsonObj } );
 
  // Put the results in a div
  posting.done(function( data ) {
	addButton(data);
    //alert("Data Loaded: " + data);
  });
}