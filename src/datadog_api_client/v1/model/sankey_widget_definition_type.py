# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SankeyWidgetDefinitionType(ModelSimple):
    """
    Type of the Sankey widget.

    :param value: If omitted defaults to "sankey". Must be one of ["sankey"].
    :type value: str
    """

    allowed_values = {
        "sankey",
    }
    SANKEY: ClassVar["SankeyWidgetDefinitionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SankeyWidgetDefinitionType.SANKEY = SankeyWidgetDefinitionType("sankey")
