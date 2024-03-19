"""
Create a Basic HTTP custom destination returns "OK" response
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
from datadog_api_client.v2.model.custom_destination_forward_destination_http import (
    CustomDestinationForwardDestinationHttp,
)
from datadog_api_client.v2.model.custom_destination_forward_destination_http_type import (
    CustomDestinationForwardDestinationHttpType,
)
from datadog_api_client.v2.model.custom_destination_http_destination_auth_basic import (
    CustomDestinationHttpDestinationAuthBasic,
)
from datadog_api_client.v2.model.custom_destination_http_destination_auth_basic_type import (
    CustomDestinationHttpDestinationAuthBasicType,
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
            forwarder_destination=CustomDestinationForwardDestinationHttp(
                auth=CustomDestinationHttpDestinationAuthBasic(
                    password="datadog-custom-destination-password",
                    type=CustomDestinationHttpDestinationAuthBasicType.BASIC,
                    username="datadog-custom-destination-username",
                ),
                endpoint="https://example.com",
                type=CustomDestinationForwardDestinationHttpType.HTTP,
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
