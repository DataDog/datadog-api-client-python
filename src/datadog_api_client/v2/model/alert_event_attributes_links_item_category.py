# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AlertEventAttributesLinksItemCategory(ModelSimple):
    """
    The category of the link.

    :param value: Must be one of ["runbook", "documentation", "dashboard"].
    :type value: str
    """

    allowed_values = {
        "runbook",
        "documentation",
        "dashboard",
    }
    RUNBOOK: ClassVar["AlertEventAttributesLinksItemCategory"]
    DOCUMENTATION: ClassVar["AlertEventAttributesLinksItemCategory"]
    DASHBOARD: ClassVar["AlertEventAttributesLinksItemCategory"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AlertEventAttributesLinksItemCategory.RUNBOOK = AlertEventAttributesLinksItemCategory("runbook")
AlertEventAttributesLinksItemCategory.DOCUMENTATION = AlertEventAttributesLinksItemCategory("documentation")
AlertEventAttributesLinksItemCategory.DASHBOARD = AlertEventAttributesLinksItemCategory("dashboard")
