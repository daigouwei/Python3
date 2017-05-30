//console.log('Hello, world!');
//phantom.exit();

/*var page = require('webpage').create();*/
//page.open('http://cuiqingcai.com', function(status){
    //console.log("Status: "+status);
    //if(status==="success"){
        //page.render('example.png');
    //}
    //phantom.exit();
/*});*/

/*var url = 'http://www.baidu.com';*/
//var page = require('webpage').create();
//page.onConsoleMessage = function(msg){
    //console.log(msg);
//}
//page.open(url, function(status){
    //page.evaluate(function(){
            //console.log(document.title);
    //});
    //phantom.exit();
/*});*/

var page = require('webpage').create();
page.viewportSize = {width:512, height: 250};
page.clipRect = {top:0, left:0, width:512, height:250};
page.open('http://cuiqingcai.com', function(){
    page.render('germy.png');
    phantom.exit();
});
