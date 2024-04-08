"""
Update a custom destination returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_custom_destinations_api import LogsCustomDestinationsApi
from datadog_api_client.v2.model.custom_destination_attribute_tags_restriction_list_type import (
    CustomDestinationAttributeTagsRestrictionListType,
)
from datadog_api_client.v2.model.custom_destination_type import CustomDestinationType
from datadog_api_client.v2.model.custom_destination_update_request import CustomDestinationUpdateRequest
from datadog_api_client.v2.model.custom_destination_update_request_attributes import (
    CustomDestinationUpdateRequestAttributes,
)
from datadog_api_client.v2.model.custom_destination_update_request_definition import (
    CustomDestinationUpdateRequestDefinition,
)

# there is a valid "custom_destination" in the system
CUSTOM_DESTINATION_DATA_ID = environ["CUSTOM_DESTINATION_DATA_ID"]

body = CustomDestinationUpdateRequest(
    data=CustomDestinationUpdateRequestDefinition(
        attributes=CustomDestinationUpdateRequestAttributes(
            name="Nginx logs (Updated)",
            query="source:nginx",
            enabled=False,
            forward_tags=False,
            forward_tags_restriction_list_type=CustomDestinationAttributeTagsRestrictionListType.BLOCK_LIST,
        ),
        type=CustomDestinationType.CUSTOM_DESTINATION,
        id=CUSTOM_DESTINATION_DATA_ID,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsCustomDestinationsApi(api_client)
    response = api_instance.update_logs_custom_destination(custom_destination_id=CUSTOM_DESTINATION_DATA_ID, body=body)

    print(response)
