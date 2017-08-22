var express = require('express');
var bodyParser = require("body-parser");
var app = express();

var bodyParser = require('body-parser')
app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
})); 

app.get('/', function (req, res) {
  res.send('Hello World!');
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});

app.post('/login', function(req,res) {
	console.log('coucou')
	var name = req.body.name,
	hpMax = req.body.hpMax,
	hp = req.doby.hp,
	attack = req.body.attack,



	Objects = req.body,Objects;


	res.send(name,hpMax,hp,attack,Objects)
	console.log(name);
	console.log(Objects);
});

