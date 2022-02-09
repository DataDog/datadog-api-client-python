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
    downtime_id = 123456  # int | ID of the downtime to cancel.

    # example passing only required values which don't have defaults set
    try:
        # Cancel a downtime
        api_instance.cancel_downtime(downtime_id)
    except ApiException as e:
        print("Exception when calling DowntimesApi->cancel_downtime: %s\n" % e)
