import boto3
import os
from dotenv import load_dotenv


load_dotenv()




stream_name = os.environ['STREAM_NAME']
shard_id = os.environ['SHARD_ID']
starting_position = os.environ['STARTING_POSITION']

kinesis_client = boto3.client('kinesis', region_name='us-east-1')

def process_records(records):
    for record in records:
        print('Record: ', record)

def my_consumer():
    iterator = kinesis_client.get_shard_iterator(
        StreamName=stream_name,
        ShardId=shard_id,
        StartingPosition=starting_position
    )['ShardIterator']

    while iterator:
        try:
            response = kinesis_client.get_records(ShardIterator=iterator)
            records = response['Records']

            if not records:
                break  

            process_records(records)

            iterator = response['NextShardIterator']

        except Exception as e:
            print(f"Error: {e}")
           

if __name__ == '__main__':
    my_consumer()
