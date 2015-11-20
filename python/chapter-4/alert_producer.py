###############################################
# RabbitMQ in Action
# Chapter 4.2.2 - Alerting Server Producer
# 
# Requires: pika >= 0.9.5
# 
# Author: Jason J. W. Williams
# (C)2011

#In [36]:  %run alert_producer.py -m ddd -r critical.xxx
#Sent message "ddd" tagged with routing key 'critical.xxx' to exchange '/'.

#In [37]:  %run alert_producer.py -m yyy -r xxx.rate_limit
#Sent message "yyy" tagged with routing key 'xxx.rate_limit' to exchange '/'.

###############################################
import json, pika
from optparse import OptionParser

#/(asp.0) Read in command line arguments
opt_parser = OptionParser()
opt_parser.add_option("-r",
                      "--routing-key",
                      dest="routing_key",
                      help="Routing key for message (e.g. myalert.im)")
opt_parser.add_option("-m",
                      "--message",
                      dest="message", 
                      help="Message text for alert.")

args = opt_parser.parse_args()[0]

#/(asp.1) Establish connection to broker
creds_broker = pika.PlainCredentials("guest", "guest123")
conn_params = pika.ConnectionParameters("192.168.111.192",
                                        virtual_host = "/",
                                        credentials = creds_broker)
conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()

#/(asp.2) Publish alert message to broker
msg = json.dumps(args.message)
msg_props = pika.BasicProperties()
msg_props.content_type = "application/json"
msg_props.durable = False

channel.basic_publish(body=msg,
                      exchange="alerts",
                      properties=msg_props,
                      routing_key=args.routing_key)

print ("Sent message %s tagged with routing key '%s' to " + \
       "exchange '/'.") % (json.dumps(args.message),
                           args.routing_key)