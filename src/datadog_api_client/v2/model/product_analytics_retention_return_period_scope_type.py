# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsRetentionReturnPeriodScopeType(ModelSimple):
    """
    The discriminator identifying a scope narrowed to one return period.

    :param value: If omitted defaults to "return_period". Must be one of ["return_period"].
    :type value: str
    """

    allowed_values = {
        "return_period",
    }
    RETURN_PERIOD: ClassVar["ProductAnalyticsRetentionReturnPeriodScopeType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsRetentionReturnPeriodScopeType.RETURN_PERIOD = ProductAnalyticsRetentionReturnPeriodScopeType(
    "return_period"
)
