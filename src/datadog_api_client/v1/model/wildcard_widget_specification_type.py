# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WildcardWidgetSpecificationType(ModelSimple):
    """
    Type of specification used by the wildcard widget.

    :param value: Must be one of ["vega", "vega-lite"].
    :type value: str
    """

    allowed_values = {
        "vega",
        "vega-lite",
    }
    VEGA: ClassVar["WildcardWidgetSpecificationType"]
    VEGA_LITE: ClassVar["WildcardWidgetSpecificationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WildcardWidgetSpecificationType.VEGA = WildcardWidgetSpecificationType("vega")
WildcardWidgetSpecificationType.VEGA_LITE = WildcardWidgetSpecificationType("vega-lite")
