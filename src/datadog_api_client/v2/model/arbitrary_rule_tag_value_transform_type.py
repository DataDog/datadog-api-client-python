# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ArbitraryRuleTagValueTransformType(ModelSimple):
    """
    The kind of transform.

    :param value: Must be one of ["string_replace", "regex_extract", "regex_replace", "lookup_map"].
    :type value: str
    """

    allowed_values = {
        "string_replace",
        "regex_extract",
        "regex_replace",
        "lookup_map",
    }
    STRING_REPLACE: ClassVar["ArbitraryRuleTagValueTransformType"]
    REGEX_EXTRACT: ClassVar["ArbitraryRuleTagValueTransformType"]
    REGEX_REPLACE: ClassVar["ArbitraryRuleTagValueTransformType"]
    LOOKUP_MAP: ClassVar["ArbitraryRuleTagValueTransformType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ArbitraryRuleTagValueTransformType.STRING_REPLACE = ArbitraryRuleTagValueTransformType("string_replace")
ArbitraryRuleTagValueTransformType.REGEX_EXTRACT = ArbitraryRuleTagValueTransformType("regex_extract")
ArbitraryRuleTagValueTransformType.REGEX_REPLACE = ArbitraryRuleTagValueTransformType("regex_replace")
ArbitraryRuleTagValueTransformType.LOOKUP_MAP = ArbitraryRuleTagValueTransformType("lookup_map")
