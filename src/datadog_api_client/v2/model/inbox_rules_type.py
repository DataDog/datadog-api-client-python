# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class InboxRulesType(ModelSimple):
    """
    The pipeline rule type associated to inbox rules

    :param value: If omitted defaults to "inbox_rules". Must be one of ["inbox_rules"].
    :type value: str
    """

    allowed_values = {
        "inbox_rules",
    }
    INBOX_RULES: ClassVar["InboxRulesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


InboxRulesType.INBOX_RULES = InboxRulesType("inbox_rules")
