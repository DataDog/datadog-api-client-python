"""
Create a custom destination with Elasticsearch forwarding returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi
from datadog_api_client.v2.model.custom_destination_attributes import CustomDestinationAttributes
from datadog_api_client.v2.model.custom_destination_create_payload import CustomDestinationCreatePayload
from datadog_api_client.v2.model.custom_destination_without_id import CustomDestinationWithoutId
from datadog_api_client.v2.model.elasticsearch_destination import ElasticsearchDestination
from datadog_api_client.v2.model.elasticsearch_destination_type import ElasticsearchDestinationType
from datadog_api_client.v2.model.http_destination_basic_auth import HttpDestinationBasicAuth
from datadog_api_client.v2.model.http_destination_basic_auth_type import HttpDestinationBasicAuthType

body = CustomDestinationCreatePayload(
    data=CustomDestinationWithoutId(
        attributes=CustomDestinationAttributes(
            name="my-destination",
            version=0,
            forwarder_destination=ElasticsearchDestination(
                type=ElasticsearchDestinationType.ELASTICSEARCH,
                endpoint="https://example.org/my-intake",
                index_name="name",
                index_rotation="yyyy-MM-dd",
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
