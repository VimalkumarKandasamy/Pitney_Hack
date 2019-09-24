
#!/usr/bin/env python
import pika
import json
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello',durable=True)






ss = ["org.pitney.hack.Shipper#SH1","org.pitney.hack.Shipper#SH2","org.pitney.hack.Shipper#SH3","org.pitney.hack.Shipper#SH4","org.pitney.hack.Shipper#SH5"]
tt = ["org.pitney.hack.Shipment#T1","org.pitney.hack.Shipment#T2","org.pitney.hack.Shipment#T3","org.pitney.hack.Shipment#T4","org.pitney.hack.Shipment#T5"]

i=0
j=0
y=0
for y in range(5):
	s=ss[i]
	t=tt[4]
	data = {     "$class": "org.pitney.hack.Shipping",     "shipment": t,    "shipper": s,    "dimension": "100x100",    "weight": "150g"}
	message = json.dumps(data)
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print(message)
	time.sleep(1)
	i=i+1
connection.close()



