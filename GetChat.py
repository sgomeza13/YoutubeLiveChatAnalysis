import pytchat
import boto3

kinesis_client = boto3.client('kinesis', region_name='us-east-1')

#*
comprehend_client = boto3.client('comprehend', region_name='us-east-1')  

def analyze_sentiment(comment):
    response = comprehend_client.detect_sentiment(Text=comment, LanguageCode='en')
    sentiment = response['Sentiment']
    return sentiment


#*

def getLiveData(videoId):
    chat = pytchat.create(video_id=videoId)
    while chat.is_alive():
        for c in chat.get().sync_items():
            #print(f"Video:{videoId} {c.datetime} [{c.author.name}]- {c.message}")
            
            data = {'videoId':videoId,
                    'datetime': c.datetime,
                   'author': c.author.name,
                   'message': c.message}
            
            # # *
            # sentiment = analyze_sentiment(c.message)
            # data['sentiment'] = sentiment
            # # *

            response = kinesis_client.put_record(StreamName='youtube_stream',
                                                 Data=str(data),
                                                 PartitionKey=videoId)
            
            # print(f"Record sent to Kinesis with sequence number: {response['SequenceNumber']}\n ShardId: {response['ShardId']}")
            print("Data to be sent to Kinesis:", data)

            # *
            # Agrega análisis de sentimientos al mensaje después de enviar a Kinesis
            sentiment = analyze_sentiment(c.message)
            data['sentiment'] = sentiment
            
            print(f"Sentiment Analysis for '{c.message}': {sentiment}")

            # *

            