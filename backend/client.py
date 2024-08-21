import requests 
import json 

url = "http://127.0.0.1:5000/" # IP ran from server.py

### SAMPLE PAYLOADS ###

windows = {
  "hello": {
    "os_type": "Windows",
    "version": {
      "Semantic": [
        10,
        0,
        22621
      ]
    },
    "edition": "Windows 11 Professional",
    "codename": 'null',
    "bitness": "X64"
  },
  "id": "2bbb0b82-9092-4dec-b40c-e96ffb1a9ee5",
  "timestamp": "2023-02-26T19:12:46.121185400Z"
}

linux = {
  "hello": {
    "os_type": "Ubuntu",
    "version": {
      "Custom": "22.04"
    },
    "edition": 'null',
    "codename": "jammy",
    "bitness": "X64"
  },
  "id": "79d8e9ab-350a-4cd2-0183-799923d75d24",
  "timestamp": "2023-02-26T19:16:02.479478032Z"
}

status = {
  "battery": {
    "has_battery": 'true',
    "percent": 93
  },
  "id": "2bbb0b82-9092-4dec-b40c-e96ffb1a9ee5",
  "timestamp": "2023-03-01T01:24:15.895800500Z"
}

# Runs a while loop for testing different preset json dumps
while True:
    print("1. Windows hello\n2. Linux hello\n3. Status Update\n")
    test = input()
    if (test == '1'):
        json = windows
    elif (test == '2'):
        json = linux
    elif (test == '3'):
        json = status
    print(f"SENDING PAYLOAD {json}")
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, json=json, headers=headers)