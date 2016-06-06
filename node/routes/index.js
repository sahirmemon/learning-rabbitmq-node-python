var express = require('express');
var router = express.Router();

var amqp = require('amqplib/callback_api');

/* GET home page. */
router.get('/', function(req, res, next) {

  // Connect to RabbitMQ server
  amqp.connect('amqp://localhost', function(err, conn) {

    // Create a channel
    conn.createChannel(function(err, ch) {

      // Create a queue to send messages to
      var q = 'hello';

      ch.assertQueue(q, {durable: false});
      ch.sendToQueue(q, new Buffer(JSON.stringify({message:'LOL', action:'TOUCH'})));
      console.log(" [x] Send 'Hello World!'");

      // Close the connection
      setTimeout(function() { conn.close(); }, 500);
    });
  });








  res.render('index', { title: 'Express' });
});

module.exports = router;
