"""
Create a custom destination with HTTP basic auth forwarding returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi
from datadog_api_client.v2.model.custom_destination_attributes import CustomDestinationAttributes
from datadog_api_client.v2.model.custom_destination_create_payload import CustomDestinationCreatePayload
from datadog_api_client.v2.model.custom_destination_without_id import CustomDestinationWithoutId
from datadog_api_client.v2.model.http_destination import HttpDestination
from datadog_api_client.v2.model.http_destination_basic_auth import HttpDestinationBasicAuth
from datadog_api_client.v2.model.http_destination_basic_auth_type import HttpDestinationBasicAuthType
from datadog_api_client.v2.model.http_destination_type import HttpDestinationType

body = CustomDestinationCreatePayload(
    data=CustomDestinationWithoutId(
        attributes=CustomDestinationAttributes(
            name="my-destination",
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
        type="custom_destination",
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_logs_custom_destination"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    response = api_instance.create_logs_custom_destination(body=body)

    print(response)
