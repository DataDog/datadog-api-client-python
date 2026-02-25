# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsExecutionType(ModelSimple):
    """
    Override the query execution strategy.

    :param value: Must be one of ["simple", "background", "trino-multistep", "materialized-view"].
    :type value: str
    """

    allowed_values = {
        "simple",
        "background",
        "trino-multistep",
        "materialized-view",
    }
    SIMPLE: ClassVar["ProductAnalyticsExecutionType"]
    BACKGROUND: ClassVar["ProductAnalyticsExecutionType"]
    TRINO_MULTISTEP: ClassVar["ProductAnalyticsExecutionType"]
    MATERIALIZED_VIEW: ClassVar["ProductAnalyticsExecutionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsExecutionType.SIMPLE = ProductAnalyticsExecutionType("simple")
ProductAnalyticsExecutionType.BACKGROUND = ProductAnalyticsExecutionType("background")
ProductAnalyticsExecutionType.TRINO_MULTISTEP = ProductAnalyticsExecutionType("trino-multistep")
ProductAnalyticsExecutionType.MATERIALIZED_VIEW = ProductAnalyticsExecutionType("materialized-view")
