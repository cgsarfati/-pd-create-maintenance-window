#!/usr/bin/env python

# Python script to create a 2-hour maintenance window on one PD service
# CLI usage: python maintenance-window.py


import pdpyras
from datetime import datetime, timedelta


api_token = 'api-key-here'  # API KEY HERE
session = pdpyras.APISession(api_token)


def create_maintenance_window():

    # set up time
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=120)

    print("Creating maintenance window...")

    # create window
    try:
        api_request = session.rpost('maintenance_windows', json={
            'type': 'maintenance_window',
            'start_time': start_time.isoformat(),
            'end_time': end_time.isoformat(),
            'description': "PagerDuty Maintenance Window",
            'services': [
                {'id': 'service-id-here',  # SERVICE ID HERE
                    'type': 'service_reference'}]
            })
        print("Maintenance window successfully created")

    # error handling
    except pdpyras.PDClientError as e:
        msg = "API Error: "
        if e.response is not None:
            msg += "HTTP %d" % (e.response.status_code)
            print(msg)


if __name__ == '__main__':
    create_maintenance_window()
