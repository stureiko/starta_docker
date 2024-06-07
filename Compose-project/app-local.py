from flask import Flask, request, jsonify
from datetime import datetime
from netifaces import interfaces, ifaddresses, AF_INET

app = Flask(__name__)


def get_ip():
    ip_addr = {}
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        if addresses != ['No IP addr']:
            ip_addr[ifaceName] = addresses
    return ip_addr


@app.route('/', methods=['GET'])
def last_entry():
    now = datetime.now()
    ip_address = get_ip().__str__()

    return {"now": now, "ip_address": ip_address}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3256)
