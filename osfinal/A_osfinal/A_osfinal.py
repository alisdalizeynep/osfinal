from pymongo import MongoClient
from confluent_kafka import Producer
from bson.json_util import dumps
import time
from confluent_kafka.admin import AdminClient, NewTopic

# MongoDB veritabanı bağlantısı
client = MongoClient("mongodb://localhost:27017")
print("Connected to MongoDB")

# Veritabanı seçimi
db = client["osfinaldb"]
print("Selected database: osfinaldb")

# Koleksiyon seçimi
collection = db["osfinalcollection"]
print("Selected collection: osfinalcollection")

# Kafka yapılandırması
kafka_broker = "localhost:9092"
kafka_topic = "X"

def send_to_kafka(document):
    # JSON mesajı olarak dökümanı Kafka'ya gönder
    producer = Producer({"bootstrap.servers": kafka_broker})
    producer.produce(kafka_topic, value=dumps(document))
    producer.flush()
    print("Sent document to Kafka")

def check_new_documents():
    # Tüm belgeleri sorgula
    all_documents = collection.find()
    print("Retrieved all documents from the collection")

    # Yeni belgeleri Kafka'ya gönder
    for document in all_documents:
        send_to_kafka(document)

def create_topic():
    admin_client = AdminClient({"bootstrap.servers": kafka_broker})

    # Define the topic configuration
    topic_config = {
        "cleanup.policy": "delete",
        "compression.type": "gzip",
        "retention.ms": "86400000"
    }

    # Create the topic
    new_topic = NewTopic(kafka_topic, num_partitions=1, replication_factor=1, config=topic_config)
    admin_client.create_topics([new_topic])

    print("Topic created")

def main():
    create_topic()  # Kafka'da konu oluştur
    print("Topic created")
    while True:
        check_new_documents()
        print("Checked for new documents")
        time.sleep(10)  # 10 saniye bekle

if __name__ == "__main__":
    main()
