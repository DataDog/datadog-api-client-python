# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardWidgetValidationReflowType(ModelSimple):
    """
    Reflow behavior used for an ordered dashboard.

    :param value: Must be one of ["auto", "fixed"].
    :type value: str
    """

    allowed_values = {
        "auto",
        "fixed",
    }
    AUTO: ClassVar["DashboardWidgetValidationReflowType"]
    FIXED: ClassVar["DashboardWidgetValidationReflowType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardWidgetValidationReflowType.AUTO = DashboardWidgetValidationReflowType("auto")
DashboardWidgetValidationReflowType.FIXED = DashboardWidgetValidationReflowType("fixed")
