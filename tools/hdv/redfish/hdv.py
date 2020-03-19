##############################################################################
# Copyright (c) 2020 China Mobile Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################
'''
hdv tools
 all config files are put under conf/
 config.yaml is the global configuration
 additional config for supporting two modes
 - excel: tools will parse the depend_id sheet and cases sheet and
 execute test case and write report back to excel
 - yaml: tools will parse depends.yaml and cases.yaml and execute test case
 and write a report.yaml
 theory:
   either test case can be finished by one restful request,
   or an additional request needed to get dependency parent resource.
   e.g a case for checking port, should get networkadaptor_id before that.
'''
import argparse
from hdv_redfish import run as run_case


def parse_args():
    '''
    parse arguments
    '''
    parser = argparse.ArgumentParser(description="hdv tool by redfish, \
    check readme under ./docs")
    parser.add_argument('--version', action='version',
                        version='%(prog)s 0.1', help="show tool version")
    parser.add_argument('--config', type=str, default="./conf/config.yaml",
                        help="given global config.yaml file")
    parser.add_argument('--file_type', type=str, default="excel",
                        help="config file type, [yaml|excel],default is excel")
    parser.add_argument('--case_yaml', type=str, default="./conf/cases.yaml",
                        help="case yaml file, uesd if file_type = yaml")
    parser.add_argument('--depends_yaml', type=str,
                        default="./conf/depends.yaml",
                        help="depends yaml file,uesd if file_type = yaml")
    parser.add_argument('--case_excel', type=str, default="./conf/cases.xlsx",
                        help="excel case file used if file_type = excel")
    args = parser.parse_args()
    return args


def main():
    '''
    main function
    '''
    args = parse_args()
    run_case(args.config, args.case_excel, args.depends_yaml, args.case_yaml,
             args.file_type)


if __name__ == "__main__":
    main()
