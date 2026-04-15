# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RetentionReturnCriteriaTimeIntervalUnit(ModelSimple):
    """
    Unit of time for retention return criteria interval.

    :param value: Must be one of ["day", "week", "month"].
    :type value: str
    """

    allowed_values = {
        "day",
        "week",
        "month",
    }
    DAY: ClassVar["RetentionReturnCriteriaTimeIntervalUnit"]
    WEEK: ClassVar["RetentionReturnCriteriaTimeIntervalUnit"]
    MONTH: ClassVar["RetentionReturnCriteriaTimeIntervalUnit"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RetentionReturnCriteriaTimeIntervalUnit.DAY = RetentionReturnCriteriaTimeIntervalUnit("day")
RetentionReturnCriteriaTimeIntervalUnit.WEEK = RetentionReturnCriteriaTimeIntervalUnit("week")
RetentionReturnCriteriaTimeIntervalUnit.MONTH = RetentionReturnCriteriaTimeIntervalUnit("month")
