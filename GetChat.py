import pytchat
import boto3

kinesis_client = boto3.client('kinesis', region_name='us-east-1')


def getLiveData(videoId):
    chat = pytchat.create(video_id=videoId)
    while chat.is_alive():
        for c in chat.get().sync_items():
            #print(f"Video:{videoId} {c.datetime} [{c.author.name}]- {c.message}")
            
            data = {'videoId':videoId,
                    'datetime': c.datetime,
                   'author': c.author.name,
                   'message': c.message}
            response = kinesis_client.put_record(StreamName='LiveYTChat',
                                                 Data=str(data),
                                                 PartitionKey=videoId)
            
            print(f"Record sent to Kinesis with sequence number: {response['SequenceNumber']}")
            