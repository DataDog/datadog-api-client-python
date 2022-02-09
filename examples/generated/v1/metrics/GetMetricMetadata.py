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
    metric_name = "metric_name_example"  # str | Name of the metric for which to get metadata.

    # example passing only required values which don't have defaults set
    try:
        # Get metric metadata
        api_response = api_instance.get_metric_metadata(metric_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_metric_metadata: %s\n" % e)
