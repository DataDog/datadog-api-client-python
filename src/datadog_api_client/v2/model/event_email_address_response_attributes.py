# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.event_email_address_alert_type import EventEmailAddressAlertType
    from datadog_api_client.v2.model.event_email_address_format import EventEmailAddressFormat


class EventEmailAddressResponseAttributes(ModelNormal):
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
            "created_at": (datetime,),
            "description": (str, none_type),
            "email": (str,),
            "format": (EventEmailAddressFormat,),
            "last_used_at": (datetime, none_type),
            "notify_handles": ([str],),
            "revoked_at": (datetime, none_type),
            "tags": ([str],),
        }

    attribute_map = {
        "alert_type": "alert_type",
        "created_at": "created_at",
        "description": "description",
        "email": "email",
        "format": "format",
        "last_used_at": "last_used_at",
        "notify_handles": "notify_handles",
        "revoked_at": "revoked_at",
        "tags": "tags",
    }

    def __init__(
        self_,
        created_at: datetime,
        email: str,
        format: EventEmailAddressFormat,
        alert_type: Union[EventEmailAddressAlertType, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        last_used_at: Union[datetime, none_type, UnsetType] = unset,
        notify_handles: Union[List[str], UnsetType] = unset,
        revoked_at: Union[datetime, none_type, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an event email address resource.

        :param alert_type: The alert type of events generated from the email address.
        :type alert_type: EventEmailAddressAlertType, optional

        :param created_at: The timestamp of when the event email address was created.
        :type created_at: datetime

        :param description: A description of the event email address.
        :type description: str, none_type, optional

        :param email: The generated email address for ingesting events.
        :type email: str

        :param format: The format of events ingested through the email address.
        :type format: EventEmailAddressFormat

        :param last_used_at: The timestamp of when the event email address was last used.
        :type last_used_at: datetime, none_type, optional

        :param notify_handles: A list of handles to notify when an email is received.
        :type notify_handles: [str], optional

        :param revoked_at: The timestamp of when the event email address was revoked.
        :type revoked_at: datetime, none_type, optional

        :param tags: A list of tags to apply to events generated from the email address.
        :type tags: [str], optional
        """
        if alert_type is not unset:
            kwargs["alert_type"] = alert_type
        if description is not unset:
            kwargs["description"] = description
        if last_used_at is not unset:
            kwargs["last_used_at"] = last_used_at
        if notify_handles is not unset:
            kwargs["notify_handles"] = notify_handles
        if revoked_at is not unset:
            kwargs["revoked_at"] = revoked_at
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.email = email
        self_.format = format
