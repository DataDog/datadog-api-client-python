# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SankeyRumDataSource(ModelSimple):
    """
    Sankey widget with RUM data source.

    :param value: If omitted defaults to "rum". Must be one of ["rum", "product_analytics"].
    :type value: str
    """

    allowed_values = {
        "rum",
        "product_analytics",
    }
    RUM: ClassVar["SankeyRumDataSource"]
    PRODUCT_ANALYTICS: ClassVar["SankeyRumDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SankeyRumDataSource.RUM = SankeyRumDataSource("rum")
SankeyRumDataSource.PRODUCT_ANALYTICS = SankeyRumDataSource("product_analytics")
