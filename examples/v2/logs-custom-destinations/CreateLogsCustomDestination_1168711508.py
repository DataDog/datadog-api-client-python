"""
Create a custom destination with HTTP request header forwarding returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi
from datadog_api_client.v2.model.custom_destination_attributes import CustomDestinationAttributes
from datadog_api_client.v2.model.custom_destination_create_data import CustomDestinationCreateData
from datadog_api_client.v2.model.custom_destination_create_request import CustomDestinationCreateRequest
from datadog_api_client.v2.model.custom_destination_type import CustomDestinationType
from datadog_api_client.v2.model.http_destination import HttpDestination
from datadog_api_client.v2.model.http_destination_custom_header_auth import HttpDestinationCustomHeaderAuth
from datadog_api_client.v2.model.http_destination_custom_header_auth_type import HttpDestinationCustomHeaderAuthType
from datadog_api_client.v2.model.http_destination_type import HttpDestinationType

body = CustomDestinationCreateRequest(
    data=CustomDestinationCreateData(
        attributes=CustomDestinationAttributes(
            name="my-destination",
            version=0,
            forwarder_destination=HttpDestination(
                type=HttpDestinationType.HTTP,
                endpoint="https://example.org/my-intake",
                auth=HttpDestinationCustomHeaderAuth(
                    type=HttpDestinationCustomHeaderAuthType.CUSTOM_HEADER,
                    header_name="header",
                    header_value="value",
                ),
            ),
        ),
        type=CustomDestinationType.CUSTOM_DESTINATION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_logs_custom_destination"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    response = api_instance.create_logs_custom_destination(body=body)

    print(response)
