# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonthlyResourceType(ModelSimple):
    """
    Type of a monthly resource usage record.

    :param value: If omitted defaults to "monthly_resource". Must be one of ["monthly_resource"].
    :type value: str
    """

    allowed_values = {
        "monthly_resource",
    }
    MONTHLY_RESOURCE: ClassVar["MonthlyResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonthlyResourceType.MONTHLY_RESOURCE = MonthlyResourceType("monthly_resource")
