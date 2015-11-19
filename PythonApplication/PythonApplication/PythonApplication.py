###############################################
# RabbitMQ in Action
# Chapter 1 - Hello World Producer
# 
# Requires: pika >= 0.9.5
# 
# Author: Jason J. W. Williams
# (C)2011
###############################################

import pika, sys
from pika import spec
credentials = pika.PlainCredentials("guest", "guest123")
conn_params = pika.ConnectionParameters("192.168.111.192",
                                        credentials = credentials)
conn_broker = pika.BlockingConnection(conn_params) #/(hwp.1) Establish connection to broker


channel = conn_broker.channel() #/(hwp.2) Obtain channel

def confirm_handler(frame): #/(hwppc.1) Publisher confirm handler
    if type(frame.method) == spec.Confirm.SelectOk:
        print "Channel in 'confirm' mode."
    elif type(frame.method) == spec.Basic.Nack:
        if frame.method.delivery_tag in msg_ids:
            print "Message lost!"
    elif type(frame.method) == spec.Basic.Ack:
        if frame.method.delivery_tag in msg_ids:
            print frame.method.delivery_tag,"Confirm received!"
            msg_ids.remove(frame.method.delivery_tag)

#/(hwppc.2) Put channel in "confirm" mode
channel.confirm_delivery(callback=confirm_handler)

msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"

msg_ids = [] #/(hwppc.3) Reset message ID tracker

channel.basic_publish(body=msg,
                      exchange="hello-exchange",
                      properties=msg_props,
                      routing_key="hola") #/(hwppc.4) Publish the message

msg_ids.append(len(msg_ids) + 1) #/(hwppc.5) Add ID to tracking list

channel.close()

#for i in range(1000):
#    channel.basic_publish(body=msg+str(i),
#                          exchange="hello-exchange",
#                          properties=msg_props,
#                          routing_key="hola") #/(hwp.5) Publish the message
#channel.basic_publish(body='quit',
#                          exchange="hello-exchange",
#                          properties=msg_props,
#                          routing_key="hola") #/(hwp.5) Publish the message