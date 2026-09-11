# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DefaultInboxRuleType(ModelSimple):
    """
    The JSON:API type for default inbox rules.

    :param value: If omitted defaults to "default_inbox_rules". Must be one of ["default_inbox_rules"].
    :type value: str
    """

    allowed_values = {
        "default_inbox_rules",
    }
    DEFAULT_INBOX_RULES: ClassVar["DefaultInboxRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DefaultInboxRuleType.DEFAULT_INBOX_RULES = DefaultInboxRuleType("default_inbox_rules")
