'''
@author: cmcc
'''
import os
import yaml
# pylint: disable=E0611
from log_utils import LOGGER


def read_yaml(file):
    '''read a yaml file
    '''
    if not os.path.exists(file):
        LOGGER.info("%s not found", file)
        return None
    return yaml.load(open(file, "r"))


def write_yaml(file, dict_data):
    '''write a yaml file
    '''
    yaml.safe_dump(dict_data, open(file, "w"), explicit_start=True)


print(read_yaml("./conf/depends.yaml"))
print(read_yaml("./conf/cases.yaml"))

write_yaml("./conf/report.yaml", read_yaml("./conf/cases.yaml"))
