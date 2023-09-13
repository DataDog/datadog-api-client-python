"""
Create a custom destination with Splunk forwarding returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi
from datadog_api_client.v2.model.custom_destination_attributes import CustomDestinationAttributes
from datadog_api_client.v2.model.custom_destination_create_data import CustomDestinationCreateData
from datadog_api_client.v2.model.custom_destination_create_request import CustomDestinationCreateRequest
from datadog_api_client.v2.model.custom_destination_type import CustomDestinationType
from datadog_api_client.v2.model.splunk_hec_destination import SplunkHecDestination
from datadog_api_client.v2.model.splunk_hec_destination_type import SplunkHecDestinationType

body = CustomDestinationCreateRequest(
    data=CustomDestinationCreateData(
        attributes=CustomDestinationAttributes(
            name="my-destination",
            version=0,
            forwarder_destination=SplunkHecDestination(
                type=SplunkHecDestinationType.SPLUNK_HEC,
                endpoint="https://example.org/my-intake",
                access_token="secret",
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
