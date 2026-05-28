# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HostMapWidgetDimension(ModelSimple):
    """
    Visual dimension driven by a formula in the infrastructure host map widget.

    :param value: Must be one of ["node", "fill", "size"].
    :type value: str
    """

    allowed_values = {
        "node",
        "fill",
        "size",
    }
    NODE: ClassVar["HostMapWidgetDimension"]
    FILL: ClassVar["HostMapWidgetDimension"]
    SIZE: ClassVar["HostMapWidgetDimension"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HostMapWidgetDimension.NODE = HostMapWidgetDimension("node")
HostMapWidgetDimension.FILL = HostMapWidgetDimension("fill")
HostMapWidgetDimension.SIZE = HostMapWidgetDimension("size")
