from confluent_kafka import Consumer, Producer
from pymongo import MongoClient
from bson.json_util import dumps

def send_to_kafka(document):
    kafka_broker = "localhost:9092"
    kafka_topic = "X"
    producer = Producer({"bootstrap.servers": kafka_broker})
    producer.produce(kafka_topic, value=dumps(document))
    producer.flush()
    print("Sent document to Kafka")

def consume_from_kafka():
    kafka_broker = "localhost:9092"
    kafka_topic = "X"
    consumer_group = "subscriber_group"

    # Kafka Consumer yapılandırması
    consumer_config = {
        'bootstrap.servers': kafka_broker,
        'group.id': consumer_group,
        'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(consumer_config)

    # Kafka topic'ini dinle
    consumer.subscribe([kafka_topic])

    try:
        while True:
            message = consumer.poll(1.0)  # 1 saniye boyunca mesajları bekler
            if message is None:
                continue
            if message.error():
                print("Kafka Consumer hatası: {}".format(message.error()))
                continue

            # Gelen mesajı konsola yazdır
            print("Received message: {}".format(message.value().decode('utf-8')))

    except KeyboardInterrupt:
        pass

    finally:
        consumer.close()

def check_new_documents():
    # MongoDB veritabanı bağlantısı
    client = MongoClient("mongodb://localhost:27017")
    print("Connected to MongoDB")

    # Veritabanı seçimi
    db = client["osfinaldb"]
    print("Selected database: osfinaldb")

    # Koleksiyon seçimi
    collection = db["osfinalcollection"]
    print("Selected collection: osfinalcollection")

    # Tüm belgeleri sorgula
    all_documents = collection.find()
    print("Retrieved all documents from the collection")

    if all_documents.count() == 0:
        print("No new documents.")
        return

    for document in all_documents:
        send_to_kafka(document)
        print("Sent document to Kafka")

if __name__ == "__main__":
    # Üç kopya olarak çalıştır
    for i in range(3):
        print("Starting consumer {}".format(i+1))
        check_new_documents()
        consume_from_kafka()
