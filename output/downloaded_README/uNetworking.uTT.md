<div align="center"><img src="µTT.png"/></div>

µTT ("microTT") is a lightweight and efficient MQTT broker designed to raise the bar for pub/sub performance. It significantly outperforms emqtt, Redis, HiveMQ, Mosquitto, RabbitMQ, Mosca and many others. Memory usage per connection is also significantly lower as it builds on the networking foundation developed for µWebSockets.

Read more about MQTT [here](http://mqtt.org/), find client libraries [here](http://www.hivemq.com/mqtt-client-library-encyclopedia).

### Vendor-neutral, minimal & efficient pub/sub
Below is a simple Node.js example using MQTT.js:
```javascript
var mqtt = require('mqtt');

// connect to the broker
var client = mqtt.connect('mqtt://localhost');

client.on('connect', (err, granted) => {
  // subscribe to all temperature sensors
  client.subscribe('sensors/+/temperature', () => {
    // publish some temperature numbers
    client.publish('sensors/house/temperature', '21');
    client.publish('sensors/sauna/temperature', '107');
  });
});

client.on('message', (topic, message) => {
  // receive our numbers
  console.log(topic + ': ' + message.toString() + ' Celcius');
});
```

### Compilation
The broker and matching benchmark can be compiled with a C++17 compiler using make on Linux:

```
git clone --recursive https://github.com/uNetworking/uTT.git
make
```

Both broker and benchmark are in a *very* experimental and broken state currently. This is all highly unstable and incomplete right now.

### Benchmarks
A simple & automatic broadcasting benchmark has been developed to determine roughly the publishing performance of a few brokers under varying burst load. It supports both MQTT and Redis protocols to allow comparison with Redis (which has shown to be a good reference at small broadcasts).

<div align="center"><img src="benchmarks/averaged.png"/></div>

* HiveMQ is proprietary and limited to 25 connections in demo mode. I was to receive a full test version but was later denied this when they realized I was posting benchmark results.

<div align="center"><img src="benchmarks/redis.png"/></div>

* Results in text form can be found in the `benchmark_results` file.
