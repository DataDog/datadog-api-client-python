# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RulesetStatusRespDataType(ModelSimple):
    """
    Ruleset status resource type.

    :param value: If omitted defaults to "ruleset_status". Must be one of ["ruleset_status"].
    :type value: str
    """

    allowed_values = {
        "ruleset_status",
    }
    RULESET_STATUS: ClassVar["RulesetStatusRespDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RulesetStatusRespDataType.RULESET_STATUS = RulesetStatusRespDataType("ruleset_status")
