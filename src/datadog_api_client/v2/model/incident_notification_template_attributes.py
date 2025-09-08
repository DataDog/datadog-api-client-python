# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class IncidentNotificationTemplateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "category": (str,),
            "content": (str,),
            "created": (datetime,),
            "modified": (datetime,),
            "name": (str,),
            "subject": (str,),
        }

    attribute_map = {
        "category": "category",
        "content": "content",
        "created": "created",
        "modified": "modified",
        "name": "name",
        "subject": "subject",
    }
    read_only_vars = {
        "created",
        "modified",
    }

    def __init__(
        self_, category: str, content: str, created: datetime, modified: datetime, name: str, subject: str, **kwargs
    ):
        """
        The notification template's attributes.

        :param category: The category of the notification template.
        :type category: str

        :param content: The content body of the notification template.
        :type content: str

        :param created: Timestamp when the notification template was created.
        :type created: datetime

        :param modified: Timestamp when the notification template was last modified.
        :type modified: datetime

        :param name: The name of the notification template.
        :type name: str

        :param subject: The subject line of the notification template.
        :type subject: str
        """
        super().__init__(kwargs)

        self_.category = category
        self_.content = content
        self_.created = created
        self_.modified = modified
        self_.name = name
        self_.subject = subject
