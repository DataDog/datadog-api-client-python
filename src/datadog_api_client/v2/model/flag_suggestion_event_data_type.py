# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FlagSuggestionEventDataType(ModelSimple):
    """
    Flag suggestion events resource type.

    :param value: If omitted defaults to "flag-suggestion-events". Must be one of ["flag-suggestion-events"].
    :type value: str
    """

    allowed_values = {
        "flag-suggestion-events",
    }
    FLAG_SUGGESTION_EVENTS: ClassVar["FlagSuggestionEventDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FlagSuggestionEventDataType.FLAG_SUGGESTION_EVENTS = FlagSuggestionEventDataType("flag-suggestion-events")
