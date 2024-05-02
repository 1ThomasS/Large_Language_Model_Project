# importing the required libraries  
from time import sleep  
from json import dumps  
from kafka import KafkaProducer 

# initializing the Kafka producer  
my_producer = KafkaProducer(  
    bootstrap_servers = ['localhost:9092'],  
    value_serializer = lambda x:dumps(x).encode('utf-8')  
    )  
# generating the numbers ranging from 1 to 500  
for n in range(500):  
    my_data = {'num' : n}  
    print('publishing to quickstart-events Topic :'+ str(n))
    my_producer.send('quickstart-events', value = my_data)  
    sleep(1)  
