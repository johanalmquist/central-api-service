import json

import pika
import requests

from ArubaCentral import sites
from inventory import Inventory


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue="new-ap")

    def callback(ch, method, properties, body):
        url = "http://notification:8001/slack/"
        headers = {"Content-Type": "application/json"}
        # Find info about ap from inv
        inv = Inventory()
        device = inv.findDevice(serial=body)
        if device is None:
            return None
        # Find info about site from inv
        site = inv.findSite(site_id=device["site_id"])
        # Get aruba cental site id
        nmess = {"message": sites.findOrCreate(site)}
        requests.post(url=url, data=json.dumps(nmess), headers=headers)

    channel.basic_consume(queue="new-ap", on_message_callback=callback, auto_ack=True)
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    while True:
        main()
