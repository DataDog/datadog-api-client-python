# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WidgetExperienceType(ModelSimple):
    """
    Widget experience types that differentiate between the products using the specific widget.

    :param value: Must be one of ["ccm_reports", "logs_reports", "csv_reports", "product_analytics"].
    :type value: str
    """

    allowed_values = {
        "ccm_reports",
        "logs_reports",
        "csv_reports",
        "product_analytics",
    }
    CCM_REPORTS: ClassVar["WidgetExperienceType"]
    LOGS_REPORTS: ClassVar["WidgetExperienceType"]
    CSV_REPORTS: ClassVar["WidgetExperienceType"]
    PRODUCT_ANALYTICS: ClassVar["WidgetExperienceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetExperienceType.CCM_REPORTS = WidgetExperienceType("ccm_reports")
WidgetExperienceType.LOGS_REPORTS = WidgetExperienceType("logs_reports")
WidgetExperienceType.CSV_REPORTS = WidgetExperienceType("csv_reports")
WidgetExperienceType.PRODUCT_ANALYTICS = WidgetExperienceType("product_analytics")
