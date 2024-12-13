"""
Cancels a data deletion request returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.data_deletion_api import DataDeletionApi

# there is a valid "deletion_request" in the system
DELETION_REQUEST_DATA_ID = environ["DELETION_REQUEST_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["cancel_data_deletion_request"] = True
with ApiClient(configuration) as api_client:
    api_instance = DataDeletionApi(api_client)
    response = api_instance.cancel_data_deletion_request(
        id=DELETION_REQUEST_DATA_ID,
    )

    print(response)
