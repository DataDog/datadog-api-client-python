# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ArbitraryRuleResponseDataType(ModelSimple):
    """
    Arbitrary rule resource type.

    :param value: If omitted defaults to "arbitrary_rule". Must be one of ["arbitrary_rule"].
    :type value: str
    """

    allowed_values = {
        "arbitrary_rule",
    }
    ARBITRARY_RULE: ClassVar["ArbitraryRuleResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ArbitraryRuleResponseDataType.ARBITRARY_RULE = ArbitraryRuleResponseDataType("arbitrary_rule")
