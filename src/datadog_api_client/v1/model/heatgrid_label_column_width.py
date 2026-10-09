# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HeatgridLabelColumnWidth(ModelSimple):
    """
    Width of the label column.

    :param value: Must be one of ["xs", "s", "m", "l", "xl"].
    :type value: str
    """

    allowed_values = {
        "xs",
        "s",
        "m",
        "l",
        "xl",
    }
    XS: ClassVar["HeatgridLabelColumnWidth"]
    S: ClassVar["HeatgridLabelColumnWidth"]
    M: ClassVar["HeatgridLabelColumnWidth"]
    L: ClassVar["HeatgridLabelColumnWidth"]
    XL: ClassVar["HeatgridLabelColumnWidth"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HeatgridLabelColumnWidth.XS = HeatgridLabelColumnWidth("xs")
HeatgridLabelColumnWidth.S = HeatgridLabelColumnWidth("s")
HeatgridLabelColumnWidth.M = HeatgridLabelColumnWidth("m")
HeatgridLabelColumnWidth.L = HeatgridLabelColumnWidth("l")
HeatgridLabelColumnWidth.XL = HeatgridLabelColumnWidth("xl")
