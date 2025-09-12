# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RulesetRespDataType(ModelSimple):
    """
    Ruleset resource type.

    :param value: If omitted defaults to "ruleset". Must be one of ["ruleset"].
    :type value: str
    """

    allowed_values = {
        "ruleset",
    }
    RULESET: ClassVar["RulesetRespDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RulesetRespDataType.RULESET = RulesetRespDataType("ruleset")
