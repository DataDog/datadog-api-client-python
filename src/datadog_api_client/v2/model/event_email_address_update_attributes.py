# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.event_email_address_alert_type import EventEmailAddressAlertType


class EventEmailAddressUpdateAttributes(ModelNormal):
    validations = {
        "description": {
            "max_length": 1024,
        },
        "notify_handles": {
            "max_items": 10,
        },
        "tags": {
            "max_items": 20,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_email_address_alert_type import EventEmailAddressAlertType

        return {
            "alert_type": (EventEmailAddressAlertType,),
            "description": (str, none_type),
            "notify_handles": ([str],),
            "tags": ([str],),
        }

    attribute_map = {
        "alert_type": "alert_type",
        "description": "description",
        "notify_handles": "notify_handles",
        "tags": "tags",
    }

    def __init__(
        self_,
        alert_type: EventEmailAddressAlertType,
        description: Union[str, none_type],
        notify_handles: List[str],
        tags: List[str],
        **kwargs,
    ):
        """
        Attributes for updating an event email address.

        :param alert_type: The alert type of events generated from the email address.
        :type alert_type: EventEmailAddressAlertType

        :param description: A description of the event email address.
        :type description: str, none_type

        :param notify_handles: A list of handles to notify when an email is received.
        :type notify_handles: [str]

        :param tags: A list of tags to apply to events generated from the email address.
        :type tags: [str]
        """
        super().__init__(kwargs)

        self_.alert_type = alert_type
        self_.description = description
        self_.notify_handles = notify_handles
        self_.tags = tags
