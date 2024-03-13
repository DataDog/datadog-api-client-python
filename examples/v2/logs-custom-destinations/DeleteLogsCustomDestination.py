"""
Delete a custom destination returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi

# there is a valid "custom_destination" in the system
CUSTOM_DESTINATION_DATA_ID = environ["CUSTOM_DESTINATION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    api_instance.delete_logs_custom_destination(
        custom_destination_id=CUSTOM_DESTINATION_DATA_ID,
    )
