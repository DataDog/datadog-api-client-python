"""
Delete subject type returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi

# there is a valid "experiment_subject_type" in the system
EXPERIMENT_SUBJECT_TYPE_DATA_ID = environ["EXPERIMENT_SUBJECT_TYPE_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    api_instance.delete_subject_type(
        subject_type_id=EXPERIMENT_SUBJECT_TYPE_DATA_ID,
    )
