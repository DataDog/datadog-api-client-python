"""
Delete metric collection returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi

# there is a valid "experiment_metric_collection" in the system
EXPERIMENT_METRIC_COLLECTION_DATA_ID = environ["EXPERIMENT_METRIC_COLLECTION_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    api_instance.delete_metric_collection(
        metric_collection_id=EXPERIMENT_METRIC_COLLECTION_DATA_ID,
    )
