import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import logs_metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = logs_metrics_api.LogsMetricsApi(api_client)
    metric_id = "metric_id_example"  # str | The name of the log-based metric.

    # example passing only required values which don't have defaults set
    try:
        # Delete a log-based metric
        api_instance.delete_logs_metric(metric_id)
    except ApiException as e:
        print("Exception when calling LogsMetricsApi->delete_logs_metric: %s\n" % e)
