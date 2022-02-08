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
    metric_name = "metric_name_example"  # str | Name of the metric for which to edit metadata.
    body = MetricMetadata(
        description="description_example",
        per_unit="second",
        short_name="short_name_example",
        statsd_interval=1,
        type="count",
        unit="byte",
    )  # MetricMetadata | New metadata.

    # example passing only required values which don't have defaults set
    try:
        # Edit metric metadata
        api_response = api_instance.update_metric_metadata(metric_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->update_metric_metadata: %s\n" % e)
