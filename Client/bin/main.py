#!/usr/bin/env python3
# Author:wb-wwb500625
# Create Date:2019/9/10

import os
import sys


BASE_DIR = os.path.dirname(os.getcwd())

sys.path.append(BASE_DIR)

from core import handler

if __name__ == '__main__':

    handler.ArgvHandler(sys.argv)