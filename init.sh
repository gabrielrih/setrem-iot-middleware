#!/bin/sh

( rabbitmqctl wait --timeout 60 $RABBITMQ_PID_FILE ; \
# Enable MQTT plugin
rabbitmq-plugins enable rabbitmq_mqtt ; \
# Creating queue
rabbitmqadmin declare queue name=$MQTT_DEFAULT_TOPIC_NAME durable=true ; \
rabbitmqadmin declare binding source=amq.topic destination_type=queue destination=$MQTT_DEFAULT_TOPIC_NAME routing_key=$MQTT_DEFAULT_TOPIC_NAME ; \
# Create Rabbitmq user
rabbitmqctl add_user $RABBITMQ_USER $RABBITMQ_PASSWORD 2>/dev/null ; \
rabbitmqctl set_user_tags $RABBITMQ_USER administrator ; \
rabbitmqctl set_permissions -p / $RABBITMQ_USER  ".*" ".*" ".*" ; \
echo "*** User '$RABBITMQ_USER' with password '$RABBITMQ_PASSWORD' completed. ***" ; \
echo "*** Log in the WebUI at port 15672 (example: http:/localhost:15672) ***") &

# $@ is used to pass arguments to the rabbitmq-server command.
# For example if you use it like this: docker run -d rabbitmq arg1 arg2,
# it will be as you run in the container rabbitmq-server arg1 arg2
rabbitmq-server $@