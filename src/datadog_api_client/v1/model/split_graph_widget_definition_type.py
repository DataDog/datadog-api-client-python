# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SplitGraphWidgetDefinitionType(ModelSimple):
    """
    Type of the split graph widget

    :param value: If omitted defaults to "split_group". Must be one of ["split_group"].
    :type value: str
    """

    allowed_values = {
        "split_group",
    }
    SPLIT_GROUP: ClassVar["SplitGraphWidgetDefinitionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SplitGraphWidgetDefinitionType.SPLIT_GROUP = SplitGraphWidgetDefinitionType("split_group")
