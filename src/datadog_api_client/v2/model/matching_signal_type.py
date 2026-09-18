# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MatchingSignalType(ModelSimple):
    """
    The type of the resource. The value should always be `matching_signal`.

    :param value: If omitted defaults to "matching_signal". Must be one of ["matching_signal"].
    :type value: str
    """

    allowed_values = {
        "matching_signal",
    }
    MATCHING_SIGNAL: ClassVar["MatchingSignalType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MatchingSignalType.MATCHING_SIGNAL = MatchingSignalType("matching_signal")
