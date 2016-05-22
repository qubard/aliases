var express = require('express');
var bodyParser = require('body-parser');
var pythonShell = require('python-shell');
var app = express();

app.use(express.static('static'));
app.use(bodyParser.urlencoded());
app.use(bodyParser.json());

app.get('/', function (req, res) {
	res.sendFile('index.html');
});

app.post('/',  function (req, res) {
    pythonShell.run('aliases.py', {args: [req.body.text, req.body.name]}, function(err, results){
        if(err) { console.log(err); res.send(['Oops, something went wrong.']) }
        res.send(results);
    });
});

var server = app.listen(80);