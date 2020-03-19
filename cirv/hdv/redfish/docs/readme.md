##############################################################################
# Copyright (c) 2020 China Mobile Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

This is a prototype of hardware validation implementation in redfish interface for a certain hardware vendor.
which originally is contributed by China Mobile.
>>> Usage:
usage: hdv.py [-h] [--version] [--config CONFIG] [--file_type FILE_TYPE]
              [--case_yaml CASE_YAML] [--depends_yaml DEPENDS_YAML]
              [--case_excel CASE_EXCEL]

hdv tool by redfish, it works in two mode

optional arguments:
  -h, --help            show this help message and exit
  --version             show tool version
  --config CONFIG       given global config.yaml file
  --file_type FILE_TYPE
                        config file type, [yaml|excel]
  --case_yaml CASE_YAML
                        case yaml file, uesd if file_type = yaml
  --depends_yaml DEPENDS_YAML
                        depends yaml file,uesd if file_type = yaml
  --case_excel CASE_EXCEL
                        excel case file used if file_type = excel
example:
#default case 
1>python .\hdv.py 
following config used
  - ./conf/config.yaml 
  - file_type=excel
  - ./conf/cases.xlsx
# use file_type=yaml
2>python .\hdv.py --file_type=yaml		

example1. default conf/config.yaml, file_type=excel, cases.xlsx used
python .\hdv.py
example2. use yaml file type config, default conf/cases.yaml conf/depends.yaml used 
python .\hdv.py --file_type=yaml 
example3. user input config file 
python .\hdv.py --file_type=yaml --case_yaml=./conf-new/cases.yaml --depends_yaml=./conf-new/depends.yaml		
						
>>> tools directory:

./redfish
├─conf   # config directory
├─docs   # readme
├─logs   # hdv.log would be generated here.

$ ls -lR .
$ ls redfish/*.py
redfish/__init__.py  
redfish/excel_2_yaml.py   #tool script to convert excel cases.xlsx sheets content to yaml format cases.yaml and depends.yaml
redfish/hdv_redfish.py    #the code implementation by parsing config.yaml and cases.xlsx or cases.yaml and depends.yaml
redfish/log_utils.py      #log utils
redfish/errors.py         #error code definition for the tool during parse.
redfish/hdv.py            #hdv portal
redfish/http_handler.py   #http_handler
redfish/yaml_utils.py	  #yaml utils for test.

$ ls redfish/conf
config.yaml  #global config yaml where define BMC settings, static value, and some position definition in the cases.xlsx excel
cases.xlsx   #two sheet defined (cases and depend_id), input case file if file_type=excel, default way.
             #sheet cases - define all test case redfish url, expected value, etc
			 #sheet dependent_id - define all dependent_id url which is used to get parent resource id for the url in the cases.
cases.yaml   #test cases yaml file,where the same set test case with cases.xlsx, it is used if file_type=yaml
depends.yaml #depends.yaml where the same content with sheet dependent_id, it is used if file_type=yaml
report.yaml  #final test report, it is used if file_type=yaml

$ ls redfish/docs
readme.md   #readme

$ ls redfish/logs
hdv.log     # test log file

>>> Principle
The hdv tool gets the global config from conf/config.yaml, e.g bmc settings, and 
global variable definitions, and some excel column position used in case file_type=excel
User can select eiter file_type yaml or excel as the configure file type, 
default type is excel at present. However the principle is similar.

If file_type is excel, it will parse two sheets of excel workbook, cases and dependent_id. 
The dependent_id sheet is used to define how to get the parents before checking a final redfish url, 
thinking about checking a port should get the adapter at first.
The cases sheet is the test cases template, where the variable will be replaced 
by global static value from config yaml or dependent_id

By running a final redfish url request, it will get response result from the test server.
Then tool will compare the response value with expected value defined in <expected_result> column of cases sheet to decide if the case status.

test report of each case <details,case_status>  will write back to the same excel in the last two columns.

Meanwhile, yaml file_type is supported also, it processes similarly as excel, except
- reading depends.yaml to get the dependent_id
- reading cases.yaml to run the test case
- report.yaml will be created as the final report.
cases.xlsx will not be used anymore in yaml case.

Besides, excel_2_yaml.py script can be used to convert the cases.xlsx to yaml file accordingly. 
If you want to update the cases content, you can update the excel at first, then convert by the script.

>>> FAQ:
1. how to customize expected result?
you need put a json format value in it, the hierachy should be exactly the same with actual returned value, 
as the comparing implementation relies on it.
 => a simple example: '{"AssetTag": "CM_cc@1234"}'
 => a complex example: 
'{    "count": 2,    "Manufacturer": "Intel(R) Corporation",    "MaxSpeedMHz":
    2300,    "Model": "Intel(R) Xeon(R) Gold 5218N CPU @ 2.30GHz",    "ProcessorArchitecture":
    ["x86", "IA-64", "ARM", "MIPS", "OEM"],    "Socket": [1, 2],    "Status": {        "Health":
    "OK",        "State": "Enabled"    },    "TotalCores": 16,    "TotalThreads":
    32}'
 
in the above data, a specific "count" attribute defined to check components quantity returned, e.g How many cpus expected.
generally it can be a subset attributes definition, comparing with actual return value
also it can support list of all expected value for list of objects. 
example: "Socket:[1,2]", expecting return "Socket:1" and "Socket:2" from returned response

>>>Perspective:
- there are differences between vendors's implementation, or even versions for the same vendor.
- define more test case or update existing case in the cases.yaml and depends.yaml or cases.xlsx file to support much more checks.
- more implementation could be contributed from community so that it can grow bigger to support more types and checkpoints test case.
	
#https://gerrit.opnfv.org/gerrit/admin/repos/cirv
