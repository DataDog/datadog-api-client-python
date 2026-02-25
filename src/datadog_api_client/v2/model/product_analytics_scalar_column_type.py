# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsScalarColumnType(ModelSimple):
    """
    Column type.

    :param value: Must be one of ["number", "group"].
    :type value: str
    """

    allowed_values = {
        "number",
        "group",
    }
    NUMBER: ClassVar["ProductAnalyticsScalarColumnType"]
    GROUP: ClassVar["ProductAnalyticsScalarColumnType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsScalarColumnType.NUMBER = ProductAnalyticsScalarColumnType("number")
ProductAnalyticsScalarColumnType.GROUP = ProductAnalyticsScalarColumnType("group")
