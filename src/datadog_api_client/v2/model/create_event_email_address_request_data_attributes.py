# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CreateEventEmailAddressRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "alert_type": (str,),
            "description": (str,),
            "format": (str,),
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
        format: str,
        notify_handles: List[str],
        tags: List[str],
        alert_type: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param alert_type:
        :type alert_type: str, optional

        :param description:
        :type description: str, optional

        :param format:
        :type format: str

        :param notify_handles:
        :type notify_handles: [str]

        :param tags:
        :type tags: [str]
        """
        if alert_type is not unset:
            kwargs["alert_type"] = alert_type
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.format = format
        self_.notify_handles = notify_handles
        self_.tags = tags
