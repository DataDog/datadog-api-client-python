"""
Create a Splunk custom destination returns "OK" response
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
from datadog_api_client.v2.model.custom_destination_forward_destination_splunk import (
    CustomDestinationForwardDestinationSplunk,
)
from datadog_api_client.v2.model.custom_destination_forward_destination_splunk_type import (
    CustomDestinationForwardDestinationSplunkType,
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
            forwarder_destination=CustomDestinationForwardDestinationSplunk(
                access_token="my-access-token",
                endpoint="https://example.com",
                type=CustomDestinationForwardDestinationSplunkType.SPLUNK_HEC,
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
