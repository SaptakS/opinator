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

    div.className = 'opinator';

    div.innerHTML = '<input type="button" value="opinator" style="background: aquamarine;width: 300px;height: 100px;position: fixed;left: 35%;top: 30%;font-size: 35px;opacity: .8;border-radius: 20px;"/>';
		
	var elem = document.getElementsByTagName('body');
    elem[0].appendChild(div);
}