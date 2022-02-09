import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()
configuration.unstable_operations["update_tag_configuration"] = True

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    metric_name = "dist.http.endpoint.request"  # str | The name of the metric.
    body = MetricTagConfigurationUpdateRequest(
        data=MetricTagConfigurationUpdateData(
            attributes=MetricTagConfigurationUpdateAttributes(
                aggregations=MetricCustomAggregations([
                    MetricCustomAggregation(
                        space=MetricCustomSpaceAggregation("sum"),
                        time=MetricCustomTimeAggregation("sum"),
                    ),
                ]),
                include_percentiles=True,
                tags=["app","datacenter"],
            ),
            id="test.metric.latency",
            type=MetricTagConfigurationType("manage_tags"),
        ),
    )  # MetricTagConfigurationUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update a tag configuration
        api_response = api_instance.update_tag_configuration(metric_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->update_tag_configuration: %s\n" % e)
