# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiCustomRuleRevisionDataType(ModelSimple):
    """
    AI custom rule revision resource type.

    :param value: If omitted defaults to "ai_rule_revision". Must be one of ["ai_rule_revision"].
    :type value: str
    """

    allowed_values = {
        "ai_rule_revision",
    }
    AI_RULE_REVISION: ClassVar["AiCustomRuleRevisionDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiCustomRuleRevisionDataType.AI_RULE_REVISION = AiCustomRuleRevisionDataType("ai_rule_revision")
