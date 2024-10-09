"""
Post a change event returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.events_api import EventsApi
from datadog_api_client.v2.model.change_event import ChangeEvent
from datadog_api_client.v2.model.change_event_category import ChangeEventCategory
from datadog_api_client.v2.model.change_event_create_request import ChangeEventCreateRequest
from datadog_api_client.v2.model.change_event_create_request_type import ChangeEventCreateRequestType
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

body = ChangeEventCreateRequest(
    attributes=ChangeEvent(
        attributes=ChangeEventCustomAttributes(
            author=ChangeEventCustomAttributesAuthor(
                name="",
                type=ChangeEventCustomAttributesAuthorType.USER,
            ),
            change_metadata=dict(
                [
                    ("resource_link", "/feature/fallback_payments_test"),
                    ("user", "{'email': 'dd_user_email', 'name': 'dd_user'}"),
                ]
            ),
            changed_resource=ChangeEventCustomAttributesChangedResource(
                name="fallback_payments_test",
                type=ChangeEventCustomAttributesChangedResourceType.FEATURE_FLAG,
            ),
            impacted_resources=[
                ChangeEventCustomAttributesImpactedResourcesItems(
                    name="payments_api",
                    type=ChangeEventCustomAttributesImpactedResourcesItemsType.SERVICE,
                ),
            ],
            new_value=dict([("enabled", "True"), ("percentage", "50%"), ("rule", "{'datacenter': 'us1.prod'}")]),
            prev_value=dict([("enabled", "True"), ("percentage", "10%"), ("rule", "{'datacenter': 'us1.prod'}")]),
        ),
        category=ChangeEventCategory.CHANGE,
        message="payment_processed feature flag has been enabled",
        tags=[
            "environment:test",
        ],
        title="payment_processed feature flag updated",
    ),
    type=ChangeEventCreateRequestType.EVENT,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = EventsApi(api_client)
    response = api_instance.create_event(body=body)

    print(response)
