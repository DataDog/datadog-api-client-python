"""
Delete a custom destination returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi

# there is a valid "logs_custom_destination" in the system
LOGS_CUSTOM_DESTINATION_DATA_ID = environ["LOGS_CUSTOM_DESTINATION_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_logs_custom_destination"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    response = api_instance.delete_logs_custom_destination(
        custom_destination_id=LOGS_CUSTOM_DESTINATION_DATA_ID,
    )

    print(response)
