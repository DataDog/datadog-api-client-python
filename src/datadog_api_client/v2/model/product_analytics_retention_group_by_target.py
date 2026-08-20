# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsRetentionGroupByTarget(ModelSimple):
    """
    Which axis of the retention grid a group-by applies to.

    :param value: Must be one of ["cohort", "return_period"].
    :type value: str
    """

    allowed_values = {
        "cohort",
        "return_period",
    }
    COHORT: ClassVar["ProductAnalyticsRetentionGroupByTarget"]
    RETURN_PERIOD: ClassVar["ProductAnalyticsRetentionGroupByTarget"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsRetentionGroupByTarget.COHORT = ProductAnalyticsRetentionGroupByTarget("cohort")
ProductAnalyticsRetentionGroupByTarget.RETURN_PERIOD = ProductAnalyticsRetentionGroupByTarget("return_period")
