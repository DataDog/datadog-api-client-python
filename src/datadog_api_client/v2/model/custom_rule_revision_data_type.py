# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomRuleRevisionDataType(ModelSimple):
    """
    Resource type

    :param value: If omitted defaults to "custom_rule_revision". Must be one of ["custom_rule_revision"].
    :type value: str
    """

    allowed_values = {
        "custom_rule_revision",
    }
    CUSTOM_RULE_REVISION: ClassVar["CustomRuleRevisionDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomRuleRevisionDataType.CUSTOM_RULE_REVISION = CustomRuleRevisionDataType("custom_rule_revision")
