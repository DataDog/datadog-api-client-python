# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsRetentionGridCohortType(ModelSimple):
    """
    Whether the row holds one cohort's own numbers, or the weighted roll-up across every cohort.

    :param value: Must be one of ["raw", "aggregated"].
    :type value: str
    """

    allowed_values = {
        "raw",
        "aggregated",
    }
    RAW: ClassVar["ProductAnalyticsRetentionGridCohortType"]
    AGGREGATED: ClassVar["ProductAnalyticsRetentionGridCohortType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsRetentionGridCohortType.RAW = ProductAnalyticsRetentionGridCohortType("raw")
ProductAnalyticsRetentionGridCohortType.AGGREGATED = ProductAnalyticsRetentionGridCohortType("aggregated")
