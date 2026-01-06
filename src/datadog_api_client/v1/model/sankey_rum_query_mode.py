# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SankeyRumQueryMode(ModelSimple):
    """
    Sankey mode for RUM queries.

    :param value: If omitted defaults to "source". Must be one of ["source", "target"].
    :type value: str
    """

    allowed_values = {
        "source",
        "target",
    }
    SOURCE: ClassVar["SankeyRumQueryMode"]
    TARGET: ClassVar["SankeyRumQueryMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SankeyRumQueryMode.SOURCE = SankeyRumQueryMode("source")
SankeyRumQueryMode.TARGET = SankeyRumQueryMode("target")
