"""
Create a custom destination returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi
from datadog_api_client.v2.model.azure_fallback_destination import AzureFallbackDestination
from datadog_api_client.v2.model.azure_fallback_destination_integration import AzureFallbackDestinationIntegration
from datadog_api_client.v2.model.azure_fallback_destination_type import AzureFallbackDestinationType
from datadog_api_client.v2.model.custom_destination_attributes import CustomDestinationAttributes
from datadog_api_client.v2.model.custom_destination_compression_type import CustomDestinationCompressionType
from datadog_api_client.v2.model.custom_destination_create_data import CustomDestinationCreateData
from datadog_api_client.v2.model.custom_destination_create_request import CustomDestinationCreateRequest
from datadog_api_client.v2.model.custom_destination_type import CustomDestinationType
from datadog_api_client.v2.model.http_destination import HttpDestination
from datadog_api_client.v2.model.http_destination_basic_auth import HttpDestinationBasicAuth
from datadog_api_client.v2.model.http_destination_basic_auth_type import HttpDestinationBasicAuthType
from datadog_api_client.v2.model.http_destination_type import HttpDestinationType

body = CustomDestinationCreateRequest(
    data=CustomDestinationCreateData(
        attributes=CustomDestinationAttributes(
            buffer_max_bytes=10000000,
            buffer_timeout_seconds=100,
            compression=CustomDestinationCompressionType.GZIP_COMPRESSION,
            enabled=True,
            fallback_destination=AzureFallbackDestination(
                container="container-name",
                integration=AzureFallbackDestinationIntegration(
                    client_id="aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
                    tenant_id="aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
                ),
                storage_account="account-name",
                type=AzureFallbackDestinationType.AZURE,
            ),
            forwarder_destination=HttpDestination(
                auth=HttpDestinationBasicAuth(
                    password="password",
                    type=HttpDestinationBasicAuthType.BASIC,
                    username="username",
                ),
                endpoint="https://example.org/my-intake",
                type=HttpDestinationType.HTTP,
            ),
            max_retry_duration_seconds=100,
            name="my-destination",
            query="source:dummy",
            version=0,
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
