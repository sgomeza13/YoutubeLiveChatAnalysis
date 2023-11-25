import boto3
import os
from dotenv import load_dotenv


load_dotenv()




stream_name = os.environ['STREAM_NAME']
shard_id = os.environ['SHARD_ID']
starting_position = os.environ['STARTING_POSITION']

kinesis_client = boto3.client('kinesis')

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
                break  # Exit the loop if there are no more records

            process_records(records)

            iterator = response['NextShardIterator']

        except Exception as e:
            print(f"Error: {e}")
            # Handle the error appropriately, e.g., back off and retry

if __name__ == '__main__':
    my_consumer()
