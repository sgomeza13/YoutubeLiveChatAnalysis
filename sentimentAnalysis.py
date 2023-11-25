from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kinesis import KinesisUtils, InitialPositionInStream

sc = SparkContext(appName="KinesisExample")
ssc = StreamingContext(sc, 1)  # 1-second batch interval

kinesisStream = KinesisUtils.createStream(
    ssc, "KinesisExample", "LiveYTChat2", "kinesis.us-east-1.amazonaws.com",
    "us-east-1",
    InitialPositionInStream.LATEST, 4  # Number of shards
)

# Process the Kinesis stream
kinesisStream.map(lambda x: x).pprint()

ssc.start()
ssc.awaitTermination()
