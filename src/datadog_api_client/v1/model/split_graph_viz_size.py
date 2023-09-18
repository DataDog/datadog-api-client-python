# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SplitGraphVizSize(ModelSimple):
    """
    Size of the individual graphs in the split.

    :param value: Must be one of ["xs", "sm", "md", "lg"].
    :type value: str
    """

    allowed_values = {
        "xs",
        "sm",
        "md",
        "lg",
    }
    XS: ClassVar["SplitGraphVizSize"]
    SM: ClassVar["SplitGraphVizSize"]
    MD: ClassVar["SplitGraphVizSize"]
    LG: ClassVar["SplitGraphVizSize"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SplitGraphVizSize.XS = SplitGraphVizSize("xs")
SplitGraphVizSize.SM = SplitGraphVizSize("sm")
SplitGraphVizSize.MD = SplitGraphVizSize("md")
SplitGraphVizSize.LG = SplitGraphVizSize("lg")
