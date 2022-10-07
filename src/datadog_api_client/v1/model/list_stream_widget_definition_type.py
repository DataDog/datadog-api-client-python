# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ListStreamWidgetDefinitionType(ModelSimple):
    """
    Type of the list stream widget.

    :param value: If omitted defaults to "list_stream". Must be one of ["list_stream"].
    :type value: str
    """

    allowed_values = {
        "list_stream",
    }
    LIST_STREAM: ClassVar["ListStreamWidgetDefinitionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ListStreamWidgetDefinitionType.LIST_STREAM = ListStreamWidgetDefinitionType("list_stream")
