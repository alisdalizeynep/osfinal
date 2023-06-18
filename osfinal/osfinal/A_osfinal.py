from pymongo import MongoClient
from bson.json_util import dumps
from confluent_kafka import Producer
from threading import Thread
import time

# MongoDB veritabanı bağlantısı
client = MongoClient("mongodb://localhost:27017/")
print("Connected to MongoDB")

# Veritabanı seçimi
db = client["programa"]
print("Selected database: programa")

# Koleksiyon seçimi
collection = db["collect"]
print("Selected collection: collect")

# Kafka yapılandırması
kafka_broker = "localhost:9092"
kafka_topic = "X"

def send_to_kafka(document):
    # JSON mesajı olarak dökümanı Kafka'ya gönder
    producer = Producer({"bootstrap.servers": kafka_broker})
    producer.produce(kafka_topic, value=dumps(document))
    producer.flush()
    print("Sent document to Kafka")

def watch_collection_changes():
    last_document_id = None

    while True:
        # Son belge ID'sine göre yeni belgeleri sorgula
        query = {}
        if last_document_id:
            query["_id"] = {"$gt": last_document_id}

        new_documents = collection.find(query)

        for document in new_documents:
            send_to_kafka(document)
            last_document_id = document["_id"]

        time.sleep(10)  # Her 10 saniyede bir sorgulama yap

def main():
    # Collection değişikliklerini izlemek için ayrı bir thread başlat
    thread = Thread(target=watch_collection_changes)
    thread.start()

    # Ana thread uyumlu bir şekilde devam etsin
    thread.join()

if __name__ == "__main__":
    main()
