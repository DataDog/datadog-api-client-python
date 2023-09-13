"""
Update a custom destination returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi
from datadog_api_client.v2.model.custom_destination import CustomDestination
from datadog_api_client.v2.model.custom_destination_attributes import CustomDestinationAttributes
from datadog_api_client.v2.model.custom_destination_type import CustomDestinationType
from datadog_api_client.v2.model.custom_destination_update_request import CustomDestinationUpdateRequest
from datadog_api_client.v2.model.http_destination import HttpDestination
from datadog_api_client.v2.model.http_destination_basic_auth import HttpDestinationBasicAuth
from datadog_api_client.v2.model.http_destination_basic_auth_type import HttpDestinationBasicAuthType
from datadog_api_client.v2.model.http_destination_type import HttpDestinationType

# there is a valid "logs_custom_destination" in the system
LOGS_CUSTOM_DESTINATION_DATA_ATTRIBUTES_NAME = environ["LOGS_CUSTOM_DESTINATION_DATA_ATTRIBUTES_NAME"]
LOGS_CUSTOM_DESTINATION_DATA_ID = environ["LOGS_CUSTOM_DESTINATION_DATA_ID"]

body = CustomDestinationUpdateRequest(
    data=CustomDestination(
        id=LOGS_CUSTOM_DESTINATION_DATA_ID,
        attributes=CustomDestinationAttributes(
            name="my-destination--updated-name",
            version=0,
            forwarder_destination=HttpDestination(
                type=HttpDestinationType.HTTP,
                endpoint="https://example.org/my-intake",
                auth=HttpDestinationBasicAuth(
                    type=HttpDestinationBasicAuthType.BASIC,
                    username="username",
                    password="password",
                ),
            ),
        ),
        type=CustomDestinationType.CUSTOM_DESTINATION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_logs_custom_destination"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    response = api_instance.update_logs_custom_destination(
        custom_destination_id=LOGS_CUSTOM_DESTINATION_DATA_ID, body=body
    )

    print(response)
