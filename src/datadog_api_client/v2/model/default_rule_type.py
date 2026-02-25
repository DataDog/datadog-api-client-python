# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DefaultRuleType(ModelSimple):
    """
    The JSON:API type for default rules.

    :param value: If omitted defaults to "default-rule". Must be one of ["default-rule"].
    :type value: str
    """

    allowed_values = {
        "default-rule",
    }
    DEFAULT_RULE: ClassVar["DefaultRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DefaultRuleType.DEFAULT_RULE = DefaultRuleType("default-rule")
