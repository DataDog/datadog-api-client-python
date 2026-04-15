# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RetentionReturnCriteriaTimeIntervalType(ModelSimple):
    """
    Type of time interval for return criteria.

    :param value: If omitted defaults to "fixed". Must be one of ["fixed"].
    :type value: str
    """

    allowed_values = {
        "fixed",
    }
    FIXED: ClassVar["RetentionReturnCriteriaTimeIntervalType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RetentionReturnCriteriaTimeIntervalType.FIXED = RetentionReturnCriteriaTimeIntervalType("fixed")
