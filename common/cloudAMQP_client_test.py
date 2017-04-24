from cloudAMQP_client import CloudAMQClient

CLOUDAMQ_URL = 'amqp://bqsxgvoa:C6bUAT6qWGjukFAlx__O617evO_-RHiB@sidewinder.rmq.cloudamqp.com/bqsxgvoa'
QUEUE_NAME = 'dataFetcherTaskQueue'


# Initialize a client
client = CloudAMQClient(CLOUDAMQ_URL, QUEUE_NAME)

# send a message

client.sendDataFetcherTask({'name': 'libchaos'})

# Reiveve a message

client.getDataFetcherTask()



