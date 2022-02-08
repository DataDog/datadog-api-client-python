import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import downtimes_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = downtimes_api.DowntimesApi(api_client)
    downtime_id = 123456  # int | ID of the downtime to update.
    body = Downtime(
        disabled=False,
        end=1412793983,
        message="Message on the downtime",
        monitor_id=123456,
        monitor_tags=["*"],
        parent_id=123,
        recurrence=DowntimeRecurrence(
            period=1,
            rrule="FREQ=MONTHLY;BYSETPOS=3;BYDAY=WE;INTERVAL=1",
            type="weeks",
            until_date=1447786293,
            until_occurrences=2,
            week_days=["Mon","Tue"],
        ),
        scope=["env:staging"],
        start=1412792983,
        timezone="America/New_York",
    )  # Downtime | Update a downtime request body.

    # example passing only required values which don't have defaults set
    try:
        # Update a downtime
        api_response = api_instance.update_downtime(downtime_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DowntimesApi->update_downtime: %s\n" % e)
