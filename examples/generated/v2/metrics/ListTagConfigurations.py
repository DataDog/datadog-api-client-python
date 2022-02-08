import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["list_tag_configurations"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    filter_configured = True  # bool | Filter metrics that have configured tags. (optional)
    filter_tags_configured = "app"  # str | Filter tag configurations by configured tags. (optional)
    filter_metric_type = MetricTagConfigurationMetricTypes("count")  # MetricTagConfigurationMetricTypes | Filter tag configurations by metric type. (optional)
    filter_include_percentiles = True  # bool | Filter distributions with additional percentile aggregations enabled or disabled. (optional)
    filter_tags = "env IN (staging,test) AND service:web"  # str | Filter metrics that have been submitted with the given tags. Supports boolean and wildcard expressions. Cannot be combined with other filters. (optional)
    window_seconds = 3600  # int | The number of seconds of look back (from now) to apply to a filter[tag] query. Defaults value is 3600 (1 hour), maximum value is 172,800 (2 days). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List tag configurations
        api_response = api_instance.list_tag_configurations(filter_configured=filter_configured, filter_tags_configured=filter_tags_configured, filter_metric_type=filter_metric_type, filter_include_percentiles=filter_include_percentiles, filter_tags=filter_tags, window_seconds=window_seconds)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_tag_configurations: %s\n" % e)
