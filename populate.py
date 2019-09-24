
#!/usr/bin/env python
import pika
import json
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello',durable=True)


'''

#populate Authority

data = { "$class": "org.pitney.hack.Authority",  "authority_id": "Authority1",  "business": "Pitney Bowes"}
message = json.dumps(data)
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(message)
time.sleep(1)
connection.close()

#populate Customer

'''
vn = ["C1","C2","C3","C4","C5"]
mm = ["SACHIN","ARAVIND","KUMAR","SHIVA","LAKSMAN"]
ll=["org.pitney.hack.Locations#COIMBATORE","org.pitney.hack.Locations#CHENNAI","org.pitney.hack.Locations#BANGALORE","org.pitney.hack.Locations#SALEM","org.pitney.hack.Locations#TRICHY"]

i=0
j=0
y=0
for y in range(5):
	v=vn[i]
	m=mm[i]
	ii=ll[i]
	data = { "$class": "org.pitney.hack.Customer", "customer_id": v, "customer_name": m, "location": ii }
	message = json.dumps(data)
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print(message)
	time.sleep(1)
	i=i+1
connection.close()

'''
#populate Deliverperson


vn = ["D1","D2","D3","D4","D5"]
mm = ["FEDEX","FEDEX","DELHIVERY","DELHIVERY","ECOMEXPRESS"]
ll=["org.pitney.hack.Locations#COIMBATORE","org.pitney.hack.Locations#CHENNAI","org.pitney.hack.Locations#BANGALORE","org.pitney.hack.Locations#SALEM","org.pitney.hack.Locations#TRICHY"]

i=0
j=0
y=0
for y in range(5):
	v=vn[i]
	m=mm[i]
	ii=ll[i]
	data = { "$class": "org.pitney.hack.Delivery_person", "d_person_id": v, "firm_name": m, "remarks": "good", "location": ii }
	message = json.dumps(data)
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print(message)
	time.sleep(1)
	i=i+1
connection.close()


#populate locations
vn = ["COIMBATORE","CHENNAI","BANGALORE","SALEM","TRICHY"]
mm = ["10.9959N76.9670E","13.0827N80.2707E","12.9716N77.5946E","11.6643N78.1460E","10.7905N78.7047E"]
ll=["COIMBATORE","CHENNAI","BANGALORE","SALEM","TRICHY"]

i=0
j=0
y=0
for y in range(5):
	v=vn[i]
	m=mm[i]
	ii=ll[i]
	data = { "$class": "org.pitney.hack.Locations", "location_code": v, "gps_coordinates": m , "address": ii}
	message = json.dumps(data)
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print(message)
	time.sleep(1)
	i=i+1
connection.close()


#populate product
vn = ["P1","P2","P3","P4","P5"]
mm = ["100","200","300","400","500"]
ll=["org.pitney.hack.Seller#S1","org.pitney.hack.Seller#S2","org.pitney.hack.Seller#S3","org.pitney.hack.Seller#S4","org.pitney.hack.Seller#S5"]

i=0
j=0
y=0
for y in range(5):
	v=vn[i]
	m=mm[i]
	ii=ll[i]
	data = { "$class": "org.pitney.hack.Product", "product_id": v, "price": m, "dimension": "100x100mm",  "type": "glass", "weight": "100gm", "seller": ii}
	message = json.dumps(data)
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print(message)
	time.sleep(1)
	i=i+1
connection.close()



#populate seller
vn = ["S1","S2","S3","S4","S5"]
mm = ["SELLERINDIA","POORVIKA","CHENNAISELLERS","SHOPPERS","ECART"]
ll=["org.pitney.hack.Locations#COIMBATORE","org.pitney.hack.Locations#CHENNAI","org.pitney.hack.Locations#BANGALORE","org.pitney.hack.Locations#SALEM","org.pitney.hack.Locations#TRICHY"]

i=0
j=0
y=0
for y in range(5):
	v=vn[i]
	m=mm[i]
	ii=ll[i]
	data = { "$class": "org.pitney.hack.Seller",  "seller_id": v,  "company_name": m,     "location": ii}
	message = json.dumps(data)
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print(message)
	time.sleep(1)
	i=i+1
connection.close()




#populate shipment
vn = ["T1","T2","T3","T4","T5"]


i=0
j=0
y=0
for y in range(5):
	v=vn[i]
	data = { "$class": "org.pitney.hack.Shipment","tracking_id": v,  "order": "org.pitney.hack.Order#O1","status": "Good", "service_type": "FEDEX", "packaging_time": "1 hour", "no_of_pieces": "2",    "dimension": "100x100",   "weight": "150g",  "shipper": "org.pitney.hack.Shipper#SH1"}
	message = json.dumps(data)
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print(message)
	time.sleep(1)
	i=i+1
connection.close()






#populate order
vn = ["O101","O201","O301","O401","O501"]
mm = ["org.pitney.hack.Customer#C1","org.pitney.hack.Customer#C2","org.pitney.hack.Customer#C3","org.pitney.hack.Customer#C4","org.pitney.hack.Customer#C5"]
ll=["org.pitney.hack.Locations#COIMBATORE","org.pitney.hack.Locations#CHENNAI","org.pitney.hack.Locations#BANGALORE","org.pitney.hack.Locations#SALEM","org.pitney.hack.Locations#TRICHY"]
ss = ["org.pitney.hack.Seller#S1","org.pitney.hack.Seller#S2","org.pitney.hack.Seller#S3","org.pitney.hack.Seller#S4","org.pitney.hack.Seller#S5"]
pp = ["org.pitney.hack.Product#P1","org.pitney.hack.Product#P2","org.pitney.hack.Product#P3","org.pitney.hack.Product#P4","org.pitney.hack.Product#P5"]
i=0
j=0
y=0
for y in range(5):
	v=vn[i]
	m=mm[i]
	ii=ll[i]
	s=ss[i]
	p=pp[i]
	data = {     "$class": "org.pitney.hack.Order",    "order_id": v,    "customer": m,    "product": p,     "seller": s,     "location": ii}
	message = json.dumps(data)
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print(message)
	time.sleep(1)
	i=i+1
connection.close()





#populate Shipper
vn = ["SH1","SH2","SH3","SH4","SH5"]
ll=["org.pitney.hack.Locations#COIMBATORE","org.pitney.hack.Locations#CHENNAI","org.pitney.hack.Locations#BANGALORE","org.pitney.hack.Locations#SALEM","org.pitney.hack.Locations#TRICHY"]
tt = ["org.pitney.hack.Transport#Tp1","org.pitney.hack.Transport#Tp2","org.pitney.hack.Transport#Tp3","org.pitney.hack.Transport#Tp4","org.pitney.hack.Transport#Tp5"]
ww = ["org.pitney.hack.Warehouse#W1","org.pitney.hack.Warehouse#W2","org.pitney.hack.Warehouse#W3","org.pitney.hack.Warehouse#W4","org.pitney.hack.Warehouse#W5"]
i=0
j=0
y=0
for y in range(5):
	v=vn[i]
	ii=ll[i]
	t=tt[i]
	w=ww[i]
	data = {     "$class": "org.pitney.hack.Shipper",     "shipper_id": v,     "transport": t,     "location": ii,     "no_of_carriers": "10",     "return_policy": "na",     "warehouse": w,     "pricing_policy": "na",     "transit_time": "na"}
	message = json.dumps(data)
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print(message)
	time.sleep(1)
	i=i+1
connection.close()

#populate Transport
vn = ["Tp1","Tp2","Tp3","Tp4","Tp5"]
ll=["LIC10111","LIC10112","LIC10113","LIC10114","LIC10115"]

i=0
j=0
y=0
for y in range(5):
	v=vn[i]
	ii=ll[i]
	data = {     "$class": "org.pitney.hack.Transport",     "carrier_id": v,    "transportation_mode": "road",    "driver_id": ii,    "capacity": "10"}
	message = json.dumps(data)
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print(message)
	time.sleep(1)
	i=i+1
connection.close()



#populate WareHouse
vn = ["W1","W2","W3","W4","W5"]
ll=["org.pitney.hack.Locations#COIMBATORE","org.pitney.hack.Locations#CHENNAI","org.pitney.hack.Locations#BANGALORE","org.pitney.hack.Locations#SALEM","org.pitney.hack.Locations#TRICHY"]

i=0
j=0
y=0
for y in range(5):
	v=vn[i]
	ii=ll[i]

	data = {     "$class": "org.pitney.hack.Warehouse",     "warehouse_id": v,     "capacity": "10",     "security": "CAM",     "location": ii}
	message = json.dumps(data)
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print(message)
	time.sleep(1)
	i=i+1
connection.close()
'''

