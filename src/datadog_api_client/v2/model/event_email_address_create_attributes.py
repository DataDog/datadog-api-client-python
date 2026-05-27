# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.event_email_address_alert_type import EventEmailAddressAlertType
    from datadog_api_client.v2.model.event_email_address_format import EventEmailAddressFormat


class EventEmailAddressCreateAttributes(ModelNormal):
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
        from datadog_api_client.v2.model.event_email_address_format import EventEmailAddressFormat

        return {
            "alert_type": (EventEmailAddressAlertType,),
            "description": (str,),
            "format": (EventEmailAddressFormat,),
            "notify_handles": ([str],),
            "tags": ([str],),
        }

    attribute_map = {
        "alert_type": "alert_type",
        "description": "description",
        "format": "format",
        "notify_handles": "notify_handles",
        "tags": "tags",
    }

    def __init__(
        self_,
        format: EventEmailAddressFormat,
        alert_type: Union[EventEmailAddressAlertType, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        notify_handles: Union[List[str], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating an event email address.

        :param alert_type: The alert type of events generated from the email address.
        :type alert_type: EventEmailAddressAlertType, optional

        :param description: A description of the event email address.
        :type description: str, optional

        :param format: The format of events ingested through the email address.
        :type format: EventEmailAddressFormat

        :param notify_handles: A list of handles to notify when an email is received.
        :type notify_handles: [str], optional

        :param tags: A list of tags to apply to events generated from the email address.
        :type tags: [str], optional
        """
        if alert_type is not unset:
            kwargs["alert_type"] = alert_type
        if description is not unset:
            kwargs["description"] = description
        if notify_handles is not unset:
            kwargs["notify_handles"] = notify_handles
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.format = format
