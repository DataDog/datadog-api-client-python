import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    metric_name = "dist.http.endpoint.request"  # str | The name of the metric.

    # example passing only required values which don't have defaults set
    try:
        # List distinct metric volumes by metric name
        api_response = api_instance.list_volumes_by_metric_name(metric_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_volumes_by_metric_name: %s\n" % e)
