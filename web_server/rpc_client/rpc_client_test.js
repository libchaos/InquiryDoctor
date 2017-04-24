const client = require('./rpc_client');

console.log(client.add)

client.add(1, 2, function(response) {
  console.log(`1 + 2 = ${response}`);
})