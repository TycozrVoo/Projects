import websocket
import json
import time
import threading

"""
A Discord Gateway Client written in Python. See discord_gateway_client.js for a JavaScript version.
"""

def get_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)

def send_json(ws, data):
    ws.send(json.dumps(data))

def do_heartbeat(ws, interval):
    print("heartbeat starting")
    while True:
        time.sleep(interval)
        payload = {
            "op": 1,
            "d": "null"
        }
        send_json(ws, payload)
        print("heartbeat sent")

def start(token):
    ws = websocket.WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=6&encoding=json")
    
    initial = get_response(ws)
    heartbeat_interval = initial['d']['heartbeat_interval'] / 1000
    threading._start_new_thread(do_heartbeat, (ws, heartbeat_interval))

    payload = {
            'op': 2,
            'd': {
                'token': token,
                "properties": {
                    "$os": "windows",
                    "$browser": "chrome",
                    "$device": "pc"
                }
            }
        }
    send_json(ws, payload)

    while True:
        try:
            event = get_response(ws)

            print(f"{event['d']['author']['username']}#{event['d']['author']['discriminator']}: {event['d']['content']}")
            with open("debug.json", "w+") as f:
                f.write(json.dumps(event))
        except:
            pass
