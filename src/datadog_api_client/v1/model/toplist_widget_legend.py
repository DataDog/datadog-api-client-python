# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ToplistWidgetLegend(ModelSimple):
    """
    Top list widget stacked legend behavior.

    :param value: Must be one of ["automatic", "inline", "none"].
    :type value: str
    """

    allowed_values = {
        "automatic",
        "inline",
        "none",
    }
    AUTOMATIC: ClassVar["ToplistWidgetLegend"]
    INLINE: ClassVar["ToplistWidgetLegend"]
    NONE: ClassVar["ToplistWidgetLegend"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ToplistWidgetLegend.AUTOMATIC = ToplistWidgetLegend("automatic")
ToplistWidgetLegend.INLINE = ToplistWidgetLegend("inline")
ToplistWidgetLegend.NONE = ToplistWidgetLegend("none")
