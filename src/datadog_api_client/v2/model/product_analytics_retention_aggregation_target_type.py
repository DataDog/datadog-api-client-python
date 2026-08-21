# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsRetentionAggregationTargetType(ModelSimple):
    """
    The discriminator identifying a target selected by aggregation.

    :param value: If omitted defaults to "aggregation". Must be one of ["aggregation"].
    :type value: str
    """

    allowed_values = {
        "aggregation",
    }
    AGGREGATION: ClassVar["ProductAnalyticsRetentionAggregationTargetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsRetentionAggregationTargetType.AGGREGATION = ProductAnalyticsRetentionAggregationTargetType(
    "aggregation"
)
