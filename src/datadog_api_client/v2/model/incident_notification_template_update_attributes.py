# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IncidentNotificationTemplateUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "category": (str,),
            "content": (str,),
            "name": (str,),
            "subject": (str,),
        }

    attribute_map = {
        "category": "category",
        "content": "content",
        "name": "name",
        "subject": "subject",
    }

    def __init__(
        self_,
        category: Union[str, UnsetType] = unset,
        content: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        subject: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes to update on a notification template.

        :param category: The category of the notification template.
        :type category: str, optional

        :param content: The content body of the notification template.
        :type content: str, optional

        :param name: The name of the notification template.
        :type name: str, optional

        :param subject: The subject line of the notification template.
        :type subject: str, optional
        """
        if category is not unset:
            kwargs["category"] = category
        if content is not unset:
            kwargs["content"] = content
        if name is not unset:
            kwargs["name"] = name
        if subject is not unset:
            kwargs["subject"] = subject
        super().__init__(kwargs)
