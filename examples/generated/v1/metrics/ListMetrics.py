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
    q = "q_example"  # str | Query string to search metrics upon. Must be prefixed with `metrics:`.

    # example passing only required values which don't have defaults set
    try:
        # Search metrics
        api_response = api_instance.list_metrics(q)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_metrics: %s\n" % e)
