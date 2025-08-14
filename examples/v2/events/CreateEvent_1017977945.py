"""
Post an event with metric_configuration resource type returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi
from datadog_api_client.v2.model.change_event_custom_attributes import ChangeEventCustomAttributes
from datadog_api_client.v2.model.change_event_custom_attributes_author import ChangeEventCustomAttributesAuthor
from datadog_api_client.v2.model.change_event_custom_attributes_author_type import ChangeEventCustomAttributesAuthorType
from datadog_api_client.v2.model.change_event_custom_attributes_changed_resource import (
    ChangeEventCustomAttributesChangedResource,
)
from datadog_api_client.v2.model.change_event_custom_attributes_changed_resource_type import (
    ChangeEventCustomAttributesChangedResourceType,
)
from datadog_api_client.v2.model.change_event_custom_attributes_impacted_resources_items import (
    ChangeEventCustomAttributesImpactedResourcesItems,
)
from datadog_api_client.v2.model.change_event_custom_attributes_impacted_resources_items_type import (
    ChangeEventCustomAttributesImpactedResourcesItemsType,
)
from datadog_api_client.v2.model.event_category import EventCategory
from datadog_api_client.v2.model.event_create_request import EventCreateRequest
from datadog_api_client.v2.model.event_create_request_payload import EventCreateRequestPayload
from datadog_api_client.v2.model.event_create_request_type import EventCreateRequestType
from datadog_api_client.v2.model.event_payload import EventPayload
from datadog_api_client.v2.model.event_payload_integration_id import EventPayloadIntegrationId

body = EventCreateRequestPayload(
    data=EventCreateRequest(
        attributes=EventPayload(
            aggregation_key="aggregation_key_123",
            attributes=ChangeEventCustomAttributes(
                author=ChangeEventCustomAttributesAuthor(
                    name="example@datadog.com",
                    type=ChangeEventCustomAttributesAuthorType.USER,
                ),
                change_metadata=dict(
                    [
                        (
                            "dd",
                            "{'team': 'datadog_team', 'user_email': 'datadog@datadog.com', 'user_id': 'datadog_user_id', 'user_name': 'datadog_username'}",
                        ),
                        ("resource_link", "datadog.com/metric/config_test"),
                    ]
                ),
                changed_resource=ChangeEventCustomAttributesChangedResource(
                    name="config_test",
                    type=ChangeEventCustomAttributesChangedResourceType.METRIC_CONFIGURATION,
                ),
                impacted_resources=[
                    ChangeEventCustomAttributesImpactedResourcesItems(
                        name="system.cpu.usage",
                        type=ChangeEventCustomAttributesImpactedResourcesItemsType.SERVICE,
                    ),
                ],
                new_value=dict([("aggregation", "avg"), ("tags", "['env:prod', 'service:web']"), ("unit", "percent")]),
                prev_value=dict([("aggregation", "sum"), ("tags", "['env:prod']"), ("unit", "percent")]),
            ),
            category=EventCategory.CHANGE,
            integration_id=EventPayloadIntegrationId.CUSTOM_EVENTS,
            message="metric configuration has been updated",
            tags=[
                "env:api_client_test",
            ],
            title="metric configuration updated",
        ),
        type=EventCreateRequestType.EVENT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.create_event(body=body)

    print(response)
