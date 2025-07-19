#!/usr/bin/env python3
# Author:wb-wwb500625
# Create Date:2019/9/10

import os

Params = {
    "server": "192.168.1.102",
    "port": 8000,
    'url': '/assets/report/',
    'request_timeout': 30,
}


PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')
