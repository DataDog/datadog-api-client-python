# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RuleBasedViewType(ModelSimple):
    """
    The type of the resource. The value should always be `rule_based_view`.

    :param value: If omitted defaults to "rule_based_view". Must be one of ["rule_based_view"].
    :type value: str
    """

    allowed_values = {
        "rule_based_view",
    }
    RULE_BASED_VIEW: ClassVar["RuleBasedViewType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RuleBasedViewType.RULE_BASED_VIEW = RuleBasedViewType("rule_based_view")
