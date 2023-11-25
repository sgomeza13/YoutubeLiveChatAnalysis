import boto3

kinesis_client = boto3.client('kinesis')

def process_records(records):
    for record in records:
        print('Record: ', record)

def my_consumer():
    shard_id = 'shardId-000000000000'
    iterator = kinesis_client.get_shard_iterator(StreamName='myStream', ShardId=shard_id, StartingPosition='LATEST')['ShardIterator']

    while True:
        response = kinesis_client.get_records(ShardIterator=iterator)
        records = response['Records']

        process_records(records)

        iterator = response['NextShardIterator']

if __name__ == '__main__':
    my_consumer()
