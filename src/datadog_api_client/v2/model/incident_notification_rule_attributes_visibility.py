# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentNotificationRuleAttributesVisibility(ModelSimple):
    """
    The visibility of the notification rule.

    :param value: Must be one of ["all", "organization", "private"].
    :type value: str
    """

    allowed_values = {
        "all",
        "organization",
        "private",
    }
    ALL: ClassVar["IncidentNotificationRuleAttributesVisibility"]
    ORGANIZATION: ClassVar["IncidentNotificationRuleAttributesVisibility"]
    PRIVATE: ClassVar["IncidentNotificationRuleAttributesVisibility"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentNotificationRuleAttributesVisibility.ALL = IncidentNotificationRuleAttributesVisibility("all")
IncidentNotificationRuleAttributesVisibility.ORGANIZATION = IncidentNotificationRuleAttributesVisibility("organization")
IncidentNotificationRuleAttributesVisibility.PRIVATE = IncidentNotificationRuleAttributesVisibility("private")
