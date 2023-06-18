Bu proje, MongoDB veritabanında belirlenen bir koleksiyonda oluşan yeni dokümanları sorgulayıp
Apache Kafka'ya JSON mesajları üreten ve Kafka'dan gelen mesajları tüketen Python uygulamalarını içermektedir.

-------------------Gereksinimler-------------------
-Python
-pymongo kütüphanesi
-confluent_kafka kütüphanesi
-Apache Kafka
-Docker

Gerekli kütüphaneleri yüklemek için aşağıdaki komutları çalıştırabilirsiniz.
pip install pymongo
pip install confluent-kafka

----------------------Kullanım----------------------

İlgili MongoDB ve Kafka bağlantı yapılandırmalarını gerekli yerlerde güncelleyin.
A_uygulamasi.py dosyası ile, MongoDB'deki yeni dokümanları sorgulayıp ve Kafka'ya JSON mesajları üretin.
B_uygulamasi.py dosyası ile, Kafka'dan gelen mesajları tüketin.

-------------------Katkıda Bulunma-------------------
Bu projeye katkıda bulunmak isterseniz, lütfen CONTRIBUTING.md dosyasını inceleyin ve talimatları takip edin.


------------------------Lisans------------------------
Bu projenin lisansı hakkında daha fazla bilgi için LICENSE.md dosyasını inceleyin.