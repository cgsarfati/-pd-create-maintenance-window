#!/usr/bin/env python

# Python script to create a 2-hour maintenance window on one PD service

# SCRIPT SPECS
    # use pdpyras so its python 3 compatible (requirements.txt)
    # hardcode just ONE service ID, point out w/ #
    # start_time = current, end_time = +2hr
    # just ONE maintenance window, not recurring
    # hardcode API key, point out w/ #
    # Description = "PagerDuty Maintenance Window"

# EXAMPLE PAYLOAD
# {
#   "maintenance_window": {
#     "type": "maintenance_window",
#     "start_time": ""  # CURRENT
#     "end_time": " ""  # CURRENT +2hr
#     "description": "PagerDuty Maintenance Window",
#     "services": [
#       {
#         "id": "pd-service-id", ## INPUT SERVICE ID
#         "type": "service_reference"
#       }
#     ]
#   }
# }


import pdpyras
import json
import dateutil.parser as dateparser
from datetime import datetime, timedelta


api_token = 'input-api-token'  # input API key
session = pdpyras.APISession(api_token)


def create_maintenance_window():

    # initialize hardcoded variables
    # print "starting" message
    # post request w/ example payload
    # print response message / error handling
    exit()

if __name__ == '__main__':
    create_maintenance_window()
