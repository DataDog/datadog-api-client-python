"""
Get experiment analysis plan returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi

# there is a valid "experiment" in the system
EXPERIMENT_DATA_ID = environ["EXPERIMENT_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.get_experiment_analysis_plan(
        experiment_id=EXPERIMENT_DATA_ID,
    )

    print(response)
