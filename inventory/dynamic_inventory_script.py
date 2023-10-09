#!/usr/bin/env python

import json

inventory = {
    'web': {
        'hosts': ['webserver1.example.com', 'webserver2.example.com'],
        'vars': {}
    },
    'db': {
        'hosts': ['dbserver1.example.com'],
        'vars': {}
    },
    '_meta': {
        'hostvars': {}
    }
}

print(json.dumps(inventory))
