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
    body = MetricBulkTagConfigDeleteRequest(
        data=MetricBulkTagConfigDelete(
            attributes=MetricBulkTagConfigDeleteAttributes(
                emails=MetricBulkTagConfigEmailList(["sue@example.com","bob@example.com"]),
            ),
            id="kafka.lag",
            type=MetricBulkConfigureTagsType("metric_bulk_configure_tags"),
        ),
    )  # MetricBulkTagConfigDeleteRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Configure tags for multiple metrics
        api_response = api_instance.delete_bulk_tags_metrics_configuration(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->delete_bulk_tags_metrics_configuration: %s\n" % e)
