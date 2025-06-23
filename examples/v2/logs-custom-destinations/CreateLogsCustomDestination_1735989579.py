"""
Create a Microsoft Sentinel custom destination returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi
from datadog_api_client.v2.model.custom_destination_attribute_tags_restriction_list_type import (
    CustomDestinationAttributeTagsRestrictionListType,
)
from datadog_api_client.v2.model.custom_destination_create_request import CustomDestinationCreateRequest
from datadog_api_client.v2.model.custom_destination_create_request_attributes import (
    CustomDestinationCreateRequestAttributes,
)
from datadog_api_client.v2.model.custom_destination_create_request_definition import (
    CustomDestinationCreateRequestDefinition,
)
from datadog_api_client.v2.model.custom_destination_forward_destination_microsoft_sentinel import (
    CustomDestinationForwardDestinationMicrosoftSentinel,
)
from datadog_api_client.v2.model.custom_destination_forward_destination_microsoft_sentinel_type import (
    CustomDestinationForwardDestinationMicrosoftSentinelType,
)
from datadog_api_client.v2.model.custom_destination_type import CustomDestinationType

body = CustomDestinationCreateRequest(
    data=CustomDestinationCreateRequestDefinition(
        attributes=CustomDestinationCreateRequestAttributes(
            enabled=False,
            forward_tags=False,
            forward_tags_restriction_list=[
                "datacenter",
                "host",
            ],
            forward_tags_restriction_list_type=CustomDestinationAttributeTagsRestrictionListType.ALLOW_LIST,
            forwarder_destination=CustomDestinationForwardDestinationMicrosoftSentinel(
                type=CustomDestinationForwardDestinationMicrosoftSentinelType.MICROSOFT_SENTINEL,
                tenant_id="f3c9a8a1-4c2e-4d2e-b911-9f3c28c3c8b2",
                client_id="9a2f4d83-2b5e-429e-a35a-2b3c4182db71",
                data_collection_endpoint="https://my-dce-5kyl.eastus-1.ingest.monitor.azure.com",
                data_collection_rule_id="dcr-000a00a000a00000a000000aa000a0aa",
                stream_name="Custom-MyTable",
            ),
            name="Nginx logs",
            query="source:nginx",
        ),
        type=CustomDestinationType.CUSTOM_DESTINATION,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    response = api_instance.create_logs_custom_destination(body=body)

    print(response)
