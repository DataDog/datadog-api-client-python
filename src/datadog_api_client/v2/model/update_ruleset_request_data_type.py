# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class UpdateRulesetRequestDataType(ModelSimple):
    """
    Update ruleset resource type.

    :param value: If omitted defaults to "update_ruleset". Must be one of ["update_ruleset"].
    :type value: str
    """

    allowed_values = {
        "update_ruleset",
    }
    UPDATE_RULESET: ClassVar["UpdateRulesetRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UpdateRulesetRequestDataType.UPDATE_RULESET = UpdateRulesetRequestDataType("update_ruleset")
