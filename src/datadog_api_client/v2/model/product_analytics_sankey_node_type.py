# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsSankeyNodeType(ModelSimple):
    """
    Node type.

    :param value: Must be one of ["regular", "other", "dropoff"].
    :type value: str
    """

    allowed_values = {
        "regular",
        "other",
        "dropoff",
    }
    REGULAR: ClassVar["ProductAnalyticsSankeyNodeType"]
    OTHER: ClassVar["ProductAnalyticsSankeyNodeType"]
    DROPOFF: ClassVar["ProductAnalyticsSankeyNodeType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsSankeyNodeType.REGULAR = ProductAnalyticsSankeyNodeType("regular")
ProductAnalyticsSankeyNodeType.OTHER = ProductAnalyticsSankeyNodeType("other")
ProductAnalyticsSankeyNodeType.DROPOFF = ProductAnalyticsSankeyNodeType("dropoff")
