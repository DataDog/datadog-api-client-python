"""
List tags by metric name returns "Success" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

# there is a valid "metric_tag_configuration" in the system
METRIC_TAG_CONFIGURATION_DATA_ID = environ["METRIC_TAG_CONFIGURATION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_tags_by_metric_name(
        metric_name=METRIC_TAG_CONFIGURATION_DATA_ID,
    )

    print(response)
