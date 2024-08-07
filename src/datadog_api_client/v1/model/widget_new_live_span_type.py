# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WidgetNewLiveSpanType(ModelSimple):
    """
    Type "live" denotes a live span in the new format.

    :param value: If omitted defaults to "live". Must be one of ["live"].
    :type value: str
    """

    allowed_values = {
        "live",
    }
    LIVE: ClassVar["WidgetNewLiveSpanType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetNewLiveSpanType.LIVE = WidgetNewLiveSpanType("live")
