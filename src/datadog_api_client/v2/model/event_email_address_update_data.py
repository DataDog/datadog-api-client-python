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
    from datadog_api_client.v2.model.event_email_address_update_attributes import EventEmailAddressUpdateAttributes
    from datadog_api_client.v2.model.event_email_address_resource_type import EventEmailAddressResourceType


class EventEmailAddressUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_email_address_update_attributes import EventEmailAddressUpdateAttributes
        from datadog_api_client.v2.model.event_email_address_resource_type import EventEmailAddressResourceType

        return {
            "attributes": (EventEmailAddressUpdateAttributes,),
            "type": (EventEmailAddressResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: EventEmailAddressUpdateAttributes, type: EventEmailAddressResourceType, **kwargs):
        """
        Data for updating an event email address.

        :param attributes: Attributes for updating an event email address.
        :type attributes: EventEmailAddressUpdateAttributes

        :param type: The type of the resource. Must be ``event_emails``.
        :type type: EventEmailAddressResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
