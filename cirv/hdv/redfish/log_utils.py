##############################################################################
# Copyright (c) 2020 China Mobile Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################
"""
define the LOGGER settings
"""
import logging
import sys

BASE_DIR = sys.path[0]
LOG_FILE = BASE_DIR + "/" + "logs" + "/" + 'hdv.log'

LOGGER = logging.getLogger("redfish")
LOGGER.setLevel(logging.DEBUG)

FORMATTER = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] \
    - %(funcName)s - %(levelname)s: %(message)s')

FILE = logging.FileHandler(filename=LOG_FILE, mode='w')
FILE.setLevel(logging.DEBUG)
FILE.setFormatter(FORMATTER)

CONSOLE = logging.StreamHandler()
CONSOLE.setLevel(logging.DEBUG)
CONSOLE.setFormatter(FORMATTER)

LOGGER.addHandler(CONSOLE)
LOGGER.addHandler(FILE)
