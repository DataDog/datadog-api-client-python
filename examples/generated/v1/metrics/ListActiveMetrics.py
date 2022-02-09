import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import metrics_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    _from = 1  # int | Seconds since the Unix epoch.
    host = "host_example"  # str | Hostname for filtering the list of metrics returned. If set, metrics retrieved are those with the corresponding hostname tag. (optional)
    tag_filter = "env IN (staging,test) AND service:web"  # str | Filter metrics that have been submitted with the given tags. Supports boolean and wildcard expressions. Cannot be combined with other filters. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get active metrics list
        api_response = api_instance.list_active_metrics(_from)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_active_metrics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get active metrics list
        api_response = api_instance.list_active_metrics(_from, host=host, tag_filter=tag_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_active_metrics: %s\n" % e)
