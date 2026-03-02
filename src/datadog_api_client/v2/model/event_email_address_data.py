# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.event_email_address_response_attributes import EventEmailAddressResponseAttributes
    from datadog_api_client.v2.model.event_email_address_relationships import EventEmailAddressRelationships
    from datadog_api_client.v2.model.event_email_address_resource_type import EventEmailAddressResourceType


class EventEmailAddressData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_email_address_response_attributes import (
            EventEmailAddressResponseAttributes,
        )
        from datadog_api_client.v2.model.event_email_address_relationships import EventEmailAddressRelationships
        from datadog_api_client.v2.model.event_email_address_resource_type import EventEmailAddressResourceType

        return {
            "attributes": (EventEmailAddressResponseAttributes,),
            "id": (str,),
            "relationships": (EventEmailAddressRelationships,),
            "type": (EventEmailAddressResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: EventEmailAddressResponseAttributes,
        id: str,
        relationships: EventEmailAddressRelationships,
        type: EventEmailAddressResourceType,
        **kwargs,
    ):
        """
        A single event email address resource.

        :param attributes: Attributes of an event email address resource.
        :type attributes: EventEmailAddressResponseAttributes

        :param id: The UUID of the event email address.
        :type id: str

        :param relationships: Relationships associated with an event email address resource.
        :type relationships: EventEmailAddressRelationships

        :param type: The type of the resource. Must be ``event_emails``.
        :type type: EventEmailAddressResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.relationships = relationships
        self_.type = type
