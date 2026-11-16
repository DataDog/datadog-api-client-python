# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FeatureFlagSuggestionDataType(ModelSimple):
    """
    The resource type for feature flag suggestions.

    :param value: If omitted defaults to "flag-suggestions". Must be one of ["flag-suggestions"].
    :type value: str
    """

    allowed_values = {
        "flag-suggestions",
    }
    FLAG_SUGGESTIONS: ClassVar["FeatureFlagSuggestionDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FeatureFlagSuggestionDataType.FLAG_SUGGESTIONS = FeatureFlagSuggestionDataType("flag-suggestions")
