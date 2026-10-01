# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DashboardExperienceType(ModelSimple):
    """
    The experience type of the dashboard.

    :param value: Must be one of ["default", "product_analytics"].
    :type value: str
    """

    allowed_values = {
        "default",
        "product_analytics",
    }
    DEFAULT: ClassVar["DashboardExperienceType"]
    PRODUCT_ANALYTICS: ClassVar["DashboardExperienceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DashboardExperienceType.DEFAULT = DashboardExperienceType("default")
DashboardExperienceType.PRODUCT_ANALYTICS = DashboardExperienceType("product_analytics")
