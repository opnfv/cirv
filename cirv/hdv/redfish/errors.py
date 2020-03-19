##############################################################################
# Copyright (c) 2020 China Mobile Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################
"""
ERROR CODE instruction
"""
ERROR_CODE = {
    # E100XXX: Connection
    "E100001": "E100001:fail to get response from the url",
    "E100002": "E100002:unexpected request url",
    "E100003": "E100003:failed to setup connection",
    # E200XXX: options - tools arguments.
    "E200001": "E200001:unsupported input file_mode, \
    should be one of [yaml,excel]",
    # E300XXX: resource issue  - depended resource is not existing...
    "E300001": "E300001:invalid token",
    "E300002": "E300002:fail to get dependency parent id, Action: check if the \
    resource support by server",
    "E300003": "E300003:fail to get expected id list for component_id, \
    Action: check if the resource support by server",
    # E400XXX: configuration error
    "E400001": "E400001:fail to find configure file",
    "E400002": "E400002:parse config.yaml exception",
    "E400003": "E400003: key_list is null for key_flags",
    "E400004": "E400004: unexpected response body type",
    "E400005": "E400005: customized expected value format error, \
    Action:check input expected value type with actual returned value type",
    "E400006": "E400006: unexpected expected value type, \
    expected[str,list,dict]",
    "E400007": "E400007: unexpected expected value type while comparing",
    # E500XXX: application - find no value from cache
    "E500001": "E500001: fail find key from actual value, \
    Action: check if the attribute support by server",
    # E600XXX: restful interface
    "E600001": "E600001: unsupported redfish api?",
    }

WARN_CODE = {
    "W100001": "W100001: fail to the response from a request",
    "W100002": "W100002: unexpected type of return_value type",
    "W100003": "W100003: NoneType value",
}
