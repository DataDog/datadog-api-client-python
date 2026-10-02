"""
Create experiment metric group from collection returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi

# there is a valid "experiment" in the system
EXPERIMENT_DATA_ID = environ["EXPERIMENT_DATA_ID"]

# there is a valid "experiment_metric_collection_with_metric" in the system
EXPERIMENT_METRIC_COLLECTION_WITH_METRIC_DATA_ID = environ["EXPERIMENT_METRIC_COLLECTION_WITH_METRIC_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.create_experiment_metric_group_from_collection(
        experiment_id=EXPERIMENT_DATA_ID,
        metric_collection_id=EXPERIMENT_METRIC_COLLECTION_WITH_METRIC_DATA_ID,
    )

    print(response)
