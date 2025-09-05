# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentNotificationTemplateType(ModelSimple):
    """
    Notification templates resource type.

    :param value: If omitted defaults to "notification_templates". Must be one of ["notification_templates"].
    :type value: str
    """

    allowed_values = {
        "notification_templates",
    }
    NOTIFICATION_TEMPLATES: ClassVar["IncidentNotificationTemplateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentNotificationTemplateType.NOTIFICATION_TEMPLATES = IncidentNotificationTemplateType("notification_templates")
