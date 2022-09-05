from datetime import datetime
import ssl
import socket
import urllib3
import json

DAYSLEFT = 5
DOMAINS = [
    # Here goes list of domains
]
webhook = (
    # Here goes slack webhook address
)
dateFormat = "%b %d %H:%M:%S %Y %Z"


def lambda_handler(event, context):
    check_domain()
    return {"message": "Function executed successfully"}


def send_message(payload):
    http = urllib3.PoolManager()
    type = "POST"
    headers = {"Content-Type": "application/json"}
    url = webhook
    encodedData = json.dumps(payload)
    r = http.request(type, url, headers=headers, body=encodedData)


def check_domain():
    for domain in DOMAINS:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as server:
            try:
                server.connect((domain, 443))
                cert = server.getpeercert()
            except:
                message = "Unable to retreive certificate data for {}".format(domain)
                payload = {"text": message}
                send_message(payload)
                continue

        expTime = datetime.strptime(cert["notAfter"], dateFormat)
        now = datetime.today()
        daysLeft = (expTime - now).days
        message = "Certificate for {} will expire in {} days!".format(domain, daysLeft)
        payload = {"text": message}
        if daysLeft < DAYSLEFT:
            send_message(payload)
