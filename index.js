var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var Datastar = require('datastar');

var datastar = new Datastar({
  config: {
    user: 'scylla',
    password: 'scylla',
    cqlVersion: '3.0.0',
    consistencyLevel: 'one',
    keyspace: 'fci',
    hosts: ['127.0.0.1: 9042']}
}).connect();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));

var dogRoutes = require('./routes/dog_routes')(app, datastar);

var server = app.listen(3000, function () {
    console.log('Server running at http://127.0.0.1:3000/');
});
