# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class EventEmailAddressResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "alert_type": (str,),
            "created_at": (datetime,),
            "description": (str,),
            "email": (str,),
            "format": (str,),
            "last_used_at": (datetime,),
            "notify_handles": ([str],),
            "revoked_at": (datetime,),
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
        format: str,
        notify_handles: List[str],
        tags: List[str],
        alert_type: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        last_used_at: Union[datetime, UnsetType] = unset,
        revoked_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param alert_type:
        :type alert_type: str, optional

        :param created_at:
        :type created_at: datetime

        :param description:
        :type description: str, optional

        :param email:
        :type email: str

        :param format:
        :type format: str

        :param last_used_at:
        :type last_used_at: datetime, optional

        :param notify_handles:
        :type notify_handles: [str]

        :param revoked_at:
        :type revoked_at: datetime, optional

        :param tags:
        :type tags: [str]
        """
        if alert_type is not unset:
            kwargs["alert_type"] = alert_type
        if description is not unset:
            kwargs["description"] = description
        if last_used_at is not unset:
            kwargs["last_used_at"] = last_used_at
        if revoked_at is not unset:
            kwargs["revoked_at"] = revoked_at
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.email = email
        self_.format = format
        self_.notify_handles = notify_handles
        self_.tags = tags
