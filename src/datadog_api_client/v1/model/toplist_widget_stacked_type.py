# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ToplistWidgetStackedType(ModelSimple):
    """
    Top list widget stacked display type.

    :param value: If omitted defaults to "stacked". Must be one of ["stacked"].
    :type value: str
    """

    allowed_values = {
        "stacked",
    }
    STACKED: ClassVar["ToplistWidgetStackedType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ToplistWidgetStackedType.STACKED = ToplistWidgetStackedType("stacked")
